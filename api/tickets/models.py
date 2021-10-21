from django.db import models
from django.contrib.auth import get_user_model


class Section(models.Model):
    name = models.CharField(max_length=50, unique=True)
    curved = models.BooleanField(default=False)
    balcony = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Row(models.Model):
    row = models.IntegerField()
    section = models.ForeignKey(Section, on_delete=models.SET_NULL, null=True, default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.section} - row: {self.row}"


class Rank(models.Model):
    name = models.CharField(max_length=50, unique=True)
    rank = models.IntegerField(unique=True)
    cost = models.IntegerField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} - rank: {self.rank}"


class Seat(models.Model):
    number = models.IntegerField(unique=True, primary_key=True)
    section = models.ForeignKey(Section, on_delete=models.SET_NULL, null=True, default=None)
    row = models.ForeignKey(Row, on_delete=models.SET_NULL, null=True, default=None)
    rank = models.ForeignKey(Rank, on_delete=models.SET_NULL, null=True, default=None)
    user = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True, default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def is_aisle(self):
        return str(self.number)[-1] == '0' or str(self.number)[-1] == '9'

    def is_front(self):
        return self.row.row == 1
    
    def is_balcony(self):
        return self.section.balcony

    def is_available(self):
        return self.user == None

    def __str__(self):
        return f"{self.row} - seat: {self.number}"