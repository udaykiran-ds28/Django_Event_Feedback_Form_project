
from django.urls import path
from .import views
urlpatterns = [
    path('',views.home,name='home'),
    path('show_events/', views.event_list, name='show_events'),
    path('edit/<int:id>/', views.edit_event, name='edit_event'),
    path('delete/<int:id>/', views.delete_event, name='delete_event'),
]