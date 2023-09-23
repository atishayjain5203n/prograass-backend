from django.shortcuts import render
from dotenv import load_dotenv
import os
import firebase_admin
import json
from firebase_admin import credentials, firestore
from django.http import HttpResponseBadRequest
from rest_framework.decorators import api_view
from django.http.response import JsonResponse
from google.cloud.firestore_v1.base_query import FieldFilter
load_dotenv()
cred_key = {
  "type": os.environ.get('TYPE'),
  "project_id": os.environ.get('PROJECT_ID'),
  "private_key_id": os.environ.get('PRIVATE_KEY_ID'),
  "private_key": os.environ.get('PRIVATE_KEY'),
  "client_email": os.environ.get('CLIENT_EMAIL'),
  "client_id": os.environ.get('CLIENT_ID'),
  "auth_uri": os.environ.get('AUTH_URI'),
  "token_uri": os.environ.get('TOKEN_URI'),
  "auth_provider_x509_cert_url": os.environ.get('AUTH_PROVIDER_URL'),
  "client_x509_cert_url": os.environ.get('CLIENT_CERT_URL'),
  "universe_domain": os.environ.get('UNIVERSE_DOMAIN')
}
cred = credentials.Certificate(cred_key)
firebase_admin.initialize_app(cred)

@api_view(['GET', 'POST', 'DELETE'])
def getList(request):
    db= firestore.client()
    list= db.collection("peers")
    if(request.method== 'GET'): 
     peers= list.stream()
     res = {"peers": []}
     for peer in peers:
         data= peer.to_dict()
         curres= {}
         curres = data
         res["peers"].append(
             curres
         )
         print(res)   
     return JsonResponse(res, safe=False)
 
@api_view(['GET', 'POST', 'DELETE'])
def addObject(request):
    db= firestore.client()
    new_peer= db.collection("projects").document("4e401fbb40f76c61e270")
    details= {}
    with open("apis/pq.json") as json_file:
        details = json.load(json_file)
    new_peer.set(details)
    return JsonResponse({'success': True}, safe=False)

@api_view(['GET', 'POST', 'DELETE'])
def addParameter(request):
    db= firestore.client()
    peer_list= db.collection("peers")
    project_list = db.collection("projects").stream()
    for project in project_list:
         data= project.to_dict()
         for peers in data["members"]:
             peer_list.document(peers).update({"myprojects": firestore.ArrayUnion([str(data["project_id"])])})
             
    return JsonResponse({'success': True}, safe=False)    

@api_view(['GET', 'POST', 'DELETE'])
def getProjectList(request):
    db = firestore.client()
    project_list = db.collection("projects")
    peers= project_list.stream()
    res = {"projects": []}
    for peer in peers:
         data= peer.to_dict()
         curres= {}
         curres = data
         res["projects"].append(
             curres
         )
         print(res)   
    return JsonResponse(res, safe=False)
    
@api_view(['GET', 'POST', 'DELETE'])
def getPeerById(request):
    db = firestore.client()
    peer_list = db.collection("peers")
    id = request.query_params.get('id', None)
    if id  is None:
        return HttpResponseBadRequest('id param not present')     
    else:
       peers = peer_list.where(filter = FieldFilter("uid","==", id)).stream()
       for peer in peers:
            data= peer.to_dict()
            res ={}
            res= data
            return JsonResponse(res, safe= True)
    return HttpResponseBadRequest('record not present') 
@api_view(['GET', 'POST', 'DELETE'])
def getProjectById(request):
    db = firestore.client()
    project_list = db.collection("projects")
    id = request.query_params.get('id', None)
    if id  is None:
        return HttpResponseBadRequest('id param not present')     
    else:
       projects = project_list.where(filter = FieldFilter("project_id","==", id)).stream()
       for project in projects:
            data= project.to_dict()
            res ={}
            res= data
            return JsonResponse(res, safe= True)
    return HttpResponseBadRequest('record not present') 
   
        
@api_view(['GET', 'POST', 'DELETE'])
def empty(request):
    return JsonResponse({'status': 'url not valid'}, safe=True)