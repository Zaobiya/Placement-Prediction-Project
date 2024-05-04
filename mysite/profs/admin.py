from django.contrib import admin
from profs.models import RelationshipManager, AdminProfile, StudentProfile
from aimz.models import CourseEnrollment
# Register your models here.

class StudentProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'image', 'roll_number', 'contact_number', 'skills']


# class RelationshipManagerAdmin(admin.ModelAdmin):
#     list_display = ['user', 'contact_number', 'email', 'display_assigned_students']

#     def display_assigned_students(self, obj):
#         return ", ".join([student.user.username for student in obj.assigned_students.all()])

#     display_assigned_students.short_description = 'Assigned student'

class AdminProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'email', 'contact_number']


class CourseEnrollmentInline(admin.TabularInline):
    model = CourseEnrollment
    extra = 0 

    readonly_fields = ['student', 'enrollment_date']

    def has_add_permission(self, request, obj=None):
        return False  # Disable the ability to add new enrollments from this inline



admin.site.register(StudentProfile, StudentProfileAdmin)
# admin.site.register(RelationshipManager, RelationshipManagerAdmin)
admin.site.register(AdminProfile, AdminProfileAdmin)