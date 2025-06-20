from django.views import generic
from django.urls import reverse_lazy
from .models import Todo
from .forms import TodoCreateForm


class TodoListView(generic.ListView):
    queryset = Todo.objects.all()
    template_name = 'myapp/list.html'
    context_object_name = 'todos'
    
    def get_queryset(self):
        import pdb;pdb.set_trace()
        return super().get_queryset()
    
        query=self.request.Get.get('q')
        if query:
            queryset=queryset.filter(name_contains='q')
            
        return queryset
        

class TodoCreateView(generic.CreateView):
    template_name = 'myapp/create.html'
    form_class = TodoCreateForm
    success_url = reverse_lazy('todo_list')

class TodoDetailView(generic.DetailView):
    model = Todo
    template_name = 'myapp/detail.html'
    context_object_name = 'todo'

class TodoUpdateView(generic.UpdateView):
    template_name='myapp/update.html'
    queryset=Todo.objects.all()
    form_class=TodoCreateForm
    success_url = reverse_lazy('todo_list')
    model=Todo
    
class TodoDeleteView(generic.DeleteView):
    template_name='myapp/delete.html'
    queryset=Todo.objects.all()
    success_url=reverse_lazy('todo_list')


