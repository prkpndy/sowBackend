from django.http import HttpResponse, JsonResponse

from .models import PriceListItems

def index(request):
  return HttpResponse("Hello person! This is the index of pricelist api")

def pricelist(request, offset):
  itemList = list(PriceListItems.objects.order_by('article_number').values())
  data = {'data': itemList}

  response = JsonResponse(data)
  response['Access-Control-Allow-Origin'] = '*'

  return response

# Access-Control-Allow-Origin
# Access-Control-Allow-Methods
# Access-Control-Allow-Credentials
