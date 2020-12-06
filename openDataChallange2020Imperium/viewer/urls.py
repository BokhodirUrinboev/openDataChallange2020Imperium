from django.urls import path
from . import views
app_name = "openDataChallange2020Imperium.viewer"
urlpatterns = [
    path('', views.index_view, name='index'),
    path('signup/', views.sign_up_view, name='signup'),
    path('login/', views.sign_in_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('settings/', views.settings_view, name='settings'),

]