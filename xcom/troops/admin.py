from django.contrib import admin
from troops.models import Role
from troops.models import Rank
from troops.models import Status
from troops.models import Squad
from troops.models import Soldier
from troops.models import SoldierEvent
from troops.models import MissionType
from troops.models import MissionResult
from troops.models import Mission
from troops.models import Event
from troops.models import Stats

# Register your models here.
admin.site.register(Role)
admin.site.register(Rank)
admin.site.register(Status)
admin.site.register(Squad)
admin.site.register(Soldier)
admin.site.register(SoldierEvent)
admin.site.register(MissionType)
admin.site.register(MissionResult)
admin.site.register(Mission)
admin.site.register(Event)
admin.site.register(Stats)
