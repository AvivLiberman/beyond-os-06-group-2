from django.shortcuts import redirect, render
from users.models import User
from .forms import TaskForm
from .models import Task


def create(request):
    app_user = User.objects.get(user=request.user)
    form = TaskForm(user=app_user)

    if request.method == 'POST':
        form = TaskForm(data=request.POST, user=app_user)
        if form.is_valid():
            assignee = User.objects.get(pk=request.POST['assignee'])

            Task.create_task(title=request.POST['title'],
                             assignee=assignee,
                             created_by=app_user,
                             priority=request.POST['priority'],
                             status=request.POST['status'],
                             description=request.POST['description'])
            return redirect('homepage')

    context = {'form': form}
    return render(request, 'create.html', context)
