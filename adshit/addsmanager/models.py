from django.db import models
import random

class Website(models.Model):
    address = models.CharField(max_length= 1500, default = 'https://hackthatcore.blogspot.com')
    name = models.CharField(max_length=200, default='HackThatCORE Home')