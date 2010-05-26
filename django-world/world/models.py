from django.contrib.gis.db import models
from django.utils.translation import ugettext_lazy as _

CONTINENTS = (('AF', _('Africa')),
             ('AS', _('Asia')),			
             ('EU',  _('Europe')),
             ('NA', _('North America')),
             ('OC', _('Oceania')),
             ('SA',  _('South America')),
             ('AN', _('Antarctica')),)

class Language(models.Model):
    """
    Human languages spoken in the world.
    
    Geonames dataset: http://download.geonames.org/export/dump/iso-languagecodes.txt
    """
    
    iso3_code = models.CharField(_('ISO 639-3 code'), max_length = 3, primary_key = True)
    iso2_code = models.CharField(_('ISO 639-2 code'), max_length = 15, null = True)
    iso1_code = models.CharField(_('ISO 639-1 code'), max_length = 2, null = True)
    name = models.CharField(_('name'), max_length = 150)

    class Meta:
        verbose_name = _('language')
        verbose_name_plural = _('languages')

    def __unicode__(self):
        return self.name



class Country(models.Model):
    """
    Countries of the world.
    
    Geonames dataset: http://download.geonames.org/export/dump/countryInfo.txt
    """
    
    iso_code = models.CharField(_('iso 2 code'), max_length=2, primary_key = True)
    iso3_code = models.CharField(_('iso 3 code'), max_length = 3, unique = True)
    iso_numeric_code = models.PositiveIntegerField(_('iso numeric code'), unique = True)
    fips_code = models.CharField(_('FIPS code'), max_length = 2, null = True)
    name = models.CharField(_('name'), max_length=150, unique = True, db_index = True)
    area = models.PositiveIntegerField(_('area'), db_index = True)
    population = models.PositiveIntegerField(_('population'), db_index = True)
    continent = models.CharField(_('continent'), max_length = 3, choices = CONTINENTS)
    tld = models.CharField(_('TLD'), max_length = 3)
    currency_code = models.CharField(_('currency code'), max_length = 3)
    currency_name = models.CharField(_('currency name'), max_length = 150)
    phone = models.CharField(_('phone'), max_length = 50, null = True)
    postal_code_format = models.CharField(_('postal code format'), max_length = 255, null = True)
    postal_code_regex = models.CharField(_('postal code regex'), max_length = 255, null = True)
    languages = models.ManyToManyField(Language, verbose_name = _('languages'))
    geonames_id = models.PositiveIntegerField(_('geonames ID'), unique = True, db_index = True)
    neighbours = models.ManyToManyField('self', symmetrical = True, verbose_name = _('neighbours'))
    equivalent_fips_code = models.CharField(_('equivalent FIPS code'), max_length = 2, null = True)

    class Meta:
        verbose_name = _('country')
        verbose_name_plural = _('countries')


    def __unicode__(self):
        return self.name
        
class FirstAdministrativeArea(models.Model):
    """
    First administrative areas. Roghly equivalent to US
    states. US states are first administrative areas.
    
    Geonames dataset: http://download.geonames.org/export/dump/admin1Codes.txt
    """
    
    code = models.CharField(_('code'), max_length = 10, primary_key = True)
    name = models.CharField(_('name'), max_length = 150, db_index = True)

    class Meta:
        verbose_name = _('first administrative area')
        verbose_name_plural = _('first administrative areas')

    def __unicode__(self):
        return self.name

class SecondAdministrativeArea(models.Model):
    """
    Second administrative areas. Smaller regions. Roughly equivalent to US
    counties.
    
    Geonames dataset: http://download.geonames.org/export/dump/admin2Codes.txt
    """
    
    code = models.CharField(_('code'), max_length = 50, primary_key = True)
    name = models.CharField(_('name'), max_length = 150, db_index = True)
    ascii_name = models.CharField(_('ASCII name'), max_length = 150, db_index = True)
    geonames_id = models.PositiveIntegerField(_('geonames ID'), db_index = True)

    class Meta:
        verbose_name = _('second administrative area')
        verbose_name_plural = _('second administrative areas')


    def __unicode__(self):
        return self.name 

class FeatureClass(models.Model):
    """
    Feature classes. Used for classification of the geonames
    features dataset.
    
    Geonames dataset: http://download.geonames.org/export/dump/featureCodes_<language>.txt 
    """
    
    code = models.CharField(_('code'), max_length = 10, primary_key = True)
    name = models.CharField(_('name'), max_length = 150, db_index = True )
    description = models.TextField(_('description'))

    class Meta:
        verbose_name = _('feature class')
        verbose_name_plural = _('feature classes')

    def __unicode__(self):
        return self.name 


class Place(models.Model):
    """
    A place is a feature in the geonames jargon.
    
    Geonames datasets:
    http://download.geonames.org/export/dump/cities1000.zip
    http://download.geonames.org/export/dump/cities15000.zip
    http://download.geonames.org/export/dump/cities5000.zip
    http://download.geonames.org/export/dump/allCountries.zip
    
    Also avalable per country datasets.
    """
    
    geonames_id   = models.PositiveIntegerField(_('geonames ID'), primary_key = True)
    name = models.CharField(_('name'), max_length = 200, db_index = True)  
    ascii_name = models.CharField(_('ASCII name'), max_length = 200, db_index = True)
    point = models.PointField(_('point'))
    feature_class = models.ForeignKey(FeatureClass, null = True, verbose_name = _('feature class'))
    country = models.ForeignKey(Country, null = True, verbose_name = _('country'))
    first_admin_area = models.ForeignKey(FirstAdministrativeArea, null = True, verbose_name = _('first administrative area'))
    second_admin_area = models.ForeignKey(SecondAdministrativeArea, null = True, verbose_name = _('second administrative area'))
    population = models.PositiveIntegerField(_('population'), db_index = True)
    elevation   = models.IntegerField(_('elevation'), null = True)
    gtopo30_elevation = models.IntegerField(_('GTOPO30 elevation'), null = True)
    timezone =  models.CharField(_('timezone'), max_length = 50)
    
    objects = models.GeoManager()
    
    class Meta:
        verbose_name = _('place')
        verbose_name_plural = _('places')

    def __unicode__(self):
        return self.ascii_name 


class AlternativeName(models.Model):
    """
    Names in different lagnuages for countries and places.
    
    Geonames dataset: http://download.geonames.org/export/dump/alternateNames.zip
    """
    
    name_id = models.PositiveIntegerField(_('name ID'), primary_key = True)
    language = models.ForeignKey(Language, null = True, verbose_name = _('language'))
    language_code = models.CharField(_('language code'), max_length = 15, null = True)
    geonames_id = models.PositiveIntegerField(_('geonames ID'), db_index = True)
    name = models.CharField(_('name'), max_length  = 255, db_index = True)
    is_preferred = models.BooleanField(_('preferred'), default = False)
    is_short = models.BooleanField(_('short'), default = False)

    class Meta:
        verbose_name = _('alternative name')
        verbose_name_plural = _('alternative names')

    def __unicode__(self):
        return self.name

class CountryAlternativeName(AlternativeName):
    country = models.ForeignKey(Country, verbose_name = _('country'))
    
    class Meta:
        verbose_name = _('alternative name for country')
        verbose_name_plural = _('alternative names for countries')


class PlaceAlternativeName(AlternativeName):
    place = models.ForeignKey(Place, verbose_name = _('place'))

    
    class Meta:
        verbose_name = _('alternative name for place')
        verbose_name_plural = _('alternative names for places')
