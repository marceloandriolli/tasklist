from django import forms
from django.forms import ModelForm, TextInput, Select
from django.forms.widgets import CheckboxInput
from django.forms.fields import IntegerField
from .models import Task



class TaskForm(ModelForm):
	class Meta:
		model = Task
		fields = ('name','description','status')
		widgets = {
			'name': TextInput(attrs={'class' : 'form-control'}),
			'description': TextInput(attrs={'class' : 'form-control'}),
			'status': Select(attrs={'class' : 'selectpicker'})

		}