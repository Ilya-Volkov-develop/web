from django.urls import path
from .views import *

urlpatterns = [
    path('', face, name='face_url'),
    path('video_rgb/', video_rgb, name='video_rgb'),
]
