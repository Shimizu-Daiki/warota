from django.shortcuts import render, redirect

from .models import User, Problem
from .forms import ProblemForm
from .answer_form import AnswerForm
#from use_word2vec import *

def index(request):
  posts = Problem.objects.all()
  return render(request, 'index.html', {'posts':posts})

def get_create_form(request):
  if request.method == "POST":
        form = ProblemForm(request.POST)
        if form.is_valid():
            post = form.save(commit=True)
            return redirect('index')
  else:
      form = ProblemForm()
  return render(request, 'form.html', {'form': form})

def show(request, pk):
  return render(request, 'show.html', { })

def get_answer_form(request):
  if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            post = form.save(commit=True)
            return redirect('index')
  else:
      form = AnswerForm()
  return render(request, 'answer.html', {'form': form}) 

def delete(request, pk):
  post = Problem.objects.get(pk=pk)
  post.delete()
  return redirect('index')



