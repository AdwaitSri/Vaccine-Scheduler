from django.db import models

class PersonalDetails(models.Model):

    name = models.CharField(max_length=30)
    phone_no = models.BigIntegerField(primary_key=True)
    age = models.IntegerField()
    gender = models.CharField(max_length=30)
    pwd = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'personal_details'
    def __str__(self):
        return (self.phone_no)

class VaccinationDetails(models.Model):
    phone_no = models.BigIntegerField(primary_key=True)
    booking_status = models.CharField(max_length=45, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    time = models.CharField(max_length=45, blank=True, null=True)
    location = models.CharField(max_length=45, blank=True, null=True)
    vaccination_id = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vaccination_details'

    def __str__(self):
        return (self.phone_no)
# Create your models here.
