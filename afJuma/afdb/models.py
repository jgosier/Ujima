from django.db import models

class Bidcountry(models.Model):
    countrycd = models.CharField(max_length=10,primary_key=True, db_column=u'CountryCD', blank=True) # Field name made lowercase.
    biddercountry = models.CharField(max_length=80,db_column=u'BidderCountry', blank=True) # Field name made lowercase.
    slug = models.CharField(max_length=100,db_column=u'Slug', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'BidCountry'

    def __unicode__(self):
        return self.bidcountry

    def get_absolute_url(self):
        return '/afdb/bidcountry/%s/'% self.slug   

class Bidders(models.Model):
    biddercod = models.CharField(max_length=25,primary_key=True, db_column=u'Biddercod', blank=True) # Field name made lowercase.
    biddername = models.CharField(max_length=200,db_column=u'BidderName', blank=True) # Field name made lowercase.
    slug = models.CharField(max_length=255,db_column=u'Slug', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'Bidders'
        
    def __unicode__(self):
        return self.biddername

    def get_absolute_url(self):
        return '/afdb/bidder/%s/'% self.slug   

class Projcountry(models.Model):
    countrycd = models.CharField(max_length=10,primary_key=True, db_column=u'CountryCD', blank=True) # Field name made lowercase.
    projectcountry = models.CharField(max_length=80,db_column=u'ProjectCountry', blank=True) # Field name made lowercase.
    slug = models.CharField(max_length=100,db_column=u'Slug', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'ProjCountry'

   

    def get_absolute_url(self):
        return '/afdb/projcountry/%s/'% self.slug   

class Companies(models.Model):
    code = models.CharField(max_length=25,primary_key=True, db_column=u'Code', blank=True) # Field name made lowercase.
    companyname = models.CharField(max_length=100,db_column=u'CompanyName', blank=True) # Field name made lowercase.
    slug = models.CharField(max_length=200,db_column=u'Slug', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'companies'

    def __unicode__(self):
        return self.companyname

    def get_absolute_url(self):
        return '/afdb/companies/%s/'% self.slug   



class Expensecode(models.Model):
    code = models.CharField(max_length=25,primary_key=True, db_column=u'Code', blank=True) # Field name made lowercase.
    expensecategory = models.CharField(max_length=80,db_column=u'ExpenseCategory', blank=True) # Field name made lowercase.
    slug = models.CharField(max_length=100,db_column=u'Slug', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'expensecode'

    def __unicode__(self):
        return self.expensecategory

    def get_absolute_url(self):
        return '/afdb/expensecategory/%s/'% self.slug   

class Procuremode(models.Model):
    code = models.CharField(max_length=25,primary_key=True, db_column=u'Code', blank=True) # Field name made lowercase.
    procurementmode = models.CharField(max_length=60,db_column=u'ProcurementMode', blank=True) # Field name made lowercase.
    slug = models.CharField(max_length=80,db_column=u'Slug', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'procuremode'

   

    def get_absolute_url(self):
        return '/afdb/procuremode/%s/'% self.slug   

class Sectors(models.Model):
    code = models.CharField(max_length=25,primary_key=True, db_column=u'Code', blank=True) # Field name made lowercase.
    sector = models.CharField(max_length=80,db_column=u'Sector', blank=True) # Field name made lowercase.
    slug = models.CharField(max_length=100,db_column=u'Slug', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'sectors'

    def __unicode__(self):
        return self.sector

    def get_absolute_url(self):
        return '/afdb/sector/%s/'% self.slug   


class Contract(models.Model):
    contrno = models.CharField(max_length=50,primary_key=True, db_column=u'ContrNo') # Field name made lowercase. This field type is a guess.
    year = models.CharField(max_length=10,db_column=u'Year', blank=True) # Field name made lowercase. This field type is a guess.
    projectdefinition = models.TextField(db_column=u'ProjectDefinition', blank=True) # Field name made lowercase. This field type is a guess.
    biddercod = models.ForeignKey(Bidders,db_column=u'Biddercod', blank=True) # Field name made lowercase. This field type is a guess.
    biddername = models.CharField(max_length=80,db_column=u'BidderName', blank=True) # Field name made lowercase. This field type is a guess.
    bidcountrycd = models.ForeignKey(Bidcountry,db_column=u'BidCountryCD', blank=True) # Field name made lowercase. This field type is a guess.
    description = models.TextField(db_column=u'Description', blank=True) # Field name made lowercase. This field type is a guess.
    companyname = models.CharField(max_length=100,db_column=u'CompanyName', blank=True) # Field name made lowercase. This field type is a guess.
    companycode = models.ForeignKey(Companies,db_column=u'CompanyCode', blank=True) # Field name made lowercase. This field type is a guess.
    expensecode = models.ForeignKey(Expensecode,db_column=u'Expensecode', blank=True) # Field name made lowercase. This field type is a guess.
    contracttitle = models.TextField(db_column=u'Contracttitle', blank=True) # Field name made lowercase. This field type is a guess.
    procmode = models.ForeignKey(Procuremode,db_column=u'Procmode', blank=True) # Field name made lowercase. This field type is a guess.
    projcountrycd = models.ForeignKey(Projcountry,db_column=u'ProjCountryCD', blank=True) # Field name made lowercase. This field type is a guess.
    tendernum = models.CharField(max_length=50,db_column=u'Tendernum', blank=True) # Field name made lowercase. This field type is a guess.
    loannumber = models.CharField(max_length=50,db_column=u'LoanNumber', blank=True) # Field name made lowercase. This field type is a guess.
    totalamount = models.FloatField(db_column=u'TotalAmount', blank=True) # Field name made lowercase. This field type is a guess.
    class Meta:
        db_table = u'contract'

    #def __unicode__(self):
        #return "%s%s"self.biddercod

 

