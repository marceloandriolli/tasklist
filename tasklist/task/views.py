from django.shortcuts import render,redirect,get_object_or_404

from .forms import TaskForm
from .models import Task

# Esse endpoint lista todoas as tarefas
def list(request):
	template_name = 'list.html'

	tasks = Task.objects.all()


	context = {
		'is_list':True,
		'tasks': tasks
	}

	return render(request, template_name, context)

# Esse endpoint cria as tarefas
def create(request):
	template_name = 'create.html'

	if request.method == 'POST':
		form = TaskForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('task:list')
	else:
		form = 	TaskForm()	
		
	context = {
		'is_list':False,
		'form': form
	}

	return render(request, template_name, context)	

# Esse endpoint edita as taredas
def edit(request, id):
	template_name = 'edit.html'
	context = {}
	edit_task = get_object_or_404(Task, id=id)

	context['is_list'] = False

	if request.method == 'POST':
		form = TaskForm(request.POST, instance=edit_task)
		if form.is_valid():
			form.save()
			return redirect('task:list')
	else:		
		form = TaskForm(initial={'name': edit_task.name, 
			'description': edit_task.description, 
			'status': edit_task.status}
		)
	context['form'] = form

	return render(request, template_name, context)

# Este endpoint deleta as tarefas
def delete(request, id):
	
	context = {}
	if Task.objects.filter(id=id).exists():
		Task.objects.get(id=id).delete()

	return redirect('task:list')


