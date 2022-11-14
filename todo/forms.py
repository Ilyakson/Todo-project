from django import forms

from todo.models import Task, Tag


class TaskForm(forms.ModelForm):
    deadline = forms.DateField(widget=forms.SelectDateWidget, required=False)
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = Task
        fields = ["content", "deadline", "tags"]
