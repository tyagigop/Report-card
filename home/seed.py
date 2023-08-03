from faker import Faker
fake = Faker()
from .models import *
import random
from django.db.models import Q, Sum, F
from django.core.mail import send_mail
from django.conf import settings
def seed_db():
    for _ in range(0,100):

        department_all = Department.objects.all()
        random_index = random.randint(0,len(department_all)-1)
        department = department_all[random_index]
        student_id = f'BTS-23{random.randint(0,99999)}RT'
        student_name = fake.name()
        student_email = fake.email()
        student_age = random.randint(18,55)
        student_address = fake.address()

        student_id_ins=StudentId.objects.create(student_id=student_id)
        try:
            # Check if a student with the given email already exists
            student = Student.objects.get(student_email=student_email)
            # If exists, update the student's attributes
            student.department = department
            student.student_id = student_id_ins
            student.student_name = student_name
            student.student_age = student_age
            student.student_address = student_address
            student.save()
        except Student.DoesNotExist:
            # If the student does not exist, create a new student
            student = Student.objects.create(
                department=department,
                student_id=student_id_ins,
                student_name=student_name,
                student_email=student_email,
                student_age=student_age,
                student_address=student_address,
            )




def seed_db2(n=10):
    for i in range(0,10):
        subject_obj = Subject.objects.all()
        student = Student.objects.all()
        student_index = random.randint(0,len(student)-1)
        student = student[student_index]


        for sub in subject_obj:
            subject = sub
            marks = random.randint(33,100)


            SubjectMarks.objects.create(
                marks  = marks,
                subject  = subject,
                student  = student,
                
            )


def seed_db3():
    queryset = Student.objects.all()


    ranks = Student.objects.annotate(marks = Sum('studentmarks__marks')).order_by('-marks')
    current_rank = 1
    i= 1
    for rank in ranks:
        studentCard.objects.create(
            student = rank,
            rank = i
        )
        i+=1


def send_email_to_client():
    subject = "sample"
    message = "sample"
    from_email = settings.EMAIL_HOST_USER
    recipient_list = ["hemantty0208@gmail.com"]
    send_mail(subject, message,from_email, recipient_list)











