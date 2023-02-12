from django.urls import path
from . import views
from . views import ListUserView,CreateUserView,EditUserView

urlpatterns = [
    path('', views.index,name='index'),
    path('register/', views.register, name='register'),
    path('loginUser/', views.loginUser, name='loginUser'),
    path('logoutUser', views.logoutUser, name='logoutUser'),
    #path('listUser/', views.listUser, name='listUser'),    
    path('listUser/', ListUserView.as_view(),name='listUser'), #it will automatically call member_list.html
    #path('createUser/', views.createUser, name='createUser'),
    path('createUser/', CreateUserView.as_view(), name='createUser'),
    #path('editUser/<str:pk>/', views.editUser, name='editUser'),
    path('editUser/<str:pk>/', EditUserView.as_view(), name='editUser'),
]