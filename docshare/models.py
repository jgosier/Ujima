from django.db import models
from tagging.fields import TagField
from tagging.models import Tag
import scribd
from Ujima.settings import API_KEY, API_SECRET,MEDIA_ROOT

class Document(models.Model):
    title = models.CharField(max_length=100,unique=True)
    description = models.CharField(max_length=100,blank=True,null=True)
    category=models.CharField(max_length=100,blank=True,null=True)
    access=models.CharField(max_length=20,default='c')
    language=models.CharField(max_length=20,default='en')
    show_ads=models.BooleanField(default="false")
    document = models.FileField(upload_to='Docs')
    tag_list=models.CharField(max_length=100,blank=True,null=True)
    scribd_id = models.CharField(max_length=100,blank=True,null=True)
    scribd_secret=models.CharField(max_length=50,blank=True,null=True)
    
    
    class Meta:
        db_table = 'documents'
        ordering = ('-title',)
    def __unicode__(self):
        return "%s %s %s%s%s" %(self.title,self.description,self.category,self.access,self.language)
    def _get_tags(self):
        return Tag.objects.get_for_object(self) 
    def _set_tags(self, tag_list):
        Tag.objects.update_tags(self, tag_list)
    tags = property(_get_tags, _set_tags)
    def document_url(self):
        filename = self.document.path
        basename,name=filename.rsplit('/',1)
        return u'/Media/Docs/'+name
    def document_path(self):
        return self.document.path
    def save(self):
        scribd.config(API_KEY, API_SECRET)
        ###upload doc to scribd for conversion###
        try:
            basename,name=self.document.path.rsplit('/',1)
            doc = scribd.api_user.upload(open(MEDIA_ROOT+'/Docs/'+name))
            self.scribd_id=doc.id
            self.scribd_secret=doc.access_key
            doc.title = self.title
            doc.description = self.description
            doc.access = self.access
            doc.language = self.language
            doc.tags = self.tag_list
            doc.show_ads = self.show_ads
            # Commit all above changes.
            doc.save()
        except scribd.ResponseError, err:
            print 'Scribd failed: code=%d, error=%s' % (err.errno, err.strerror)
        super(Document,self).save()
        self.tags = self.tag_list
    