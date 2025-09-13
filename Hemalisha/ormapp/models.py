from django.db import models
from django.contrib import admin
class Cars_DB(models.Model):
	car_name=models.CharField(max_length=20)
	reg_no=models.IntegerField(primary_key=True)
	fuel_type=models.CharField()
	engine_model=models.CharField()
	insurence_no=models.IntegerField()
class Cars_DBAdmin(admin.ModelAdmin):
	list_display=["car_name", "reg_no", "fuel_type", "engine_model", "insurence_no"]
