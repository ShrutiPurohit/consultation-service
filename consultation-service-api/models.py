from django.db import models
from django.db.models.fields import IntegerField

class Caselist(models.Model):
	
	caseid = models.AutoField(primary_key=True)
	patientid = models.CharField(max_length=256, blank=True)
	patientname = models.CharField(max_length=256, blank=False, default=" ")
	symptoms = models.CharField(max_length=512, blank=False)
	mobile_no = models.CharField(max_length=10,)
	date_created = models.DateTimeField(auto_now_add=True)
	groupname = models.CharField(max_length=256, blank=False,default = " ")
	diagnosis = models.CharField(max_length=512, blank=True)

	def __str__(self):
		"""Return a human readable representation of the model instance."""
		return "{}".format(self.caseid)
