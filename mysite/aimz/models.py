from django.db import models
from django.utils.html import mark_safe
from userauths.models import User
from profs.models import StudentProfile

RATING = (
    (1, "★☆☆☆☆"),
    (2, "★★☆☆☆"),
    (3, "★★★☆☆"),
    (4, "★★★★☆"),
    (5, "★★★★★")
)


class Course(models.Model):
    title = models.CharField(max_length=225)
    description = models.TextField()
    image = models.ImageField(upload_to="course")
    students_enrolled = models.ManyToManyField(StudentProfile, through='CourseEnrollment')
    
    class Meta:
        verbose_name_plural="Courses"

    def course_image(self):
        return mark_safe('<img src="%s" width="50" height="50"/>' % (self.image.url))
    
    def __str__(self):
        return self.title

class CourseEnrollment(models.Model):
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE)
    contact_number = models.CharField(max_length=15, default=0000000)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    enrollment_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural="Enrollments"

    def __str__(self):
        return f"{self.student.user.username} enrolled in {self.course.title}"
    
class Job(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    company = models.CharField(max_length=255)
    req_skills = models.TextField()
    application_deadline = models.DateField()
    applicants = models.ManyToManyField(StudentProfile, through='StudentApplication')


    class Meta:
        verbose_name_plural="Jobs"

    def __str__(self):
        return self.title
    
class StudentApplication(models.Model):
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE)
    job_opportunity = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='job_applications')
    company = models.CharField(max_length = 255, default='abcd')
    application_date = models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name_plural="Applications"

    def __str__(self):
        return f"{self.student.user.username} applied for {self.job_opportunity.title}"
    
class Contact(models.Model):
    name = models.CharField(max_length = 255)
    email = models.EmailField()
    subject = models.CharField(max_length = 255)
    message = models.TextField()

    class Meta:
        verbose_name_plural="Contact Us"

    def __str__(self):
        return self.subject