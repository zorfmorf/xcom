from django.shortcuts import render
from itertools import chain

from troops.models import Soldier
from troops.models import SoldierEvent
from troops.models import Event
from troops.models import Mission

def index(request):
	soldiers = Soldier.objects.order_by('joined')#[:5]
	events = Event.objects.order_by('date')[:5]
	missions = Mission.objects.order_by('date')[:5]
	lastevents = list(chain(events, missions))
	lastevents.sort(key=lambda r: r.date, reverse=True)
	context = {'soldiers': soldiers, 'lastevents': lastevents}
	return render(request, 'troops/index.html', context)
	
def soldier(request, soldier_id):
	try:
		soldier = Soldier.objects.get(pk=soldier_id)
		events = SoldierEvent.objects.filter(soldier=soldier.id)
	except Soldier.DoesNotExist:
		raise Http404
	return render(request, 'troops/soldier.html', {'soldier': soldier, 'events': events})
	
