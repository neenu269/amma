
from django.urls import path
from. import views
app_name='movieapp'
urlpatterns = [

    path('',views.index,name='index'),
    path('movie/<int:movie_id>/',views.detail,name='detail'),
    path('register/',views.register,name='register'),
    path('add/',views.add,name='add'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),




]