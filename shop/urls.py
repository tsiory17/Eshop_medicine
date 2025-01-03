
from django.urls import path , include
from . import views
urlpatterns = [
    path('', views.home, name ='home'),
    path('about/',views.about , name = 'about'),
    path('product/<int:pk>',views.product , name = 'product'),
    path('login/', views.login_customer, name ='login'),
    path('logout/', views.logout_customer, name ='logout'),


]
