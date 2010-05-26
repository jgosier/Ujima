# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.

from django.db import models
from djangosphinx import SphinxSearch



class Country(models.Model):
    countrycd = models.CharField(max_length=15, primary_key=True, db_column='CountryCD') # Field name made lowercase.
    country = models.CharField(max_length=150, db_column='Country', blank=True) # Field name made lowercase.
    slug = models.CharField(max_length=240, db_column='Slug', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'gfcountry'

    def __unicode__(self):
        return self.country

    def get_absolute_url(self):
        return '/globalfund/country/%s/'% self.slug
        
    

class Disease(models.Model):
    gadisease = models.CharField(max_length=90, primary_key=True, db_column='GADisease') # Field name made lowercase.
    slug = models.CharField(max_length=75, db_column='Slug', blank=True) # Field name made lowercase.
    disease = models.CharField(max_length=90, blank=True)
    class Meta:
        db_table = u'disease'

    def __unicode__(self):
        return self.disease

    def get_absolute_url(self):
        return '/globalfund/disease/%s/'% self.slug
    

        

class Orgs(models.Model):
    orgcd = models.CharField(max_length=15, primary_key=True, db_column='OrgCD') # Field name made lowercase.
    orgname = models.CharField(max_length=765, db_column='Orgname', blank=True) # Field name made lowercase.
    slug = models.CharField(max_length=765, db_column='Slug', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'orgs'

    def __unicode__(self):
        return "%s" %self.orgname
    
    def get_absolute_url(self):
        return '/globalfund/orgs/%s/'% self.slug
    

class Orgtype(models.Model):
    prtype = models.CharField(max_length=60, primary_key=True, db_column='PRType') # Field name made lowercase.
    orgtype = models.CharField(max_length=150, db_column='OrgType', blank=True) # Field name made lowercase.
    slug = models.CharField(max_length=210, db_column='Slug', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'orgtype'

    def __unicode__(self):
        return self.orgtype

    def get_absolute_url(self):
        return '/globalfund/orgtype/%s/'% self.slug


class Region(models.Model):
    regioncd = models.CharField(max_length=15, primary_key=True, db_column='RegionCD') # Field name made lowercase.
    region = models.CharField(max_length=150, db_column='Region', blank=True) # Field name made lowercase.
    slug = models.CharField(max_length=240, db_column='Slug', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'region'

    def __unicode__(self):
        return self.region

    def get_absolute_url(self):
        return '/globalfund/region/%s/'% self.slug




class Fund(models.Model):
    gdcd = models.CharField(max_length=30, primary_key =True,db_column='GDCD') # Field name made lowercase.
    regioncd = models.ForeignKey(Region,max_length=30, db_column='RegionCD', blank=True) # Field name made lowercase.
    round = models.FloatField(null=True, db_column='Round', blank=True) # Field name made lowercase.
    org = models.ForeignKey(Orgs,max_length=15, db_column='Org', blank=True) # Field name made lowercase.
    gddate = models.DateTimeField(null=True, db_column='GDDate', blank=True) # Field name made lowercase.
    gagrantno = models.CharField(max_length=150, db_column='GAGrantNo', blank=True) # Field name made lowercase.
    disbno = models.CharField(max_length=15, db_column='DisbNo', blank=True) # Field name made lowercase.
    disbinusd = models.FloatField(null=True, db_column='DisbInUSD', blank=True) # Field name made lowercase.
    disbineur = models.FloatField(null=True, db_column='DisbInEUR', blank=True) # Field name made lowercase.
    disbineg = models.FloatField(null=True, db_column='DisbIneg', blank=True) # Field name made lowercase.
    prtype = models.ForeignKey(Orgtype,max_length=60, db_column='PRType', blank=True) # Field name made lowercase.
    gfrating = models.CharField(max_length=15, db_column='GFRating', blank=True) # Field name made lowercase.
    periodstartdate = models.CharField(max_length=150, db_column='PeriodStartDate', blank=True) # Field name made lowercase.
    periodenddate = models.CharField(max_length=150, db_column='PeriodEndDate', blank=True) # Field name made lowercase.
    gadisease = models.ForeignKey(Disease,max_length=90, db_column='GADisease', blank=True) # Field name made lowercase.
    countrycd = models.ForeignKey(Country,max_length=15, db_column='CountryCD', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'fund'
        ordering = ['countrycd']

    def __unicode__(self):
        return '%s%s%s%s%s' %(self.periodenddate,self.periodstartdate,self.gfrating,self.disbno,self.gdcd)

    def get_absolute_url(self):
        return '/globalfund/id/%s/'% self.gdcd

    search = SphinxSearch(
                           
           index ='globalfund_fund' ,
           
               
           
       )
