from django.db import models

class Section(models.Model):
    name = models.CharField(max_length=50, unique=True)
    curved = models.BooleanField(default=False)
    balcony = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Rank(models.Model):
    name = models.CharField(max_length=50, unique=True)
    rank = models.PositiveIntegerField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} - rank: {self.rank}"


class Seat(models.Model):
    number = models.PositiveIntegerField(unique=True, primary_key=True)
    section = models.ForeignKey(Section, on_delete=models.SET_NULL, null=True, default=None)
    row = models.PositiveIntegerField()
    rank = models.ForeignKey(Rank, on_delete=models.SET_NULL, null=True, default=None)
    user = models.PositiveIntegerField(null=True, default=None)
    blocked = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def is_aisle(self):
        return str(self.number)[-1] == '1' or str(self.number)[-1] == '0'

    def is_front(self):
        return self.row == 1
    
    def is_balcony(self):
        return self.section.balcony

    def is_available(self):
        return self.user == None

    def __str__(self):
        return f"{self.row} - seat: {self.number}"