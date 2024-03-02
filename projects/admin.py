from django.contrib import admin

from .models import Profile, PredictDisease, PredictedData
admin.site.register(Profile)
admin.site.register(PredictDisease)
admin.site.register(PredictedData)