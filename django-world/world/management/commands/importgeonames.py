from django.core.management.base import BaseCommand, CommandError
from django.db.models.loading import get_model
from django.db.models import Q
from django.db import transaction
import datetime
import csv
import _csv

from world.models import Language, Country, Place, FirstAdministrativeArea, SecondAdministrativeArea
from world.models import FeatureClass, CountryAlternativeName, PlaceAlternativeName

def unicode_csv_reader(utf8_data, dialect=csv.excel, **kwargs):
    csv_reader = csv.reader(utf8_data, dialect=dialect, quoting = csv.QUOTE_NONE, **kwargs)
    for row in csv_reader:
        yield [unicode(cell, 'utf-8').lstrip(u'\ufeff').strip() for cell in row]



class Command(BaseCommand):
        help = 'Imports data for a table from the geonames database.'
        args = 'table csvfile'
        tables = ['languages', 'countries', 'firstadmin', 'secondadmin', 'fclasses', 'places', 'altnames']
        
        @transaction.commit_on_success
        def _import_languages(self, csvfile):
            i = 0
            for row in unicode_csv_reader(open(csvfile), delimiter = '\t'):
                Language.objects.get_or_create(iso3_code = row[0], iso2_code = row[1] or None, iso1_code  = row[2] or None, name = row[3] )
                i+=1
            return i

        @transaction.commit_on_success
        def _import_countries(self, csvfile):
            i = 0
            for row in unicode_csv_reader(open(csvfile), delimiter = '\t'):
                try:
                    country = Country.objects.get(pk = row[0])
                except Country.DoesNotExist:
                    country = Country(iso_code = row[0])
                country.iso3_code = row[1]
                country.iso_numeric_code = long(float(row[2]))
                country.fips_code = row[3] or None
                country.name = row[4]
                country.area = long(float(row[6] or 0))
                country.population = long(float(row[7]))
                country.continent = row[8]
                country.tld = row[9]
                country.currency_code = row[10]
                country.currency_name = row[11]
                country.phone = row[12] or None
                country.postal_code_format = row[13] or None
                country.postal_code_regex = row[14] or None
                country.geonames_id = long(float(row[16]))
                country.equivalent_fips_code = row[18] or None
                country.save()
                langs = row[15].split(',')
                for language in Language.objects.filter(Q(iso3_code__in = langs) |
                                                        Q(iso2_code__in = langs) |
                                                        Q(iso1_code__in = langs)):
                    country.languages.add(language)
                country.save()
                
                i+=1
            

            for row in unicode_csv_reader(open(csvfile), delimiter = '\t'):
                country  = Country.objects.get(iso_code = row[0])
                for neighbour in Country.objects.filter(iso_code__in = row[17].split(',')):
                    if not neighbour in country.neighbours.all():
                        country.neighbours.add(neighbour)
                country.save()
            
            return i
        
        @transaction.commit_on_success
        def _import_firstadmin(self, csvfile):
            i = 0
            for row in unicode_csv_reader(open(csvfile), delimiter = '\t'):
                try:
                    area = FirstAdministrativeArea.objects.get(pk = row[0])
                except FirstAdministrativeArea.DoesNotExist:
                    area = FirstAdministrativeArea(code = row[0])
                area.name = row[1]
                area.save()
            i+=1
            return i
        
        @transaction.commit_on_success
        def _import_secondadmin(self, csvfile):
            i = 0
            for row in unicode_csv_reader(open(csvfile), delimiter = '\t'):
                try:
                    area = SecondAdministrativeArea.objects.get(pk = row[0])
                except SecondAdministrativeArea.DoesNotExist:
                    area = SecondAdministrativeArea(code = row[0])
                area.name = row[1]
                area.ascii_name = row[2]
                area.geonames_id = long(row[3])
                area.save()
                i += 1
            return i
        
        @transaction.commit_on_success
        def _import_fclasses(self, csvfile):
            i = 0
            for row in unicode_csv_reader(open(csvfile), delimiter = '\t'):
                try:
                    featureclass = FeatureClass.objects.get(pk = row[0])
                except FeatureClass.DoesNotExist:
                    featureclass = FeatureClass(code = row[0])
                featureclass.name = row[1]
                featureclass.description = row[2]
                featureclass.save()
                i += 1
            return i
        
        @transaction.commit_on_success
        def _import_places(self, csvfile):
            i = 0
            for row in unicode_csv_reader(open(csvfile), delimiter = '\t'):
                
                try:
                    place = Place.objects.get(pk = long(float(row[0])))
                except Place.DoesNotExist:
                    place = Place(geonames_id = long(float(row[0])))
                place.name = row[1]
                place.ascii_name = row[2]
                place.point = 'POINT(%f %f)'%(float(row[4]), float(row[5]))
                try:
                    place.feature_class = FeatureClass.objects.get(pk = "%s.%s"%(row[6], row[7]))
                except FeatureClass.DoesNotExist:
                    pass
                try:
                    place.country = Country.objects.get(pk = row[8])
                except Country.DoesNotExist:
                    pass
                if row[10]:
                    try:
                        place.first_admin_area = FirstAdministrativeArea.objects.get(pk = "%s.%s"%(row[8],row[10]))
                    except FirstAdministrativeArea.DoesNotExist:
                        pass
                if row[10] and row[11]:
                    try:
                        place.second_admin_area = SecondAdministrativeArea.objects.get(pk = "%s.%s.%s"%(row[8],row[10], row[11]))
                    except SecondAdministrativeArea.DoesNotExist:
                        pass
                place.population = long(float(row[14]))
                if row[15]:
                    place.elevation   = long(float(row[15]))
                if row[16]:
                    place.gtopo30_elevation = long(float(row[16]))
                place.timezone =  row[17]
                place.save()
                i += 1
            return i
        
        @transaction.commit_on_success
        def _import_altnames(self, csvfile):
            i = 0
            #warmup lookups
            languages1dict = {}
            languages3dict = {}
            for language in Language.objects.all():
                languages1dict[language.iso1_code] = language
                languages3dict[language.iso3_code] = language
            placesdict = {}
            for place in Place.objects.all():
                placesdict[place.pk]  = place
            countriesdict = {}
            for country in Country.objects.all():
                countriesdict[country.pk] = country
                
            for row in unicode_csv_reader(open(csvfile), delimiter = '\t'):
                place = placesdict.get(long(float(row[1])), None)
                country = countriesdict.get(long(float(row[1])), None)
                name = None
                if place:
                    try:
                        name = PlaceAlternativeName.objects.get(pk = long(float(row[0])))
                    except PlaceAlternativeName.DoesNotExist:
                        name = PlaceAlternativeName(name_id = long(float(row[0])))
                    name.place = place
                elif country:
                    try:
                        name = CountryAlternativeName.objects.get(pk = long(float(row[0])))
                    except CountryAlternativeName.DoesNotExist:
                        name = CountryAlternativeName(name_id = long(float(row[0])))                
                    name.country = country
                if name:
                    name.language = languages1dict.get(row[2], languages3dict.get(row[2], None))
                    name.name = row[3]
                    name.language_code = row[2]
                    name.is_preferred = row[4] == '1'
                    name.is_short = row[5] == '1'
                    name.geonames_id = long(float(row[1]))
                    name.save()
                    i += 1

            return i
        
                

        def handle(self, table, csvfile, **options):

            if table not in self.tables:
                raise CommandError("Table should be one of %s"%self.tables)

            imported = getattr(self, '_import_%s'%table)(csvfile)


            print "Imported %d rows."%(imported)