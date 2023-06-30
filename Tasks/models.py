from django.db import models

class Tags(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    title = models.CharField(max_length=1000)
    def __str__(self) -> str:
        return f'Tag: {self.title}'

class Tasks(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    title = models.CharField(max_length=1000)
    description = models.TextField()
    finished = models.BooleanField(default=False)
    
    def __str__(self) -> str:
        return f'Task:{self.title}'

class Tasks_Tags(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    task = models.ForeignKey(Tasks, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tags, on_delete=models.CASCADE)