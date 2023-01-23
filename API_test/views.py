#from django.shortcuts import render
from django.views import View
from .models import games  #Import DB model
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.

class gamesListView(View):

  @method_decorator(csrf_exempt)

  def dispatch(self, request, *args, **kwargs):
    return super().dispatch(request, *args, **kwargs)

  def get(self, request, id=0): #GET function to consume data
    if (id > 0):
      gameslist = list(games.objects.filter(id=id).values())
      if len(gameslist) > 0:
        datos = {'message': "Success", 'games': gameslist}
      else:
        datos = {'message': "Game not found..."}
      return JsonResponse(datos)
            
    else:
      gameslist = list(games.objects.all().values())
      if len(gameslist) > 0:
        datos = {'message': "Success", 'games': gameslist}
      else:
        datos = {'message': "Games not Found..."}
      return JsonResponse(datos, safe=False)
    

  def post(self, request):  # POST method: Adding objects
    datos_recibidos = json.loads(request.body)
    games.objects.create(name=datos_recibidos['name'], category=datos_recibidos['category'], website=datos_recibidos['website'], company=datos_recibidos['company']) # This is how we save the information sent by user/dev
    datos = {'message': 'Saved'}
    return JsonResponse(datos)


  def put(self, request, id): # PUT method: updating objects
    datos_recibidos = json.loads(request.body)
    gameslist = list(games.objects.filter(id=id).values())
    if len(gameslist) > 0 :
      game2 = games.objects.get(id=id)
      game2.name = datos_recibidos['name']
      game2.category = datos_recibidos['category']
      game2.website = datos_recibidos['website']
      game2.company = datos_recibidos['company']
      game2.save()
      datos = {'message': "Saved"}
    else:
      datos = {'message': "This games does not exist"}
    return JsonResponse(datos)


  def delete(self, request, id):  # DELETE method
    gameslist = list(games.objects.filter(id=id).values())
    if len(gameslist) > 0 :
      games.objects.filter(id=id).delete()
      datos = {'message': "Game deleted!"}
    else:
      datos = {'message': "This games does not exist"}
    return JsonResponse(datos)


class gamesListView2(View):   # Getting list by name

  @method_decorator(csrf_exempt)

  def dispatch(self, request, *args, **kwargs):
    return super().dispatch(request, *args, **kwargs)

  def get(self, request, name=''): 
    if len(name) > 0:
      gameslist = list(games.objects.filter(name=name).values())
      if len(gameslist) > 0:
        datos = {'message': "Success", 'games': gameslist}
      else:
        datos = {'message': "Game not Found..."}
      return JsonResponse(datos)