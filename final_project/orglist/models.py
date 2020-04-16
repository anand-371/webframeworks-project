from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
class lostfound(models.Model):
	item_number=models.IntegerField(default=1)
	weight=models.IntegerField(default=1)
	insurance_amount=models.IntegerField(default=1)
	destination=models.CharField(max_length=15,default="")
	delivery_date=models.DateTimeField(default=timezone.now)
	finder=models.ForeignKey(User,on_delete=models.CASCADE)
	status=models.BooleanField(default=False) 
	file= models.FileField(default='default.jpg')
	#likes=models.ManyToManyField(User,blank=True,related_name="likes",null=True)
	
	def __str__(self):
		return str(self.item_number)

	def get_absolute_url(self):
		return reverse('post-detail', kwargs={'pk':self.pk})