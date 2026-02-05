from django.db import models

class RAM(models.Model):
    name = models.CharField(max_length=100)
    size = models.PositiveIntegerField()
    RAM = [
        ("DDR2", "ДДР2"),
        ("DDR3","ДДР3"),
        ("DDR4","ДДР4"),
    ]
    status_ram = models.CharField(max_length=20, choices=RAM, default="DDR2")
    def __str__(self):
        return self.name

class CPU(models.Model):
    name = models.CharField(max_length = 100)
    cores = models.PositiveIntegerField()
    CPU = [
        ("Intel", "Intel"),
        ("AMD","AMD"),
        ("Ryzen","Рузен")
    ]
    status_cpu = models.CharField(max_length=20, choices=CPU, default="Intel")
    def __str__(self):
        return self.name

class Manufacturer(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    
class GPU(models.Model):
    name = models.CharField(max_length = 100)
    memory = models.PositiveIntegerField()
    def __str__(self):
        return self.name

class PC(models.Model):
    name = models.CharField(max_length=100)
    cpu = models.ForeignKey(CPU, on_delete = models.CASCADE,verbose_name="проц",related_name="Cpu")
    gpu = models.ForeignKey(GPU, on_delete= models.CASCADE,verbose_name="видюха",related_name="Gpu")
    ram = models.ForeignKey(RAM, on_delete=models.CASCADE,verbose_name="оперативка",related_name="Ram")
    manufacturer = models.ForeignKey(Manufacturer, on_delete = models.CASCADE,verbose_name="производитель",related_name="Manufacturer")
    price = models.DecimalField(max_digits=10,decimal_places=2)