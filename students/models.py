from tabnanny import verbose
from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.
from django.utils.html import format_html
viloyat = (
    ("Andijon","Andijon"),
    ("Buxoro","Buxoro"),
    ("Farg'ona","Farg'ona"),
    ("Jizzax","Jizzax"),
    ("Namangan","Namangan"),
    ("Navoiy","Navoiy"),
    ("Qashqadaryo","Qashqadaryo"),
    ("Qoraqalpog'iston","Qoraqalpog'iston"),
    ("Samarqand","Samarqand"),
    ("Sirdaryo","Sirdaryo"),
    ("Surxondaryo","Surxondaryo"),
    ("Xorazm","Xorazm"),
    ("Toshkent","Toshkent")
    
)
class Parent(models.Model):
    name = models.CharField(max_length=1000,verbose_name=_("Name"),
                            help_text=_("Enter name"))
    region = models.CharField(max_length=6000,verbose_name=_("Region"), help_text=_("Choose region"),default="qashqadaryo",choices=viloyat)
    address = models.CharField(max_length=9000,verbose_name=_("Address"),help_text=_("Enter address"))
    phone = models.CharField(max_length=900,verbose_name=_("Phone number"),help_text=_("Enter phone number"))
    def __str__(self):
        return self.name
    class Meta:
        db_table = "Parent"
        verbose_name = _("Parent ")
        verbose_name_plural = _("Parents ")
    
class Student(models.Model):
    name = models.CharField(max_length=1000,verbose_name=_("Name"),
                            help_text=_("Enter name"))
    parent = models.ForeignKey(Parent,on_delete=models.CASCADE)
    address = models.CharField(max_length=9000,verbose_name=_("Address"),help_text=_("Enter address"))
    image = models.ImageField(upload_to="student-image",verbose_name=_("Image"),help_text=_("Upload image"))
    phone =  models.CharField(max_length=900,verbose_name=_("Phone number"),help_text=_("Enter phone number"))
    one_id = models.IntegerField(null=True,blank=True)
    def __str__(self):
        return self.name
    @property
    def image_show(self):
        return format_html('<img src = {} width="60" height="60" style="border-radius:50%;"'.format(self.image.url))
    def save(self, *args, **kwargs):
        if self.id:
            self.one_id = self.id +1000
        super(Student, self).save(*args, **kwargs)
    class Meta:
        db_table = "Student"
        verbose_name = _("Student ")
        verbose_name_plural = _("Students ")