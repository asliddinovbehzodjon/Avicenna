from django.db import models
from teacher.models import Teacher
from teacher.models import Subject
from django.utils.translation import gettext_lazy as _
# Create your models here.
class Test(models.Model):
    date = models.DateTimeField(verbose_name=_("Date"))
    teacher = models.ForeignKey(Teacher,on_delete=models.CASCADE,verbose_name=_("Teacher"))
    subject = models.ForeignKey(Subject,on_delete=models.CASCADE,verbose_name=_("Subject"))
    file = models.FileField(upload_to='tests',verbose_name=_("Results file(Excel)"))
    def __str__(self):
        return f"{self.subject} fanidan imtihon"
    class Meta:
        db_table = "Test"
        verbose_name = "Test"
        verbose_name_plural = 'Test'
class BotUsers(models.Model):
    telegram = models.CharField(max_length=500)
    fullname = models.CharField(max_length=500,null=True,blank=True)
    def __str__(self):
        return self.fullname