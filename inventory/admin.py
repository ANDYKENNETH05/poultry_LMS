from django.contrib import admin

# Register your models here.
from .models import Breed, FeedType, MedicationDrug, FeedingRecord

admin.site.register(Breed)
admin.site.register(FeedType)
admin.site.register(MedicationDrug)
admin.site.register(FeedingRecord)