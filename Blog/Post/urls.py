from django.urls import path
from . import views, admin

urlpatterns = [
    path('', views.home, name="home"),
    path('post/<str:pk>', views.post, name="post"),
    path('form_post/', views.formulario, name="formPost"),
    path('delete-post/<str:pk>/', views.deletepost, name="delete-post"),
    path('update-post/<str:pk>/', views.updatePost, name="update-post"),
    path('registro/', views.registro, name="registro"),
    path('LeerPost/', views.leerPost, name="LeerPost"),
    path('eliminar_post/<str:pk>/', views.eliminar_post, name="ElimarPost"),
]