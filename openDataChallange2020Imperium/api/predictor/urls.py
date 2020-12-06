from django.urls import path
from rest_framework.routers import SimpleRouter


router = SimpleRouter()
# router.register(r'', ViewSet, basename="")

urlpatterns = [
]

urlpatterns += router.urls
