from django.urls import path
from . import views
from django.contrib.auth import get_user_model
from django.http import HttpResponse


urlpatterns = [
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.registerPage, name="register"),

    path('',views.home, name = "home"),
    path('room/<str:pk>',views.room, name = "room"),
    path('profile/<str:pk>/', views.userProfile,name="user-profile"),

    path('create-room/',views.createRoom,name="create-room"),
    path('update-room/<str:pk>/', views.updateRoom, name="update-room"),
    path('delete-room/<str:pk>/', views.deleteRoom, name="delete-room"),
    path('delete-message/<str:pk>/', views.deleteMessage, name="delete-message"),

    path('update-user/', views.updateUser, name="update-user"),

    path('topics/', views.topicsPage, name="topics"),

    path('activity/', views.activityPage, name="activity"),

]


def create_admin_user(request):
    User = get_user_model()
    if not User.objects.filter(username='onkar').exists():
        User.objects.create_superuser('onkar', 'onkarok619@gmail.com', '72698582')
        return HttpResponse("Superuser created successfully.")
    return HttpResponse("Superuser already exists.")

urlpatterns += [
    path('create-admin/', create_admin_user),
]
