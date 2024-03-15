from django.http import HttpResponseBadRequest
from django.shortcuts import render, redirect
import joblib
from joblib import load
from .forms import ImageUploadForm, CustomUserCreationForm
import tensorflow as tf
import numpy as np
from PIL import Image

import pandas as pd
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from projects.models import PredictedData, Profile, PredictDisease

model = load('./SavedModel/crop_recommendation_model.joblib')

def CropRecommendation(request):
    return render(request, 'crop_recommendation.html')


@login_required(login_url='login')
def cropRecommendationResult(request):
    try:
        N = float(request.POST['N'])
        P = float(request.POST['P'])
        K = float(request.POST['K'])
        temperature = float(request.POST['temperature'])
        humidity = float(request.POST['humidity'])
        ph = float(request.POST['ph'])
        rainfall = float(request.POST['rainfall'])
    except ValueError:
        return HttpResponseBadRequest("Invalid input. Please enter numeric values for all fields.")

    user_data = pd.DataFrame({
        'N': [N],
        'P': [P],
        'K': [K],
        'temperature' : [temperature],
        'humidity' : [humidity],
        'ph': [ph],
        'rainfall': [rainfall]
    })

    recommended_crop = model.predict(user_data)
    recommended_crop_str = ' '.join(recommended_crop).upper()

    profile = request.user.profile

    prediction_instance = PredictedData(
        profile=profile,
        nitrogen=N,
        phosphorus=P, 
        pottasium=K,
        temperature=temperature,
        humidity=humidity,
        ph=ph,
        rainfall=rainfall,
        recommended_crop=recommended_crop,
    )
    prediction_instance.save()

    return render(request, 'crop_result.html', {'crop': recommended_crop_str, 'profile': profile})



def IndexPage(request):
    return render(request, 'index.html')



def LoginUser(request):
    
    if request.user.is_authenticated:
        return redirect('index')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'ERROR')
            
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'ERROR')
    
    return render(request, 'loginuser.html')



def RegisterUser(request):
    
    form = CustomUserCreationForm()
    
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            
            login(request, user)
            return redirect('index')
        
    context = {'form': form}
    
    return render(request, 'register.html', context)


def LogoutUser(request):
    logout(request)
    return redirect('login')



@login_required(login_url='/login')
def Disease_prediction(request):
    profile = request.user.profile
    disease_recc = profile.predictdisease_set.all()

    class_name = ['Healthy', 'Powdery', 'Rust']

    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            model = joblib.load('./SavedModel/leaves_disease_prediction_new_model.joblib')

            image_file = form.cleaned_data['image']
            image = Image.open(image_file)
            image = image.resize((128, 128))
            input_arr = tf.keras.preprocessing.image.img_to_array(image)
            input_arr = np.array([input_arr]) 
            predictions = model.predict(input_arr)
            result_index = np.argmax(predictions)
            model_prediction = class_name[result_index]
            
            predict_disease = PredictDisease(profile=request.user.profile, LeafImage=image_file, predicted_disease=model_prediction)
            predict_disease.save()
            
            image_url = predict_disease.LeafImage.url
            
            return render(request, 'disease_result.html', {'prediction': model_prediction, 'profile': profile, 'disease_recc':disease_recc, 'image_url':image_url})
    else:
        form = ImageUploadForm()

    return render(request, 'disease_predict.html', {'form': form})



def Account(request):
    page = 'history'
    profile = request.user.profile
    crop_recc = profile.predicteddata_set.all()
    disease_recc = profile.predictdisease_set.all()
    context = {'profile': profile, 'crop_recc': crop_recc, 'disease_recc': disease_recc, 'page':page}
    return render(request, 'account.html', context)



def User_history_description(request, pk):
    profile = request.user.profile
    search_history = profile.predicteddata_set.get(id=pk)
    context = {'profile': profile,'search_history': search_history}
    return render(request, 'account.html', context)