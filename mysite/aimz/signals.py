# signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from userauths.models import User
from profs.models import StudentProfile, RelationshipManager

@receiver(post_save, sender=User)
def create_student_profile(sender, instance, created, **kwargs):
    if created and instance.user_type == 'student':
        StudentProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def create_relationship_manager(sender, instance, created, **kwargs):
    if created and instance.user_type == 'relationship_manager':
        RelationshipManager.objects.create(user=instance)