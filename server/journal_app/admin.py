from django.contrib import admin
from .models.Journal import Journal
from .models.JournalRecommendationModel import JournalRecommendationModel

# Register your models here.
admin.site.register(Journal)
admin.site.register(JournalRecommendationModel)