from django.urls import path
from . import views
from .views import (
    SubjectListView, 
    SubjectDetailView, 
    SubjectCreateView, 
    SubjectUpdateView, 
    SubjectDeleteView,
)

urlpatterns = [
    path('', views.index, name='index'),
    path("login", views.login_view, name='login'),
    path("logout", views.logout_view, name='logout'),
    path("register", views.register, name='register'),
    path('subjects/', SubjectListView.as_view(), name='subject_list'),
    path('subject/<int:pk>/', SubjectDetailView.as_view(), name='subject_detail'),
    path('subject/add/', SubjectCreateView.as_view(), name='subject_add'),
    path('subject/<int:pk>/edit/', SubjectUpdateView.as_view(), name='subject_edit'),
    path('subject/<int:pk>/delete/', SubjectDeleteView.as_view(), name='subject_delete'),
    path('forum', views.forum, name='forum'),
    path("new_post", views.new_post, name="new_post"),
    path('faq', views.faq, name='faq'),
    path('contact', views.contact, name='contact'),
    path("like/<int:post_id>", views.like_post, name="like_post"),
    path('contact/submit', views.contact_submit, name='contact_submit'),
    path('resources/', views.resource_list, name='resource_list'),
    path('resources/<int:resource_id>/', views.resource_detail, name='resource_detail'),
]
