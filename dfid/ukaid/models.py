
from django.db import models
from djangosphinx import SphinxSearch


class Country(models.Model):
    countrycd = models.CharField(max_length=10, primary_key=True, db_column=u'COUNTRYCD', blank=True) # Field name made lowercase.
    country = models.CharField(max_length=80, db_column=u'COUNTRY', blank=True) # Field name made lowercase.
    slug = models.CharField(max_length=100, db_column=u'SLUG', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'ukaid_country'
        
    def __unicode__(self):
        return self.country

    def get_absolute_url(self):
        return '/dfid/country/%s/'% self.slug  

class Projects(models.Model):
    ariescode = models.CharField(max_length=20, primary_key=True, db_column=u'ARIESCODE', blank=True) # Field name made lowercase.
    projecttitle = models.CharField(max_length=50, db_column=u'PROJECTTITLE', blank=True) # Field name made lowercase.
    slug = models.CharField(max_length=150,db_column=u'SLUG', blank=True) # Field name made lowercase. This field type is a guess.

    class Meta:
        db_table = u'Projects'

    def __unicode__(self):
        return self.projecttitle

    def get_absolute_url(self):
        return '/dfid/projects/%s/'% self.slug 

class Risk(models.Model):
    cd = models.CharField(max_length=10, primary_key=True, db_column=u'CD', blank=True) # Field name made lowercase.
    risk = models.CharField(max_length=10,db_column=u'RISK', blank=True) # Field name made lowercase.
    slug = models.CharField(max_length=10,db_column=u'SLUG', blank=True) # Field name made lowercase.
    
    class Meta:
        db_table = u'Risk'

    def __unicode__(self):
        return self.risk

    def get_absolute_url(self):
        return '/dfid/risk/%s/'% self.slug  

class Typefunding(models.Model):
    fundcd = models.CharField(max_length=5,db_column=u'FUNDCD', blank=True) # Field name made lowercase.
    fundnature = models.CharField(max_length=50,db_column=u'FUNDNATURE', blank=True) # Field name made lowercase.
    slug = models.CharField(max_length=60, db_column=u'SLUG', blank=True) # Field name made lowercase.
    
    class Meta:
        db_table = u'TypeFunding'

    def __unicode__(self):
        return self.fundnature

    def get_absolute_url(self):
        return '/dfid/typefunding/%s/'% self.slug  

class Dfid(models.Model):
    componentcode = models.CharField(max_length=20,primary_key=True, db_column=u'COMPONENTCODE') # Field name made lowercase. This field type is a guess.
    ariescode = models.ForeignKey(Projects, max_length=20,db_column=u'ARIESCODE', blank=True) # Field name made lowercase. This field type is a guess.
    projecttitle = models.CharField(max_length=255,db_column=u'PROJECTTITLE', blank=True) # Field name made lowercase. This field type is a guess.
    componenttitle = models.CharField(max_length=255,db_column=u'COMPONENTTITLE', blank=True) # Field name made lowercase. This field type is a guess.
    purpose = models.TextField(db_column=u'PURPOSE', blank=True) # Field name made lowercase. This field type is a guess.
    country = models.ForeignKey(Country, max_length=10,db_column=u'COUNTRY', blank=True) # Field name made lowercase. This field type is a guess.
    fundnature = models.ForeignKey(Typefunding, max_length=5, db_column=u'FUNDNATURE', blank=True) # Field name made lowercase. This field type is a guess.
    start_date = models.CharField(max_length=25,db_column=u'START_DATE', blank=True) # Field name made lowercase. This field type is a guess.
    end_date = models.CharField(max_length=25,db_column=u'END_DATE', blank=True) # Field name made lowercase. This field type is a guess.
    risk = models.ForeignKey(Risk, max_length=10, db_column=u'RISK', blank=True) # Field name made lowercase. This field type is a guess.
    lifetimebudget = models.FloatField(null=True,db_column=u'LIFETIMEBUDGET', blank=True) # Field name made lowercase. This field type is a guess.
    expendituretodate = models.FloatField(null=True,db_column=u'EXPENDITURETODATE', blank=True) # Field name made lowercase. This field type is a guess.
    year = models.CharField(max_length=10,db_column=u'YEAR', blank=True) # Field name made lowercase. This field type is a guess.
    class Meta:
        db_table = u'DFID'
        ordering = ['-year']

    search = SphinxSearch(
                           
           index ='ukaid_dfid' ,
           
               
           
       )


