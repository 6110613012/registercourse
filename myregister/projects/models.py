from django.db import models
from django.core.validators import MaxValueValidator,MinValueValidator
from django.contrib.auth.models import User

class Course(models.Model):
    cID = models.CharField(max_length = 5, primary_key = True)
    cName = models.CharField(max_length = 50)
    term = models.IntegerField()
    year = models.IntegerField()
    quota = models.IntegerField()
    enroll = models.ManyToManyField(User)
    status = models.BooleanField()

    def count(self):
        return len(self.enroll.all())

    def __str__(self):
        return f"{self.cID} {self.cName} {self.term}/{self.year} {self.enroll.count()}/{self.quota} {self.status}"