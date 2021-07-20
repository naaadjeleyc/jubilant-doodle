"""
This file will populate the tables using Faker
"""
import random
import decimal
from datetime import datetime
from django.db import models
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand, CommandError
from faker import Faker

from TechSup.models import  Customer, Order, Product

class Command(BaseCommand):
    help = 'Load data into the tables'

    def handle(self,*args,**options):
        Order.objects.all().delete()
        Product.objects.all().delete()
        Customer.objects.all().delete()
        User.objects.all().delete()
        print("tables dropped successfully")

        fake = Faker()

        for i in range(10):
            first_name = fake.first_name(),
            last_name = fake.last_name(),
            username = first_name + last_name,
            user=User.objects.create_user(
            username=username,
            first_name=first_name,
            last_name=last_name,
            email = fake.ascii_free_email(),
            password ='p@ssw0rd'
            )
            customer = Customer.objects.get(user = user)
            customer.address = fake.address(),
            customer.save()

        for i in range(10):
            product = Product.objects.create(
            name = fake.catch_phrase(),
            price = int( decimal.Decimal(random.randrange(155,899))/100),
            )
            product.save()  

        customers = Customer.objects.all()
        for customer in customers:  
            for i in range(3):
                order = Order.objects.create(
                customer = customer,
                )
                order.save()   


        print("tables successfully loaded")        
