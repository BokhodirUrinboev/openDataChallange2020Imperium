from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import TAMSAMSOMAPI

urlpatterns = [
    path('tamsamsom/', TAMSAMSOMAPI.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
