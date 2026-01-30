from django.contrib import admin
from .models import Student, Unit

admin.site.site_header = 'Student Examination Records'
admin.site.site_title = 'Student Records Portal'
admin.site.index_title = 'Welcome to the Examination Management System'

# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['student_id', 'student_name', 'exam_date', 'student_cats_score', 'student_exam_score', 'student_total_score', 'comment']
    list_filter = ['unit_details', 'exam_date', 'student_chosen_prefix']
    search_fields = ['student_name', 'student_id', 'exam_date']
    
    fieldsets = (
        ('Student Identity', {
            'fields': ('student_chosen_prefix', 'student_id_number', 'student_name', 'unit_details'),
            'description': 'Enter Student details here'
        }), 
        ('Examination Information', {
            'fields': ('exam_date',), 
            'description': 'Enter when the exam was done(MM/YYYY)' 
        }), 
        ('Score Details', {
            'fields': ('student_cats_score', 'student_exam_score'), 
            'description': 'Enter Student scores here' 
        }),
        ('Additional Comments', {
            'fields': ('comment',) 
        }), 
    )
    
    
@admin.register(Unit)
class UnitAdmin(admin.ModelAdmin):
    list_display = ['unit_name', 'unit_code']
    search_fields = ['unit_name', 'unit_code']