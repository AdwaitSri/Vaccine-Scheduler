from django.db import models

class PersonalDetails(models.Model):
    reg_id = models.AutoField(db_column='Reg_id', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=30)
    phone_no = models.BigIntegerField()
    age = models.IntegerField()
    gender = models.CharField(max_length=1)
    pwd = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Personal_Details'

    def __str__(self):
        return (self.reg_id)

class VaccinationDetails(models.Model):
    reg_id = models.IntegerField(db_column='Reg_id', primary_key=True)  # Field name made lowercase.
    booking_status = models.SmallIntegerField(blank=True, null=True)
    due_date = models.DateField(blank=True, null=True)
    time = models.TimeField(blank=True, null=True)
    location = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Vaccination_Details'

    def __str__(self):
        return (self.reg_id)
# Create your models here.
