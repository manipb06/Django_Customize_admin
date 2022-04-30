from dataclasses import field
from pyexpat import model
from django.contrib import admin
from django import forms
# Register your models here.

from core.models import Person, Course, Grade

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ( "first_name", "last_name")
    search_fields = ("last_name__startswith","first_name__startswith" )       # this is for serach bar in django admin panel
    # fields = ("first_name", "last_name", "courses") # this is for how models are edited
    # form = PersonAdminForm
    

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ( "name", "year",)
    list_filter = ("year", )
    pass

@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    # list_display = ( "Course")
    pass

class PersonAdminForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = "__all__"

    



    