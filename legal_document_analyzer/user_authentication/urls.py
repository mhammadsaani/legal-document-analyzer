from django.urls import path
from user_authentication import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sign-up/', views.sign_up, name='sign-up'),
    path('login/', views.login_view, name='login'),
    path('change-password', views.change_password, name='change-password'),
    path('logout/', views.logout_view, name='logout'),
    path('unauthorized/', views.unauthorized, name='unauthorized'),
    
]