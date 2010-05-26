

from django.db import models
from djangosphinx2.models import SphinxSearch


class Agency(models.Model):
    office = models.CharField(max_length=10, primary_key=True, db_column='Office') # Field name made lowercase.
    agency = models.CharField(max_length=100, db_column='Agency', blank=True) # Field name made lowercase.
    slug = models.CharField(max_length=100, db_column='Slug', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'agency'

    def __unicode__(self):
        return self.agency

    def get_absolute_url(self):
        return '/aid/agency/%s/'% self.slug   



class Country(models.Model):
    code = models.CharField(max_length=30, primary_key=True, db_column='Code') # Field name made lowercase.
    country = models.CharField(max_length=550, db_column='Country', blank=True) # Field name made lowercase.
    slug = models.CharField(max_length=80, db_column='Slug', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'country_aid'


    def __unicode__(self):
        return self.country
    

    def get_absolute_url(self):
        return '/aid/country/%s/'% self.slug

class Prodcode(models.Model):
    prodcode = models.CharField(max_length=10, primary_key=True, db_column='ProdCode') # Field name made lowercase.
    pdescription = models.CharField(max_length=100, db_column='pdescription', blank=True) # Field name made lowercase.
    slug = models.CharField(max_length=150, blank=True)
    class Meta:
        db_table = u'prodcode'


    def __unicode__(self):
        return self.pdescription

    def get_absolute_url(self):
        return '/aid/product/%s/'% self.slug
    

class Vendors(models.Model):
    duns = models.CharField(max_length=25, primary_key=True)
    name = models.CharField(max_length=80, blank=True)
    slug = models.CharField(max_length=200, blank=True)
    class Meta:
        db_table = u'vendors'


    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return '/aid/vendor/%s/'% self.slug


class Aid(models.Model):
    usaidid = models.IntegerField(primary_key=True,db_column='usaidid') # Field name made lowercase.
    piid = models.CharField(max_length=30, db_column='PIID', blank=True) # Field name made lowercase.
    vendor = models.CharField(max_length=80, db_column='Vendor', blank=True) # Field name made lowercase.
    duns = models.ForeignKey(Vendors,max_length=25, db_column='DUNS', blank=True) # Field name made lowercase.
    parent = models.CharField(max_length=80, db_column='Parent', blank=True) # Field name made lowercase.
    dollars = models.FloatField(null=True, db_column='Dollars', blank=True) # Field name made lowercase.
    agency = models.ForeignKey(Agency,max_length=25, db_column='Agency', blank=True) # Field name made lowercase.
    datesigned = models.DateTimeField(null=True, db_column='Datesigned', blank=True) # Field renamed to remove spaces. Field name made lowercase.
    compdate = models.DateTimeField(null=True, db_column='Compdate', blank=True) # Field name made lowercase.
    description = models.TextField(db_column='Description', blank=True) # Field name made lowercase.
    pcountry = models.ForeignKey(Country,max_length=50, db_column='Pcountry', blank=True) # Field name made lowercase.
    ocountry = models.CharField(max_length=80, db_column='Ocountry', blank=True) # Field name made lowercase.
    year = models.CharField(max_length=5, db_column='Year', blank=True) # Field name made lowercase.
    employnum = models.FloatField(null=True, db_column='EmployNum', blank=True) # Field name made lowercase.
    address = models.CharField(max_length=80, db_column='Address', blank=True) # Field name made lowercase.
    city = models.CharField(max_length=80, db_column='City', blank=True) # Field name made lowercase.
    state = models.CharField(max_length=50, db_column='State', blank=True) # Field name made lowercase.
    vcountry = models.CharField(max_length=100, db_column='VCountry', blank=True) # Field name made lowercase.
    prodcode = models.ForeignKey(Prodcode,max_length=10, db_column='ProdCode', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'aid'
        ordering = ["datesigned"]
    search = SphinxSearch(
                           
           index ='aid' ,
           
               
           
       )


