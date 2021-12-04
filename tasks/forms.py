from django.forms import ModelForm
from users.models import Role, User
from .models import Task


class TaskForm(ModelForm):
    def __init__(self, user: User, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)
        self.fields['assignee'].queryset = User.objects.filter(
            team=user.team).exclude(role=Role.MANAGER)
        self.instance.created_by = user

    class Meta:
        model = Task
        exclude = ('created_by',)
