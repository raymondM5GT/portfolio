from django.shortcuts import render, redirect
from .models import Project, Skill, Tag, Message, Endorsement
from .forms import ProjectForm, MessageForm, SkillForm, EndorsementForm, CommentForm
from django.contrib import messages
# Create your views here.

def homePage(request):
    projects = Project.objects.all()
    detailedskills = Skill.objects.exclude(body='')

    skills = Skill.objects.filter(body='')
    endorsements = Endorsement.objects.filter(approved=True)

    form = MessageForm()

    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message sent successfully')
    # tags = tags.objects.all()
    context = {'projects': projects, 'skills': skills, 'detailedskills': detailedskills, 'form': form, 'endorsements': endorsements}
    return render(request, 'Base/home.html', context)


def projectPage(request, pk):
    project = Project.objects.get(id=pk)
    count = project.comment_set.count()

    comments = project.comment_set.all().order_by('-created')

    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.project = project
            comment.save()
            messages.success(request, "Your Comment was successfully added !!")


    context = {'project': project, 'count': count, 'comments': comments, 'form': form}
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


def addskill(request):
    form = SkillForm()
    if request.method == 'POST':
        form = SkillForm(request.POST)
        form.save()
        messages.success(request, 'Your skill was successfully added !!')
        return redirect('home')
    context = {'form': form}
    return render(request, 'Base/skill_form.html', context)
    
def addEndorsement(request):
    form = EndorsementForm()
    if request.method == 'POST':
        form = EndorsementForm(request.POST)
        form.save()
        messages.success(request, 'Thank you, Your Endorsement was added Successfully !!')
        return redirect('home')
    context = {'form': form}
    return render(request, 'Base/endorsement_form.html', context)    
