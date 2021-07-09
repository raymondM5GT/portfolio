from django.shortcuts import render, redirect
from .models import Project, Skill, Tag, Message
from .forms import ProjectForm, MessageForm
from django.contrib import messages
# Create your views here.

def homePage(request):
    projects = Project.objects.all()
    detailedskills = Skill.objects.exclude(body='')

    skills = Skill.objects.filter(body='')

    form = MessageForm()

    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message sent successfully')
    # tags = tags.objects.all()
    context = {'projects': projects, 'skills': skills, 'detailedskills': detailedskills, 'form': form}
    return render(request, 'Base/home.html', context)


def projectPage(request, pk):
    project = Project.objects.get(id=pk)
    context = {'project': project}
    return render(request, 'Base/project.html', context)

def addProject(request):
    form = ProjectForm()

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')


    context = {'form': form}
    return render(request, 'Base/projectform.html', context)


def editProject(request, pk):
    project = Project.objects.get(id=pk)
    form = ProjectForm(instance=project)

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')


    context = {'form': form}
    return render(request, 'Base/projectform.html', context)


def inboxPage(request):
    inbox = Message.objects.all().order_by('is_read')

    unreadcount = Message.objects.filter(is_read=False).count()
    context = {'inbox': inbox, 'unreadcount': unreadcount}
    return render(request, 'Base/inbox.html', context)

def messagePage(request, pk):
    message = Message.objects.get(id=pk)
    message.is_read = True
    message.save()
    context = {'message': message}
    return render(request, 'Base/message.html', context)    