from candidate.models import Candidate
from candidate.models import CandidateType
from django.contrib import admin

admin.site.register(CandidateType)
admin.site.register(Candidate)
