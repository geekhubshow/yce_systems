from django.shortcuts import render
from django.http import HttpResponse


def index(request):
  return render(request, 'manifest.html', {'manifest':'active'})

def search(request):
  return render(request, 'search.html', {'search':'active'})

def create(request):
  return render(request, 'create.html', {'create':'active'})

def opinion(request):
  return render(request, 'opinion.html')
# Create your views here.
