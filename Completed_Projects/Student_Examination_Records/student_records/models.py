from django.db import models
from datetime import datetime
from django.utils import timezone

# Create your models here.
class Unit(models.Model):
    unit_name = models.CharField(max_length=255)
    unit_code = models.CharField(max_length=255, primary_key=True)
    
    def __str__(self):
        return f"Unit Name: {self.unit_name}\nUnit Code: {self.unit_code}."


class Student(models.Model):
    unit_details = models.ForeignKey(Unit, on_delete=models.CASCADE)
    
    STUDENT_ID_PREFIXES = [
            ('CIS3/', 'CIS3/') , 
            ('CIS38/', 'CIS38/'),
    ]
    student_chosen_prefix = models.CharField(max_length=255, choices=STUDENT_ID_PREFIXES)
    student_id_number = models.CharField(max_length=255)
    student_id = models.CharField(max_length=50, primary_key=True, editable=False)
    def get_student_id(self):
        self.student_id = f"{self.student_chosen_prefix}{self.student_id_number}"
    
    student_name = models.CharField(max_length=255)
    
    exam_date = models.DateField()
    def get_exam_date(self):
        self.exam_date.strftime('%m/%Y')
    
    student_cats_score = models.FloatField()
    student_exam_score = models.FloatField()
    
    student_total_score = models.FloatField(editable = False, null=True, blank=True)
    def get_scores(self):
        self.student_total_score = self.student_cats_score + self.student_exam_score
        
    comment = models.CharField(max_length=255, default='No Comment')
    
    def save(self, *args, **kwargs):
        self.get_student_id()
        self.get_exam_date()
        self.get_scores()
        
        super().save(*args, **kwargs)
        
    def __str__(self):
        return f"Student Name: {self.student_name}\nStudent ID: {self.student_id}\n   Unit Details: {self.unit_details}."

        
        
    
    