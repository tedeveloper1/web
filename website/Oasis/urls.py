from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    # path('services/', views.services, name='services'),
    path('contact/', views.contact, name='contact'),
    path('blog/', views.blog, name='blog'),
    path('news/', views.news, name='news')
    # path('blog/<int:blog_id>/', views.blog_detail, name='blog_detail'),
]
