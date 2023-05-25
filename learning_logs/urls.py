from django.contrib import admin
from django.urls import path, include
from .views import index, topic, topics, new_topic, new_entry, edit_entry

app_name = 'learning_logs'

urlpatterns = [
    path("", index),
    path("topics", topics),
    path("topic/<str:topic_text>/", topic),
    path("newtopic", new_topic),
    path("newentry/<str:topic_text>/", new_entry),
    path("editentry/<int:entry_id>/", edit_entry)
]
