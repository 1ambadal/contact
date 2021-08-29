from django.urls import path
from usr import views
app_name='usr'
urlpatterns = [
    path('', views.index, name='index'),
    path('other', views.other, name='other'),
    path('register', views.register, name='register'),
    path('login',views.user_login, name='user_login'),
    path('logout',views.user_logout, name='logout'),
    path('special',views.special, name='special')

]
