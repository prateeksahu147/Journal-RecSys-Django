from django.db import models

class Journal(models.Model):
    class Meta:
        db_table = 'Journal'

    ID = models.CharField(primary_key=True, editable=True, unique=True, max_length=50)
    Title = models.CharField(max_length=80)
    Abstract = models.TextField(max_length=800)
    GeneralCategory = models.CharField(max_length=20)
    Category = models.CharField(max_length=40)

    def __str__(self) -> str:
        return self.ID +" "+self.Title