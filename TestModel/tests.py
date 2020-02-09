from django.test import TestCase
from TestModel import models
# Create your tests here.

m = models.Main()
print(m.objects.get(id=1))
