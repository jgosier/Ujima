
from django.db import models
from djangosphinx import SphinxSearch





class Country(models.Model):
    countrycd = models.CharField(max_length=5,primary_key=True, db_column=u'CountryCD') # Field name made lowercase.
    country = models.CharField(max_length=50,db_column=u'Country', blank=True) # Field name made lowercase.
    slug = models.CharField(max_length=100,db_column=u'Slug', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'wpcountry'

    def __unicode__(self):
        return self.country

    def get_absolute_url(self):
        return '/arms/country/%s/'% self.slug

    
class Weapon(models.Model):
    category = models.CharField(max_length=5,primary_key=True, db_column=u'Category') # Field name made lowercase.
    description = models.CharField(max_length=150, db_column=u'Description', blank=True) # Field name made lowercase.
    slug = models.CharField(max_length=100,blank=True)
    class Meta:
        db_table = u'weapon'

    def __unicode__(self):
        return self.description

    def get_absolute_url(self):
        return '/arms/weapon/%s/'% self.slug
    


class Arms(models.Model):
    arms_id = models.IntegerField(null=True, primary_key=True, db_column=u'Arms_ID') # Field name made lowercase.
    catcode = models.ForeignKey(Weapon,max_length=5,db_column=u'Catcode',blank=True)
    country = models.ForeignKey(Country,max_length=5,db_column=u'Country',blank=True)
    quantity = models.IntegerField(max_length=15,db_column=u'Quantity',blank=True)
    value = models.IntegerField(max_length=15,null=True,db_column=u'Value', blank=True)
    year = models.CharField(max_length=5,db_column=u'Year',blank=True)
    class Meta:
        db_table = u'arms'
    search = SphinxSearch(
                           
           index ='arms' ,
           
               
           
       )
