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
    name = models.CharField(max_length=100,null=True)
    create_at = models.DateTimeField(auto_now_add=True,null=True)
    company = models.ForeignKey(Company,on_delete=models.CASCADE,verbose_name="компания производитель",null=True) #изменить
    color = models.ForeignKey(Color,on_delete=models.PROTECT,verbose_name="цвет",related_name="cars",null=True)  #доступ получения обратной связи color.cars.all()
    engine = models.CharField(max_length=100,null=True) #choise/
    passengers_people = models.PositiveIntegerField(null=True) #50/50
    type_engine = models.CharField(max_length=100,null=True) #choise/
    trunk = models.PositiveIntegerField(null=True) #50/50
    type_akp = models.CharField(max_length=10,null=True) #choise
    model = models.CharField(max_length=100,null=True)  #изменить
    type_wheel = models.CharField(max_length=10,null=True) #choise
    wheels = models.PositiveIntegerField(null=True)  #choise/
    type_complection = models.CharField(null=True) #choise
    price = models.DecimalField(max_digits=10,decimal_places=2,null=True)

