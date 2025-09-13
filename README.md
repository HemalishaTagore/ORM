# Ex02 Django ORM Web Application
## Date:13-09-2025

## AIM
To develop a Django application to store and retrieve data from a Car Inventory Database using Object Relational Mapping(ORM).





## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 books

## PROGRAM
```
models.py
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
admin.py
from django.contrib import admin
from .models import Cars_DB, Cars_DBAdmin
admin.site.register(Cars_DB, Cars_DBAdmin)
```


## OUTPUT
![alt text](<Screenshot (14).png>)



## RESULT
Thus the program for creating car inventory database database using ORM hass been executed successfully
