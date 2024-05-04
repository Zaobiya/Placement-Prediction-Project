from django.db import models
from userauths.models import User
from django.utils.html import mark_safe
# from aimz.models import Job, StudentFeedback, Course

# Create your models here.
def user_directory_path(instance, filename):
    return 'user_{0}/{1}'.format(instance.user.id, filename)

class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    roll_number = models.CharField(max_length=20, unique=True)
    contact_number = models.CharField(max_length=15)
    image = models.ImageField(upload_to=user_directory_path)
    skills = models.TextField(default='abc...')
    #courses_enrolled = models.ManyToManyField(Course, through='CourseEnrollment')
    #job_applications = models.ManyToManyField(Job, through='StudentApplication')
    #feedback_received = models.ManyToManyField(StudentFeedback )

    class Meta:
        verbose_name_plural="Students"

    def student_image(self):
        return mark_safe('<img src="%s" width="50" height="50"/>' % (self.image.url))
    

    def __str__(self):
        return self.user.username
    

class RelationshipManager(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    contact_number = models.CharField(max_length=15)
    email = models.EmailField(max_length=200)
    assigned_students = models.ManyToManyField(StudentProfile, related_name='assigned_relationship_managers')
    
    class Meta:
        verbose_name_plural="Relationship  Managers"

    def __str__(self):
        return self.user.username
    
    def save(self, *args, **kwargs):
        self.email = self.user.email
        super().save(*args, **kwargs)

class AdminProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=200)
    contact_number = models.CharField(max_length=15)


    def __str__(self):
        return self.user.username
    