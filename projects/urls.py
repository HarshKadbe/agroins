from django.urls import path
from . import views

urlpatterns = [
    
    path('crop_prediction', views.CropRecommendation, name="croprecommendation"),
    path('crop_result', views.cropRecommendationResult, name="crop_result"),
    path('login', views.LoginUser, name="login"),
    path('', views.IndexPage, name="index"),
    path('register', views.RegisterUser, name="register"),
    path('logout/', views.LogoutUser, name="logout"),
    path('disease_prediction', views.Disease_prediction, name="disease-prediction"),
    path('account/', views.Account, name="account"),
    path('history/<str:pk>/', views.User_history_description, name="history"),
    
]
