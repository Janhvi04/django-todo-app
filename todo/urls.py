from django.contrib import admin
from django.urls import path ,include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('signup/', views.signup),
    path('loginn/', views.loginn),
    path('todopage/', views.todo),
    path('delete_todo/<int:srno>/', views.delete_todo),
    path('edit_todo/<int:srno>/', views.edit_todo, name='edit_todo'),
    path('toggle_complete/<int:srno>/', views.toggle_complete, name='toggle_complete'),
    path('signout/', views.signout, name='signout'),
    
]