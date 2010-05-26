from django.db import models
from django.template.defaultfilters import slugify
class Country(models.Model):
    iso_code = models.CharField(max_length=2, unique=True)
    name = models.CharField(max_length=50)
    iso_numeric = models.CharField(max_length=3, unique=True)
    iso_alpha3 = models.CharField(max_length=3, unique=True)
    fips_code = models.CharField(max_length=2, unique=True)
    continent = models.CharField(max_length=2)
    
    capital = models.CharField(max_length=30, blank=True)
    area_in_sq_km = models.FloatField()
    population = models.IntegerField()
    currency_code = models.CharField(max_length=3)
    # len('en-IN,hi,bn,te,mr,ta,ur,gu,ml,kn,or,pa,as,ks,sd,sa,ur-IN') = 56
    languages = models.CharField(max_length=60)
    geoname_id = models.IntegerField()

    # Bounding boxes
    bbox_west = models.FloatField()
    bbox_north = models.FloatField()
    bbox_east = models.FloatField()
    bbox_south = models.FloatField()
    def lat_lon(self):
        lat=(self.bbox_east+self.bbox_west)/2
        long=(self.bbox_north+self.bbox_south)/2
        return lat,long
    def slug(self):
        return slugify(self.name)
    