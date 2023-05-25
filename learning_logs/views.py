from django.shortcuts import render, redirect
from django.http import HttpResponseNotFound, HttpResponseForbidden
from .models import Topic, Entry, TopicForm, EntryForm
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, "index.html")


@login_required
def topic(request, topic_text):
    user_topic = Topic.objects.filter(owner=request.user).filter(text=topic_text.lower()).first()

    if user_topic is None:
        return HttpResponseForbidden()

    context = {'topic': user_topic}
    return render(request, "topic.html", context)


@login_required
def topics(request):
    context = {'topics': Topic.objects.filter(owner=request.user).all()}
    return render(request, "topics.html", context)


@login_required
def new_topic(request):
    if request.method == "POST":
        form = TopicForm(data=request.POST)
        if form.is_valid():
            insert_topic = form.save(commit=False)
            insert_topic.owner = request.user
            insert_topic.save()
        return redirect("/topics")

    else:
        form = TopicForm()

    return render(request, "new_topic.html", {'form': form})


@login_required
def new_entry(request, topic_text):
    insert_topic = Topic.objects.filter(text=topic_text).filter(owner=request.user).first()

    if insert_topic is None:
        return HttpResponseForbidden()

    if request.method == "POST":
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = insert_topic
            new_entry.save()
        return redirect("/topic/" + str(insert_topic.text))

    else:
        form = TopicForm()

    return render(request, "new_entry.html", {'form': form, 'topic': insert_topic})


@login_required
def edit_entry(request, entry_id):
    entry = Entry.objects.filter(id=entry_id).first()

    if entry is None:
        return HttpResponseNotFound()

    if entry.topic.owner != request.user:
        return HttpResponseForbidden()

    if request.method == "POST":
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            edit_entry = form.save(commit=False)
            edit_entry.topic = entry.topic
            edit_entry.save()
        return redirect("/topic/" + str(entry.topic))
    else:
        form = EntryForm(instance=entry)
        return render(request, "edit_entry.html", {'form': form, 'topic': entry.topic})
