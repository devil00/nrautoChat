from collections import Counter,defaultdict

#NF Field 
unitDict={"calories":"kcal","total fat":"g","potassium":"mg","saturated fat":"g","trans fat":"mg","total carbohydrate":"g","iron":"mg","cholesterol":"mg","sugars":"g","dietary fiber":"g","protein":"g","vitamin a":"IU","vitamin c":"IU","calcium":"mg","sodium":"mg"}

class Speller:

 def __init__(self):
    self.nutrients=unitDict.keys()
   

 def spell_correct(self,message): 
    message=list(message.lower().strip())
    nut_len=[len(n) for n in self.nutrients]
    mLen=len(message)
    if mLen in nut_len:
       w_index=get_duplIndex(nut_len,mLen) 
       try:
         for index in w_index:
           Oword=list(self.nutrients[index])           
           for i,w in message:      
              if message[i]==Oword:
                 continue
              else:      
                message[i],message[i+1]=message[i+1],message[i]
       except IndexError:
           return message 
    return "".join(message)  

def get_duplIndex(slt,element):
   words_len=defaultdict(list)
   for i,item in enumerate(slt):
      words_len[item].append(i)       
   words_len={k:v for k,v in words_len.items() if len(v)>1}
   return words_len[element]

class MessageParser:
  def __init__(self,message): 
    self.message=message
   

  def parse_message(self): 
     import re
     """
     try:
        import re
     except ImportError:
       raise ("re module is not defined")      
     else:
        return self.message
     """
     title=re.search(r'in\s+(\w+)',self.message)
     nutRgx=[re.compile(r'\b'+n+r'\b',re.I) for n in unitDict.keys()]  
     ques=filter(lambda l:l is not None ,map(lambda l : l.search(self.message),nutRgx))
     if any(ques):
      ques=ques[0].group()
     if title and ques:
         return (title.group(1),ques)
     else:
         return (None,None)
     
     
class SolrFetch:
  def __init__(self,title,field):
        self.title=title
        self.field=field

  def processQuery(self): 
     import urllib2,json
     try :
        url="http://72.251.210.26:8985/solr/select?q=title&facet=true&rows=1&fl=field&wt=json"
        url=url.replace("title",self.title).replace("field","fs_"+self.field.replace(" ","_"))
        doc=urllib2.urlopen(url).read()   
        doc=json.loads(doc)
        value=doc['response']['docs'][0]["fs_"+self.field.replace(" ","_")]
     except:
       value=None

     out_template="%s contains %s %s %s "%(self.title.title(),value,self.__getUnit(),self.field.title())

     return out_template

  def __getUnit(self):
    return unitDict[self.field]          
