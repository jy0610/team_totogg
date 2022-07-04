from django.contrib import admin
from .models import LCK_Data, rank, summerSummary

# Register your models here.
admin.site.register(LCK_Data)
admin.site.register(rank)
admin.site.register(summerSummary)