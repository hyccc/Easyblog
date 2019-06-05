from django.urls import path, re_path
from myblog import views

urlpatterns = [
    path('', views.myBlog),
    path('blogs/', views.get_blogs),
    re_path(r'detail/(\d+)/', views.get_details, name='blog_get_detail'),
]
