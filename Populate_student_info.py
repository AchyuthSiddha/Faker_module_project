import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','Faker_module_project.settings')
import django

django.setup()

from app.models import Student

from faker import Faker

from random import *

faker=Faker()

def Phone_number():
    d1=randint(6,9)
    num=''+str(d1)
    for i in range(9):
        num+=str(randint(1,9))
    return num

def Populate(n):
    for i in range(n):
        fno=faker.random_int(min=1,max=9999)
        fname=faker.name()
        fdob=faker.date()
        fmarks=faker.random_int(min=1,max=100)
        fphone=Phone_number()
        faddr=faker.address()
        femail=faker.email()
        Student.objects.get_or_create(sno=fno,sname=fname,sdob=fdob,smarks=fmarks,sphone=fphone,saddr=faddr,semail=femail)


n=int(input("enter a number of records:"))
Populate(n)
print(f'{n}record are successfully inserted....!')
    
