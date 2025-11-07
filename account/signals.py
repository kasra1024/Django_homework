from django.db.models.signals import post_save
from django.dispatch import receiver
from student.models import profile
from django.contrib.auth.models import User

@receiver(post_save , sender = User) 
def create_profile(sender , instance , created , **kwargs) : 
    """this function is create profile for users"""
    if created : 
        profile.objects.create(
            bio = f"{instance.firstname} bio" , student=instance
        )