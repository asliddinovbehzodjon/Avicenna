from django.db import models
from django.utils.translation import  gettext_lazy as _
# Create your models here.
class Subject(models.Model):
    name = models.CharField(max_length=100,verbose_name=_("Subject"),help_text=_("Enter subject name"))
    def __str__(self):
        return self.name
    class Meta:
        db_table = "Subject"
        verbose_name = _("Subject ")
        verbose_name_plural= _("Subjects ")
class Teacher(models.Model):
    name = models.CharField(max_length=100,verbose_name=_("Name"),help_text=_("Enter teacher name"))
    subject = models.ForeignKey(Subject,on_delete=models.CASCADE)
    one_id = models.IntegerField(null=True, blank=True)
    phone = models.CharField(max_length=900, verbose_name=_("Phone number"), help_text=_("Enter phone number"))
    # salary = models.CharField(max_length=600,verbose_name=_("Salary"))
    def __str__(self):
        return self.name
    def save(self, *args, **kwargs):
        if self.id:
            self.one_id = self.id +1000
        super(Teacher, self).save(*args, **kwargs)
    class Meta:
        db_table = "Teacher"
        verbose_name = _("Teacher ")
        verbose_name_plural = _("Teachers ")
