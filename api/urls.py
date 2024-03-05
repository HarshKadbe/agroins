from django import views
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views


urlpatterns = [
    path('predict_crop/', views.predict_crop, name='predict_crop'),
    path('get_predict_crop/<str:crop_id>/', views.get_predicted_crop, name="get_predicted_crop"),
    path('update_predict_crop/<str:crop_id>/', views.update_predicted_crop, name="update-predict-crop"),
    path('delete_predict_crop/<str:crop_id>/', views.delete_predicted_crop, name="delete-predicted-crop"),
    
    
    
]