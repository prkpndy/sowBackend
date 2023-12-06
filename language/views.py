from django.http import HttpResponse, JsonResponse

from .models import Terms, Us, Navigation, PriceListInfo

def index(request):
  return HttpResponse("Hello person! This is the index of language api")

# This is the API endpoint for getting terms
def terms(request):
  terms = list(Terms.objects.values())
  termsDict = {term['key']: term['value'] for term in terms}
  languageData = {
    'terms': termsDict
  }

  response = JsonResponse(languageData)
  response['Access-Control-Allow-Origin'] = '*'

  return response

# This is the API endpoint for getting us
def us(request):
  uss = list(Us.objects.values())
  ussDict = {us['key']: us['value'] for us in uss}
  languageData = {
    'us': ussDict
  }

  response = JsonResponse(languageData)
  response['Access-Control-Allow-Origin'] = '*'

  return response

# This is the API endpoint for getting navigation
def navigation(request):
  navigations = list(Navigation.objects.values())
  navigationsDict = {navigation['key']: {'name': navigation['name'], 'link': navigation['link']} for navigation in navigations}

  languageData = {
    'navigation': navigationsDict
  }

  response = JsonResponse(languageData)
  response['Access-Control-Allow-Origin'] = '*'

  return response

# This is the API endpoint for getting the data on pricelist page
def pricelist(request):
  pricelists = list(PriceListInfo.objects.values())
  pricelistsDict = {pricelist['key']: pricelist['value'] for pricelist in pricelists}

  languageData = {
    'price_list': pricelistsDict
  }

  response = JsonResponse(languageData)
  response['Access-Control-Allow-Origin'] = '*'

  return response