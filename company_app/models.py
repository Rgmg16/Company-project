from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=100)
    manager_id = models.ForeignKey('Employee', null=True, blank=True, on_delete=models.SET_NULL, related_name='managed_departments')

    def __str__(self):
        return self.name

class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='employees')
    job_title = models.CharField(max_length=100, null=True, blank=True)  # Added job title field

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.name



