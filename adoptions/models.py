from django.db import models

class Pet(models.Model):
    """
        pet model that encapsulates data about pet
        @author Anim Malvat
    """
    SEX_CHOICES = [("M", "Male"), ("F", "Female")]
    name = models.CharField(max_length=100)
    submitter = models.CharField(max_length=100)
    species = models.CharField(max_length=30)
    breed = models.CharField(max_length=30, blank=True)
    description = models.TextField()
    sex = models.CharField(max_length=1, choices=SEX_CHOICES, blank=True)
    submission_date = models.DateTimeField()
    age = models.IntegerField(null=True)
    vaccination = models.ManyToManyField("Vaccination", blank=True)

class Vaccination(models.Model):
    """
        vaccination model that encapsulates data about vaccination given to pets if any
        @author Anim Malvat
    """
    name = models.CharField(max_length=50)

    def __str__(self):
        """
            string representation of the object that will be inserted 
        """
        return self.name

