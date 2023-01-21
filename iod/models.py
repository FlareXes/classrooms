from django.contrib.auth.models import User
from django.db import models


class Room(models.Model):
    id = models.AutoField(primary_key=True)
    classroom = models.CharField(max_length=30)
    student = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    booked = models.BooleanField(default=False)
    capacity = models.IntegerField(null=True, blank=True, default=10)

    def __str__(self):
        return "iod_" + self.classroom
