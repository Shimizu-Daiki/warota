from django.shortcuts import render

from .models import User, Problem
from .forms import ProblemForm

def index(request):
  return render(request, 'index.html', {})
