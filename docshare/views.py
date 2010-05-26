from django.shortcuts import render_to_response
import scribd
from Ujima.docshare.models import *

def document_viewer(request,doc_id,template):
    doc=Document.objects.get(scribd_id=doc_id)
    doc_id=doc_id
    doc_access=doc.scribd_secret
    return render_to_response(template,locals())
def Document_list(request,template):
    docs=Document.objects.all()
    return render_to_response(template,locals())
def doc_search(requet):
    if 'q' in request.GET:
        q = request.GET['q']
        document_results = Document.objects.filter(Document__title__icontains=q)
    else:
        q = None
        document_results = None
    return render_to_response('main/doc_results.html',
                {'document_results': document_results, 'query': q},context_instance=RequestContext(request))


    return render_to_response(template,locals())
def Upload_from_file(request,file):
    
    """Passes the uploaded file to Scribd and returns scribd link."""
    scribd.config(API_KEY, API_SECRET)
       
    try:
        # Upload the file to Scribd.
        document = scribd.api_user.upload(file, access='private')
        ret=document.get_scribd_url()
        document.save()

        # Redirect back to the main page.
    except scribd.ResponseError, err:
        pass
    return ret
def upload_from_url(request,url):
    
    scribd.config(API_KEY, API_SECRET)
    try:
        # Upload the file to Scribd.
        document = scribd.api_user.upload_from_url(url, access='private')
        ret=document.get_scribd_url()
        document.save()
    except scribd.ResponseError, err:
        pass
        

def get_docs(request,query):
# Configure the Scribd API.
    scribd.config(API_KEY, API_SECRET)
    try:
        # Log the user in.
        user = scribd.login(USERNAME, PASSWORD)
        # Get all documents uploaded by the user.
        docs = user.all()
                
        # Search the user documents for the phrase query
        results = user.find('checklist')
        

    except scribd.ResponseError, err:
        print 'Scribd failed: code=%d, error=%s' % (err.errno, err.strerror)

    
