from django.shortcuts import render
from django.template import RequestContext

# Create your views here.

def index(request):
	context = {}
	return render(request, 'michaela/index.html', context)
