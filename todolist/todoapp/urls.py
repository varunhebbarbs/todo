from django.urls import path
from . import views
app_name = 'todoapp'
urlpatterns = [
    path('',views.home , name= 'home'),
    path('addTask/',views.addTask, name='addTask'),
    path('deletetask/<int:pk>',views.deleteTask, name = 'deleteTask'),
    path('mark_as_done/<int:pk>',views.mark_as_done, name = 'mark_as_done'),
    path('marsk_as_undone/<int:pk>',views.mark_as_undone, name='mark_as_undone'),
    path('edit/<int:pk>',views.editTask, name='editTask')
]