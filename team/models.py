from django.db import models

# Create your models here.
class opggData(models.Model):
  teamName = models.CharField(max_length=50, null=True, default='')
  playerName = models.CharField(max_length=50, null=True, default='')
  rst = models.CharField(max_length=20)
  champ_img = models.CharField(max_length=200, null=True, default='')
  champ = models.CharField(max_length=50)
  kda = models.CharField(max_length=100)
  score = models.CharField(max_length=100)
  ka = models.CharField(max_length=100)
  cs = models.CharField(max_length=100)
  g_time = models.CharField(max_length=100)
  
  def __str__(self):
    return f'{self.teamName}-{self.playerName}-{self.champ}--{self.rst}'