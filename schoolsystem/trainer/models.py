from django.db import models

# Create your models here.
class Trainer(models.Model):
    profile_picture=models.ImageField(upload_to="images/")
    first_name=models.CharField(max_length=15,null=True)
    last_name=models.CharField(max_length=12,null=True)
    contract=models.FileField(upload_to="images/")
    age=models.PositiveSmallIntegerField(null=True)
    Gender_choices=(
        (u'M','Male'),
        (u'F','Female'),
        (u'O','Others'),
    )
    gender=models.CharField(max_length=19, choices =Gender_choices)
    course_Name=models.CharField(max_length=15,null=True)
    email=models.EmailField(blank=True,null=True)
    LANGAUAGE_CHOICES=(
        (u'E','English'),
        (u'k','u''kiswahili'),
        (u'ki','u''kinywaranda'),
    )
    # contract=models.FileField(null=True)
    phone_number=models.CharField(max_length=15,null=True)
    language=models.CharField(max_length=3)
    id=models.CharField(primary_key=True,max_length=18)
    nationality=models.CharField(max_length=12)
    nationality_choices=((u'k',U'Kenyan'),(u'r',U'Rwandan'),(u'u','Ugandan'),(U't','Tanzanian'),(U'a','Algerian'),(U'a','Angolan'),(U'b','Burundian'),(U'b','Burkinabe'),(U'c','Cameroonian'))
    nationality=models.CharField(max_length =23,choices=nationality_choices)
   