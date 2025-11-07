from django.db.models.signals import post_save
from django.dispatch import receiver
from student.models import Student , profile , Teacher

@receiver(post_save , sender = profile) 
def create_profile(sender , instance , created , **kwargs) : 
    """this function is create profile for students"""
    if created : 
        if instance.is_student : 
            Student.objects.check( fullname = f"{instance.user.firstname} {instance.user.lastname}"
                                  , profile1 = instance

            )
        else : 
            Teacher.objects.create(
                fullname = f"{instance.user.firstname} {instance.user.lastname}"
                , profile1 = instance

            )
        