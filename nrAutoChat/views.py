from django.shortcuts import render_to_response,render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from mechanize import Speller,MessageParser,SolrFetch
import json

def index(request):
 return  render (request,'index.html')

@csrf_exempt
def process_message(request): 
    if request.method=='POST':
       
      message=request.POST['message'].lower().strip()
      mp=MessageParser(message)
      (title,field)=mp.parse_message()
      if title:  
        sf=SolrFetch(title,field)
        result=sf.processQuery()
        return HttpResponse(json.dumps({'message':result}),mimetype='application/javascript') 
      else:
       return HttpResponse(json.dumps({'message':"Not Valid"}),mimetype='application/javascript') 
