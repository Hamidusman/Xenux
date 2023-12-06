from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='/'),
    path('login', views.login_v, name='login'),
    path('reg', views.register, name='reg'),
    path('experience', views.experience, name='work')
]