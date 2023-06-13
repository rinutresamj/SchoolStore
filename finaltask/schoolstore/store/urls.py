from . import views
from django.urls import path
app_name='store'
urlpatterns = [
    path('homepage',views.home,name='home'),
    path('postlogin',views.postlogin,name='postlogin'),

]
