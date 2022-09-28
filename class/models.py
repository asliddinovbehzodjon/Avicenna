from django.db import models
from django.utils.translation import gettext_lazy as _
from students.models import Student
# Create your models here.
class Tuitor(models.Model):
    name = models.CharField(max_length=100,verbose_name=_("Name"),
                            help_text=_("Enter name"))
    phone = models.CharField(max_length=900,verbose_name=_("Phone number"),help_text=_("Enter phone number"))
    about = models.TextField(verbose_name=_("About tuitor"),help_text=_("Enter about tuitor"))
    def __str__(self):
        return self.name
    class Meta:
        db_table = 'Tuitor'
        verbose_name= _("Tuitor ")
        verbose_name_plural = _("Tuitors ")
class ClassRoom(models.Model):
    name = models.CharField(max_length=100,verbose_name=_("Class name"),help_text=_("Enter class name"))
    student = models.ManyToManyField(Student)
    tuitor = models.ForeignKey(Tuitor,on_delete=models.CASCADE)
    lesson_time = models.TextField(verbose_name=_("Lesson time"),help_text=_("Enter lesson time"))
    def __str__(self):
        return f"{self.name} sinfi"
    class Meta:
        db_table = 'ClassRoom'
        verbose_name= _("Classroom ")
        verbose_name_plural = _("Classroom ")
