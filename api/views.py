from django.http import Http404
from rest_framework import status
from joblib import load
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from projects.models import PredictedData
from .serializers import PredictDataSerializer
from rest_framework.permissions import IsAuthenticated


model = load('./SavedModel/crop_recommendation_model.joblib')


@api_view(['POST'])
def predict_crop(request):

    data = request.data

    nitrogen = float(data.get('nitrogen'))
    phosphorus = float(data.get('phosphorus'))
    pottasium = float(data.get('potassium'))
    temperature = float(data.get('temperature'))
    humidity = float(data.get('humidity'))
    ph = float(data.get('ph'))
    rainfall = float(data.get('rainfall'))

    recommended_crop = model.predict([[nitrogen, phosphorus, pottasium, temperature, humidity, ph, rainfall]])

    prediction_data = PredictedData.objects.create(
        profile=request.user.profile,
        nitrogen=nitrogen,
        phosphorus=phosphorus,
        pottasium=pottasium,
        temperature=temperature,
        humidity=humidity,
        ph=ph,
        rainfall=rainfall,
        recommended_crop=recommended_crop
    )

    return Response({'Recommended_Crop_is: ': recommended_crop, 'recommended_crop_id': prediction_data.id})


from django.shortcuts import get_object_or_404

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_predicted_crop(request, crop_id):
    prediction = get_object_or_404(PredictedData, id=crop_id, profile=request.user.profile)
    recommended_crop = prediction.recommended_crop

    if recommended_crop is None:
        raise Http404('Recommended crop not found')
    
    prediction_serializer = PredictDataSerializer(prediction)
    
    return Response({
        'prediction': prediction_serializer.data,
        'recommended_crop': recommended_crop
    })


@api_view(['PUT'])
def update_predicted_crop(request, crop_id):
    try:
        prediction = PredictedData.objects.get(id=crop_id, profile=request.user.profile)
    except PredictedData.DoesNotExist:
        return Response({'status: Status Not found'}, status=status.HTTP_404_NOT_FOUND)
    
    recommended_crop = prediction.recommended_crop
    
    serializer = PredictDataSerializer(prediction, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'prediction': serializer.data,'recommended_crop': recommended_crop})
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_predicted_crop(request, crop_id):
    try:
        prediction = PredictedData.objects.get(id=crop_id, profile=request.user.profile)
    except PredictedData.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    prediction.delete()
    
    return Response(status=status.HTTP_204_NO_CONTENT)    

