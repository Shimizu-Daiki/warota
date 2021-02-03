from django.shortcuts import render, redirect

from .models import User, Problem
from .forms import ProblemForm

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

def delete(request, pk):
  post = Problem.objects.get(pk=pk)
  post.delete()
  return redirect('index')



