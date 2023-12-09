from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('register', views.register, name='reg'),
    path('experience', views.experience, name='experience'),
    path('education', views.education, name='education'),
    path('skills', views.skills, name='skills'),
    path('resume', views.resume, name='resume')
]