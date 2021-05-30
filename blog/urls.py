from django.urls import path
from .views import (
	BlogListView,
	BlogDetailView,
	BlogUpdateView,
	BlogDeleteView,
	BlogCreateView
)


urlpatterns = [
	path('',BlogListView.as_view(), name='blog_list'),
	path('<int:pk>/', BlogDetailView.as_view(),name='blog_detail'),
	path('<int:pk>/edit/', BlogUpdateView.as_view(),name='blog_edit'),
	path('<int:pk>/delete/',BlogDeleteView.as_view(),name = 'blog_delete'),
	path('new/',BlogCreateView.as_view(),name='blog_new')

]