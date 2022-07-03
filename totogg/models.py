from django.db import models

# Create your models here.
class LCK_Data(models.Model):
  match_num = models.CharField(max_length=20)
  team = models.CharField(max_length=50)
  rst = models.CharField(max_length=20)
  side =  models.CharField(max_length=20)
  gtime = models.CharField(max_length=50)
  gold = models.IntegerField()
  tot_dam = models.IntegerField()
  kill = models.IntegerField()
  death = models.IntegerField()
  assist = models.IntegerField()
  tower = models.IntegerField()
  inhibitor = models.IntegerField()
  herald = models.IntegerField()
  dragon = models.IntegerField()
  elder = models.IntegerField()
  baron = models.IntegerField()
  sight = models.IntegerField()
  total_cs = models.IntegerField()

  def __str__(self):
    return f'{self.team}--{self.rst}'