from django.shortcuts import render,redirect,get_object_or_404
from .models import Task
from django.urls import reverse,reverse_lazy
from django.views.generic import DeleteView
# Create your views here.
def home(request):
    tasks = Task.objects.filter(is_completed = False).order_by('updated_at')
    ctasks = Task.objects.filter(is_completed=True)
    context ={
        "tasks":tasks,
        "ctasks":ctasks
    }
    return  render(request,'home.html', context=context)

def addTask(request):
    if request.POST:
        task = request.POST['task']
        Task.objects.create(task = task)
        return redirect(reverse('todoapp:home'))
        # return redirect('home')
        
def mark_as_done(request,pk):
    task = get_object_or_404(Task, pk = pk)
    task.is_completed = True
    task.save()
    return redirect(reverse('todoapp:home'))

def mark_as_undone(request,pk):
    task = get_object_or_404(Task, pk = pk)
    task.is_completed = False
    task.save()
    return redirect(reverse('todoapp:home'))

def editTask(request,pk):
     get_task = get_object_or_404(Task, pk = pk)
     if request.method =='POST':
         task = request.POST['task']
         get_task.task = task
         get_task.save()
         return redirect(reverse('todoapp:home'))

           
     else:
         context ={
             "get_task":get_task
         }
    
         return render(request,'edit.html', context=context)


    

def deleteTask(request,pk):
    task = get_object_or_404(Task, pk = pk)
    task.delete()
    return redirect(reverse('todoapp:home'))

    # if request.POST:
    #     id = request.POST['id']
    #     Task.objects.get(pk=id).delete()
    #     return redirect(reverse('todoapp:home'))
    
# class DeleteTask(DeleteView):
#     model = Task
#     success_url = reverse_lazy('todoapp:home')

    
