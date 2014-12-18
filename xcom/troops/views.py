from django.shortcuts import render

from troops.models import Soldier

def index(request):
	soldiers = Soldier.objects.order_by('joined')#[:5]
	context = {'soldiers': soldiers}
	return render(request, 'troops/index.html', context)
