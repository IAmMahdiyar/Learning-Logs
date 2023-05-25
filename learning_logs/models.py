from django.db import models
from django import forms
from django.contrib.auth.models import User


class BaseModel():
    pass


class Topic(models.Model):
    text = models.TextField(max_length=200, unique=True, )
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text

    def save(
            self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        self.text = self.text.lower()
        super().save()


class Entry(models.Model):
    date_added = models.DateTimeField(auto_now=True)
    text = models.TextField()
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        return f"{self.text[:50]}"


class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text': ''}


class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': ''}
