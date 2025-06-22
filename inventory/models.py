from django.db import models

# Create your models here.

class Breed(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    age = models.IntegerField(help_text="Age in months")  # You can calculate or store
    weight = models.FloatField(help_text="Average weight per animal in kg")

    def __str__(self):
        return self.name


class FeedType(models.Model):
    feed_type = models.CharField(max_length=100)
    quantity = models.FloatField()
    unit = models.CharField(max_length=20)  #
    purchase_date = models.DateField()
    expiry_date = models.DateField()

    def __str__(self):
        return self.feed_type

class MedicationDrug(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)  # New field for details

    def __str__(self):
        return self.name



class FeedingRecord(models.Model):
    breed = models.ForeignKey(Breed, on_delete=models.CASCADE)
    feed_type = models.ForeignKey(FeedType, on_delete=models.CASCADE)
    date = models.DateField()
    quantity = models.FloatField()

    def __str__(self):
        return f"{self.breed.name} fed {self.feed_type.feed_type} on {self.date}"