from django.urls import path
from . import views

urlpatterns = [
	path('', views.post_list, name= 'post_list'),
	path('post/<post_id>/', views.post_details, name='post_details'),
	path('new/', views.new_post, name= 'new_post'),
	path('edit/<int:post_id>/', views.edit_post, name='edit_post'),

]