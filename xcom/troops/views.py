from django.shortcuts import render
from django.shortcuts import redirect
from django.core.exceptions import ObjectDoesNotExist
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
from itertools import chain
import sys

from troops.models import Soldier
from troops.models import Squad
from troops.models import Role
from troops.models import Rank
from troops.models import Status
from troops.models import SoldierEvent
from troops.models import Event
from troops.models import Mission
from troops.models import Stats

@csrf_exempt
def index(request):
	sys.stderr.write(str(request.GET.get('name', 'empty')) + '\n')
	if request.method == 'GET' and request.GET.get('name', 'empty') is not 'empty':
		addRookie(request.GET.get("name"))
	date = Stats.objects.get(pk=1)
	soldiers = Soldier.objects.order_by('joined')#[:5]
	events = Event.objects.order_by('date')[:5]
	missions = Mission.objects.order_by('date')[:5]
	lastevents = list(chain(events, missions))
	lastevents.sort(key=lambda r: r.date, reverse=True)
	context = {'soldiers': soldiers, 'lastevents': lastevents, 'date': date}
	return render(request, 'troops/index.html', context)
	
def soldier(request, soldier_id):
	try:
		soldier = Soldier.objects.get(pk=soldier_id)
		squads = Squad.objects.all()
		events = SoldierEvent.objects.filter(soldier=soldier.id)
	except Soldier.DoesNotExist:
		raise Http404
	return render(request, 'troops/soldier.html', {'soldier': soldier, 'events': events, 'squads': squads})

def assign(request, soldier_id):
	squad_id = request.GET.get("squad")
	sold = Soldier.objects.get(pk=soldier_id)
	if sold.squad.name != squad_id:
		squad = Squad.objects.get(name = squad_id)
		sold.squad = squad
		sold.save()
		date = Stats.objects.get(pk=1)
		if squad.name != "None":
			event = SoldierEvent()
			event.soldier = sold
			event.date = date.date
			event.event = 'Assigned to ' + squad.name + ' squad'
			event.save()
	return redirect('index')

def addRookie(name):
	date = Stats.objects.get(pk=1)
	sys.stderr.write(str(name))
	soldier = Soldier()
	soldier.name = name
	soldier.joined = date.date
	soldier.role = Role.objects.get(name='Rookie')
	soldier.squad = Squad.objects.get(name='None')
	soldier.rank = Rank.objects.get(name='Pfc')
	soldier.status = Status.objects.get(name='Ready')
	soldier.save()
	event = SoldierEvent()
	event.soldier = soldier
	event.date = date.date
	event.event = 'Joined Xcom'
	event.save()
