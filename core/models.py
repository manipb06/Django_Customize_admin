from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

class Person(models.Model):
    first_name = models.TextField()
    last_name = models.TextField()
    courses = models.ManyToManyField("Course", blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} "

    class Meta:
        ordering = ("first_name","last_name" )
        

class Course(models.Model):
    name = models.TextField()
    year = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.name } {self.year}"

        # class Meta:
        #     unique_together = ("name", "year", )

class Grade(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    grade = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(100)])
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    # year = models.ForeignKey(Course, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.grade}, {self.person}, {self.course}"
