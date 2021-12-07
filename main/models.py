from django.db import models


class Task(models.Model):
    title = models.CharField('Название', max_length=50)
    task = models.TextField('Описание')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name ='Задача'
        verbose_name_plural ='Задачи'

class Doc(models.Model):
    name = models.CharField('Название файла', max_length=50)
    naming = models.CharField('ФИО', max_length=50)
    org = models.TextField('Организация')


class chkboxcourse(models.Model):
    coursename=models.CharField(max_length=100)


