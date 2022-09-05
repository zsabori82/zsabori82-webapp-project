#! /bin/python
# Author: zeinabsabori
# Version v1.0
# Description: This program will
"""
    Docstring:
"""
#Schema structure
from app import d
class Booking(d.Model):
    Booking_ID = d.Column(d.Integer,nullable=False,primary_key=True)
    Cost= d.Column(d.Integer,nullable=False)
    Number_ticket = d.Column(d.String(50), nullable=True)
    Start_Date = d.Column(d.Datetime, nullable=True)
    Return_Date = d.Column(d.Datetime, nullable=True)
    


class PersonalDetails(d.Model):
    personal_ID = d.Column(d.Integer,nullable=False,primary_key=True)
    First_name = d.Column(d.String(100),nullable=False)
    Last_name = d.Column(d.String(100), nullable=False)
    Address = d.Column(d.String(300), nullable=False)
    Gender = d.Column(d.String(1), nullable=False)
    Phone_Numb = d.Column(d.String(100), nullable=False)
    Fees = d.Column(d.Integer,nullable=False)
   



