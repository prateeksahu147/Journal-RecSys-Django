from django.db import models

class JournalRecommendationModel(models.Model):
    class Meta:
        db_table = 'Journal_RecommendationModel'
    model = models.CharField(max_length=40)
    file = models.CharField(max_length=40)

    def __str__(self) -> str:
        return self.model
