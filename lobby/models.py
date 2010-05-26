from django.db import models
from djangosphinx import SphinxSearch


class Lobbytype(models.Model):
    actcd = models.CharField(max_length=100, primary_key=True)
    name = models.CharField(max_length=50, blank=True)
    slug = models.CharField(max_length=50, blank=True)
    class Meta:
        db_table = u'lobbytype'
        
    def __unicode__(self):
        return "%s%s%s"%(self.name,self.actcd,self.slug)

    def get_absolute_url(self):
        return '/lobby/lobbytype/%s/'% self.slug

        

class Country(models.Model):
    country_cd = models.CharField(max_length=2, primary_key=True)
    country = models.CharField(max_length=80, blank=True)
    slug = models.CharField(max_length=80, blank=True)
    class Meta:
        db_table = u'lbcountry'

    def __unicode__(self):
        return "%s%s%s"%(self.country,self.country_cd,self.slug)

    def get_absolute_url(self):
        return '/lobby/country/%s/' % self.slug


class Clients(models.Model):
    fp_cd = models.CharField(max_length=10, primary_key=True)
    name = models.CharField(max_length=200, blank=True)
    slug = models.CharField(max_length=200, blank=True)
    foreign_cntry_represented = models.ForeignKey(Country, max_length=2, db_column ='foreign_cntry_represented',  blank=True)
    class Meta:
        db_table = u'clients'

    def __unicode__(self):
        return "%s%s%s"%(self.name,self.fp_cd,self.slug)

    def get_absolute_url(self):
        return '/lobby/client/%s/'% self.slug

        
   

        
class Lobbyist(models.Model):
    reg_cd = models.CharField(max_length=10,primary_key=True )
    name = models.CharField(max_length=100, blank=True)
    slug = models.CharField(max_length=100, blank=True)
    class Meta:
        db_table = u'lobbyist'
        ordering = ['name']

    def __unicode__(self):
        return "%s%s%s"%(self.name,self.reg_cd,self.slug)

    def get_absolute_url(self):
        return '/lobby/firms/%s/' % self.slug




class Activity(models.Model):
    activity_cd = models.CharField(max_length=10, primary_key=True)
    fp_cd = models.ForeignKey(Clients, max_length=10, db_column='FP_CD', blank=True)
    reg_cd = models.ForeignKey(Lobbyist, max_length=10, db_column='REG_CD', blank=True)
    supp_cd = models.CharField(max_length=10, db_column='SUPP_CD', blank=True)
    period_start_date = models.DateTimeField(null=True, blank=True)
    period_end_date = models.DateTimeField(null=True, blank=True)
    act_type = models.CharField(max_length=100, db_column='act_type', blank=True)
    actcd = models.ForeignKey(Lobbytype,max_length=100, db_column='actcd', blank=True)
    activity_desc = models.TextField(blank=True)
    financial_amount = models.FloatField(null=True, blank=True)
    financial_desc = models.TextField(blank=True)
    country = models.ForeignKey(Country,max_length=10, db_column='country', blank=True)
    year = models.CharField(max_length=5, blank=True)
    
    class Meta:
        db_table = u'activity'
        ordering = ['-year']

    def __unicode__(self):
        return  "%s%s%s%s%s%s%s"%(self.year,self.activity_cd,self.supp_cd,self.country,self.financial_desc,self.activity_desc,self.act_type)
        
    search = SphinxSearch(
           index ='activity', 
           weights = { # individual field weighting
               'title': 100,
               'activity_desc': 80,
               'country': 70,
               'fp_cd': 50,
              
           }
)
        


