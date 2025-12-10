from django.core.management.base import BaseCommand
from student.models import Student

from time import sleep

class Command (BaseCommand) : 
    def add_arguments(self, parser):
        parser.add_argument("student_id" , type=int)


    def handle(self, *args, **options):
        print (options["student_id"])
        self.stdout.write(self.style.WARNING(options["student_id"]))
        print ("---------------------------")
