from django.shortcuts import render, redirect, get_object_or_404
from django import views, forms
from .models import Tasks
from django.contrib import messages
class BookListForm(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = ["title", "author","description", "rating"]
#Create object
class TaskCreateView(views.View):
    def get(self, request):
        form = BookListForm()
        return render(request=request, template_name="tasks/task_form.html", context={"form": form})
    def post(self, request):
        form = BookListForm(request.POST)
        if form.is_valid():
            task = form.save()
            messages.success(request, f"{task.title} added successfully!!!")
            return redirect('home')
        return render(request, "tasks/task_form.html", {"form": form})
#Read objects
def show_tasks(request):
    tasks = Tasks.objects.all()
    return render(request, "tasks/tasks_show.html", {"tasks": tasks})
#Update object
class TaskUpdateView(views.View):
    def get(self, request, pk):
        task = get_object_or_404(Tasks, pk=pk)
        form = BookListForm(instance=task)
        return render(request, "tasks/task_form.html", {"form": form})
    def post(self, request, pk):
        task = get_object_or_404(Tasks, pk=pk)
        form = BookListForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('home')
        return render(request, "tasks/task_form.html", {"form": form})
#Delete object
def TaskDelete(request, pk):
    task = get_object_or_404(Tasks, pk=pk)
    task.delete()
    return redirect('home')