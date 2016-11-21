from django.db import models

# Create your models here.


STATUS_CHOICES = (
    ('Concluida', 'Concluida'),
    ('Em andamento', 'Em andamento'),
    ('Criada', 'Criada'),
)
class Task(models.Model):

	name = models.CharField('Nome', max_length=70)
	description = models.CharField('Descrição', max_length=200)
	creat_at=models.DateTimeField(
		'Criado em', auto_now_add=True)
	status = models.CharField('Status', max_length=15, choices=STATUS_CHOICES)

	def __str__(self):
		return self.name
