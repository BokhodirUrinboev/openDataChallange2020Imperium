from django.urls import path
from . import views
app_name = "openDataChallange2020Imperium.viewer"
urlpatterns = [
    path('', views.index, name='index'),
]