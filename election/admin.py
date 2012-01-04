from election.models import ElectionType
from election.models import ElectionSystem
from election.models import Election
from election.models import ElectionWinners
from django.contrib import admin

admin.site.register(Election)
admin.site.register(ElectionWinners)
admin.site.register(ElectionSystem)
admin.site.register(ElectionType)
