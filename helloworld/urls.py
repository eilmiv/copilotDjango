from django.urls import path
from . import views

app_name = 'helloworld'

urlpatterns = [
    path('', views.WorldListView.as_view(), name='world_list'),
    path('world/new/', views.WorldCreateView.as_view(), name='world_create'),
    path('world/<int:pk>/', views.WorldDetailView.as_view(), name='world_detail'),
    path('world/<int:pk>/hello/', views.send_hello, name='send_hello'),
]
