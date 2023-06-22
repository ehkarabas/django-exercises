from django.urls import path, include

from .views import (
    # FBV:
    todo_list,
    todo_add,
    todo_update,
    todo_delete,
    # CBV:
    TodoListView,
    TodoDetailView,
    TodoCreateView,
    TodoUpdateView,
    TodoDeleteView,
)

urlpatterns = [
    # FBV(Function Based Views):

    # path('list/', todo_list, name='todo_list'), # url degisse bile name uzerinden redirect yapilabilir
    # path('add/', todo_add, name='todo_add'),
    # path('update/<int:pk>', todo_update, name="todo_update"),
    # path('delete/<int:pk>', todo_delete, name="todo_delete"),

    # CBV(Class Based Views):
    path('todo_list/', TodoListView.as_view(), name="todo_list"),
    path('todo_create/', TodoCreateView.as_view(), name="todo_create"),
    path('todo_detail/<int:pk>', TodoDetailView.as_view(), name="todo_detail"),
    path('todo_update/<int:pk>', TodoUpdateView.as_view(), name="todo_update"),
    path('todo_delete/<int:pk>', TodoDeleteView.as_view(), name="todo_delete"),
]