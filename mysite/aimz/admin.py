from django.contrib import admin
from .models import Job, Course, CourseEnrollment, StudentApplication, Contact

# Register your models here.

class CourseEnrollmentAdmin(admin.ModelAdmin):
    list_display = ['display_student', 'display_course', 'display_contact_number', 'enrollment_date']

    def display_student(self, obj):
        return obj.student.user.username if obj.student else ''

    display_student.short_description = 'Student'

    def display_contact_number(self, obj):
        return obj.student.contact_number if obj.student else ''

    display_contact_number.short_description = 'Contact Number'


    def display_course(self, obj):
        return obj.course.title if obj.course else ''

    display_course.short_description = 'Course'


class StudentApplicationAdmin(admin.ModelAdmin):
    list_display = ['display_student', 'display_job', 'display_company', 'application_date']

    def display_student(self, obj):
        return obj.student.user.username if obj.student else ''

    display_student.short_description = 'Student'

    def display_job(self, obj):
        return obj.job_opportunity.title if obj.job_opportunity else ''

    display_job.short_description = 'Job'

    def display_company(self, obj):
        return obj.job_opportunity.company if obj.job_opportunity else ''

    display_company.short_description = 'Company'



class CourseAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'image', 'display_students_enrolled']

    def display_students_enrolled(self, obj):
        return ", ".join([student.user.username for student in obj.students_enrolled.all()])

    display_students_enrolled.short_description = 'Students Enrolled'

    
class JobAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'company', 'req_skills', 'application_deadline', 'get_applicants_count']

    def get_applicants_count(self, obj):
        return obj.job_applications.count()

    get_applicants_count.short_description = 'Applicants Count'


class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'message']


admin.site.register(Course, CourseAdmin)
admin.site.register(Job, JobAdmin)
admin.site.register(CourseEnrollment, CourseEnrollmentAdmin)
admin.site.register(StudentApplication, StudentApplicationAdmin)
admin.site.register(Contact, ContactAdmin)

