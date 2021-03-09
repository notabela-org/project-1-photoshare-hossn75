from django.urls import path

from feed import views

urlpatterns = [
    path('', views.index, name='index'),
    path('user/<str:username>', views.profile, name='profile'),
    path(r'new-post/', views.new_post, name='new-post'),
    path('edit-profile', views.editprofile, name='edit-profile'),
    path(r'post/<int:id>', views.post, name='post'),
]
