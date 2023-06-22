from typing import Any
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# Create your views here.

# Function Based Views:

# List:
def todo_list(request):
    from .models import Todo
    
    todos = Todo.objects.all()
    # context dictionary'si icindeki her bir key template(.html) icinde degisken olarak algilanacaktir.
    context = {
        "todos" : todos
    }
    return render(request,'list.html',context)

    """
    def render(
      request: HttpRequest | None,
      template_name: str | Sequence[str],
      context: Mapping[str, Any] | None = ...,
      content_type: str | None = ...,
      status: int | None = ...,
      using: str | None = ...
    ) -> HttpResponse
    """

# Add:
def todo_add(request):
    from .forms import TodoForm
    from django.contrib import messages
    from django.shortcuts import redirect

    # print(request.POST) # <QueryDict: {'csrfmiddlewaretoken': ['NRQL4bhgs9GA499kDdwYlZRiAlAMm1zfudQAQaTwdcS8pdLSPadAc8WD83QJ6czJ'], 'title': ['asdf'], 'description': ['asdf'], 'status': ['C'], 'priority': ['3']}>

    if request.POST:
        form = TodoForm(request.POST)
        form.save()
    else:
        form = TodoForm()

    # Yukaridaki if block'ui ile ayni logic asagidaki sekilde kurulabilir.
    form = TodoForm(request.POST or None)
    # arguman karsiligi data = request.POST or None
    """
    class TodoForm(
      data: _DataT | None = ...,
      files: _FilesT | None = ...,
      auto_id: bool | str = ...,
      prefix: str | None = ...,
      initial: Mapping[str, Any] | None = ...,
      error_class: Type[ErrorList] = ...,
      label_suffix: str | None = ...,
      empty_permitted: bool = ...,
      instance: Any | None = ...,
      use_required_attribute: bool | None = ...,
      renderer: BaseRenderer = ...
    )
    """

    if form.is_valid():
        form.save()
        # Message:
        messages.success(request,'Kaydedildi.')
        # If OK redirect:
        return redirect('todo_list') # redirect('path_name')


    context = {
        'form' : form
    }

    # return render(request,'add.html',context)
    return render(request,'add_update.html',context)

# Update:
def todo_update(request, pk):
    from .models import Todo
    from .forms import TodoForm
    from django.contrib import messages
    from django.shortcuts import redirect

    todo = Todo.objects.get(id=pk)
    form = TodoForm(instance=todo)
    if request.method== "POST":
        form = TodoForm(data = request.POST, instance=todo)
        if form.is_valid():
            form.save()
            messages.success(request, 'Güncellendi.')
            return redirect("todo_list")
    
    context = {
        'form': form,
        'todo': todo
    }

    # return render(request, 'update.html', context)
    return render(request, 'add_update.html', context)

# Delete:
def todo_delete(request, pk):
    from .models import Todo
    from django.contrib import messages
    from django.shortcuts import redirect

    todo = Todo.objects.get(id=pk)
    todo.delete()
    messages.success(request, 'Silindi.')
    return redirect("todo_list")


# Class Based Views:

from django.views.generic import (
    # Generic Display
    ListView,
    DetailView,
    # Generic Editing
    CreateView,
    UpdateView,
    DeleteView,
)

# List
class TodoListView(ListView):
    from .models import Todo

    model = Todo
    ordering = ['-id'] # siralama yapma

    # env\Lib\site-packages\django\views\generic\list.py
    """
    class MultipleObjectMixin(ContextMixin):
      allow_empty = True
      queryset = None
      model = None
      paginate_by = None
      paginate_orphans = 0
      context_object_name = None
      paginator_class = Paginator
      page_kwarg = "page"
      ordering = None
    """

    # template_name = 'todo_list.html' # templates/ icinde default => modelName/modelName_list.html

    # template_name_suffix = "_list"
    # env\Lib\site-packages\django\views\generic\list.py

# Detail
class TodoDetailView(DetailView):
    from .models import Todo

    model = Todo
    # template_name = 'todo_list.html' # templates/ icinde default => modelName/modelName_detail.html

    # template_name_suffix = "_detail"
    # env\Lib\site-packages\django\views\generic\detail.py

# Create
class TodoCreateView(CreateView):
    from .models import Todo
    from .forms import TodoForm
    from django.urls import reverse_lazy
    

    model = Todo
    form_class = TodoForm
    success_url = reverse_lazy("todo_list")
    # No URL to redirect to.  Either provide a url or define a get_absolute_url method on the Model.

    # env\Lib\site-packages\django\views\generic\edit.py
    # template_name_suffix = "_form"

    # template_name = 'todo_list.html' # templates/ icinde default => modelName/modelName_form.html

    # Islem basarili olursa mesaj gosterme:
    def post(self, request, *args, **kwargs):
        from django.contrib import messages

        messages.success(request,'Kaydedildi.')
        return super().post(request, *args, **kwargs)
    


# Update
class TodoUpdateView(UpdateView):
    from .models import Todo
    from .forms import TodoForm
    from django.urls import reverse_lazy

    # env\Lib\site-packages\django\views\generic\edit.py
    # template_name_suffix = "_form"

    model = Todo
    form_class = TodoForm
    success_url = reverse_lazy("todo_list")
    # template_name = 'todo_list.html' # templates/ icinde default => modelName/modelName_form.html

    # Islem basarili olursa mesaj gosterme:
    def post(self, request, *args, **kwargs):
        from django.contrib import messages

        messages.success(request,'Guncellendi.')
        return super().post(request, *args, **kwargs)

# Delete
class TodoDeleteView(DeleteView):
    from .models import Todo
    from django.urls import reverse_lazy

    model = Todo
    # env\Lib\site-packages\django\views\generic\edit.py
    # template_name_suffix = "_confirm_delete"
    # template_name = 'todo_list.html' # templates/ icinde default => modelName/modelName_confirm_delete.html
    success_url = reverse_lazy('todo_list')

    # template dosyasına git, onay al, öyle sil:
    # def post(self, request, *args, **kwargs):
    #     from django.contrib import messages
        
    #     messages.success(request, 'Silindi.')
    #     return super().post(request, *args, **kwargs)
    
    # template dosyasına gitmeden direkt sil:
    def get(self, request, *args, **kwargs):
        from django.contrib import messages

        messages.success(request, 'Silindi.')
        return super().delete(request, *args, **kwargs)