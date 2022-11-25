from django.urls import path
from .views import *

urlpatterns = [
    path('api/upload/xray', UploadView.as_view(), name = 'prediction'),
    # path('api/upload/ct', CTUploadView.as_view(), name = 'ct_prediction'),
]