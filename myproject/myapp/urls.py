    
from django.urls import path
from .views import TodoDetailView, TodoListView
from .views import TodoCreateView,TodoUpdateView,TodoDeleteView

urlpatterns = [
    path('', TodoListView.as_view(),name='todo_list'),
    path('create', TodoCreateView.as_view(),name='todo_create'),
     path('<int:pk>', TodoDetailView.as_view(), name='todo_detail'),
      path('update/<int:pk>', TodoUpdateView.as_view(),name='todo_update'),
        path('delete/<int:pk>', TodoDeleteView.as_view(),name='todo_delete'),
]
