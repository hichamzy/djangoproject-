import json
#from django.http import JsonResponse 
from rest_framework.decorators import api_view
from rest_framework.response import Response
from product.models import Product
from django.forms.models import model_to_dict  #convert the model to a dict
from product.serializers import Productserializer


@api_view(["GET"])
def api_home(request,*args,**kwargs):
    data={}
    instance =Product.objects.all().order_by("?").first()
    data=Productserializer(instance).data
    return Response(data)