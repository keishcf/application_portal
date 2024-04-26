from django.db import models
from django.contrib.auth.models import User
from uuid import uuid4

class UserApplication(models.Model):
    id = models.UUIDField(primary_key="True", default=uuid4, editable=False,)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    # Application Timeframe
    submitted_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    is_draft = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user.username} Application'
    
    class Meta:
        ordering = ['-submitted_at']

class ApplicantPersonalInformation(models.Model):
    application = models.OneToOneField(UserApplication, on_delete=models.CASCADE, related_name="personal_information")
    first_name = models.CharField(verbose_name="Your first name", max_length=100, help_text="First name on national ID")
    last_name = models.CharField(verbose_name="Your last name", max_length=100, help_text="Last name on national ID")
    bio = models.TextField(verbose_name="Tell us about yourself", help_text="Tell us about yourself in a few words")
    date_of_birth = models.DateField(blank=True, null=True)
    phone_number = models.CharField(verbose_name="Your phone number", max_length=20, blank=True)
    address = models.CharField(verbose_name="Your Address", max_length=255, blank=True)
    # Add other personal information fields as needed
    
    
    def __str__(self) -> str:
        return f"{self.user.username} Personal Information"

class ApplicantAcademicBackground(models.Model):
    DEGREE_CHOICES = [
        ('Bachelor', 'Bachelor'),
        ('Master', 'Master'),
        ('PhD', 'PhD'),
        ('Associate', 'Associate'),
        ('Diploma', 'Diploma'),
        ('Certificate', 'Certificate'),
        ('Other', 'Other'),
    ]
    application = models.OneToOneField(UserApplication, on_delete=models.CASCADE, related_name="academic_background")
    institution_name = models.CharField(verbose_name="Institution name you attended",max_length=200, help_text="It can be anything like university or others")
    degree = models.CharField(verbose_name="Your Degrees",max_length=100, help_text="Degrees your are qualified with like diplomas or others", choices=DEGREE_CHOICES)
    field_of_study = models.CharField(verbose_name="What is your field of study ?", max_length=100, help_text="It can be like computer science or others")
    graduation_year = models.DateField(verbose_name="What year did you graduate", help_text=" Year you graduated from your institution")
    start_year = models.IntegerField(verbose_name="When did you start your institution year ?", help_text=" Year you started your institution")
    end_year = models.IntegerField(verbose_name="When Did You Finish Your Institution Year ?", help_text=" Year you finished your institution")
    
    def __str__(self) -> str:
        return f"{self.user.username} Academic Background"
    

class ApplicantExtracurricularActivity(models.Model):
    application = models.ForeignKey(UserApplication, on_delete=models.CASCADE, related_name="extracurricular_activity")
    activity_name = models.CharField(max_length=255)
    start_year = models.IntegerField(verbose_name="What Year did you start your extracurricular activity", help_text=" Year you started your extracurricular activity")
    end_year = models.IntegerField(verbose_name="What Year Did You Finish Your extracurricular activity", help_text=" Year you finished your extracurricular activity")
    # Add other extracurricular activity fields as needed

class ApplicantDocument(models.Model):
    application = models.OneToOneField(UserApplication, on_delete=models.CASCADE, related_name="documents")
    cv = models.FileField(upload_to='documents/', blank=True, null=True, help_text="Your CV in PDF format")
    transcript = models.FileField(upload_to='documents/', blank=True, null=True, help_text="Your transcript in PDF format")
    # Add other document fields as needed
