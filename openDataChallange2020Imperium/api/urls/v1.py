from django.urls import path, include

urlpatterns = [
    path('predictor/', include(('openDataChallange2020Imperium.api.predictor.urls', 'openDataChallange2020Imperium.api.predictor'))),
]
