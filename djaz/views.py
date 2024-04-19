from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import TodoForm
from .models import Todo
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters
from .serializers import TodoSerializer


def index(request):
    item_list = Todo.objects.order_by('-date')
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo')
    form = TodoForm()

    page = {
        'forms': form,
        'list': item_list,
        'title': 'TODO LIST',
    }
    return render(request, 'djaz/i.html', page)


def remove(request, item_id):
    item = Todo.objects.get(id=item_id)
    item.delete()
    messages.info(request, 'item removed!')
    return redirect('todo')


class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    # filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    # filterset_fields = ['title']
    # search_fields = ['title']
    # ordering_fields = '__all__'
