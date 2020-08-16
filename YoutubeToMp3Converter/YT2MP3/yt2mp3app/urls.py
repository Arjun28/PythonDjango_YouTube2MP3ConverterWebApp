from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'yt2mp3app'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('GetInfo/',views.GetInfo, name = 'GetInfo')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)