from django.db import models


# Create your models here.
class LCK_Data(models.Model):
  match_num = models.CharField(max_length=20)
  set = models.IntegerField(null=True, default=0)
  team = models.CharField(max_length=50)
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
  rst = models.CharField(max_length=20)

  def __str__(self):
    return f'{self.team}--{self.rst}'

class Summer_Data(models.Model):
  match_num = models.CharField(max_length=20)
  set = models.IntegerField(null=True, default=0)
  team = models.CharField(max_length=50)
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
  rst = models.CharField(max_length=20)

  def __str__(self):
    return f'{self.team}--{self.rst}'


class rank(models.Model):
  team = models.CharField(max_length=50)
  team_logo = models.CharField(max_length=200, null=True, default='')
  score_n = models.CharField(max_length=50)
  score_wins = models.CharField(max_length=50)
  score_loses = models.CharField(max_length=50)
  score_scd = models.CharField(max_length=50)
  score_wins_rates = models.CharField(max_length=50)

  def __str__(self):
    return self.team


class summerSummary(models.Model):
  tname = models.CharField(max_length=20, primary_key=True)
  rate = models.FloatField()
  kill = models.FloatField()
  gold = models.IntegerField()
  baron = models.FloatField()
  dragon = models.FloatField()
  tower = models.FloatField()
  
  def __str__(self):
    return f'{self.tname}-{self.rate}'

class recentSummary(models.Model):
  tname = models.CharField(max_length=20, primary_key=True)
  gold = models.FloatField()
  tot_dam = models.FloatField()
  kill = models.FloatField()
  tower = models.FloatField()
  inhibitor = models.FloatField()
  dragon = models.FloatField()
  baron = models.FloatField()
  total_cs = models.FloatField()

  def get_gold(self):
    return self.gold

  def __str__(self):
    return f'{self.tname} data saved!'
  
class gameSchedule(models.Model):
  date = models.DateField()
  time = models.CharField(max_length=50)
  team1 = models.CharField(max_length=20)
  team2 = models.CharField(max_length=20)
  set = models.IntegerField(null=True)