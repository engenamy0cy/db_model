from django.db import models

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Color(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Car(models.Model):
    name = models.CharField(max_length=100)
    create_at = models.DateTimeField(auto_now_add=True)
    company = models.ForeignKey(Company, on_delete = models.CASCADE, verbose_name="компания производитель") #изменить
    color = models.ForeignKey(Color, on_delete = models.PROTECT,verbose_name = "цвет", related_name="cars") #изменить, досуп получения обратной связи color.cars.all()
    engine = models.CharField(max_length=100) #choise
    passengers_people = models.PositiveIntegerField() #50/50
    type_engine = models.CharField(max_length=100) #choise
    trunk = models.PositiveIntegerField() #50/50
    type_akp = models.CharField(max_length=10)
    model = models.CharField(max_length=100)
    type_wheel = models.CharField(max_length=100)
    wheels = models.PositiveIntegerField()
    type_complection = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10,decimal_places=2)

