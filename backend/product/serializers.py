 

from rest_framework import serializers

from .models import Product


class Productserializer(serializers.ModelSerializer):

    #in case you wanna change an attribut name or function exemple from get_discount to discount_price
    
    # 1--first use serializers methode fiels
    discount_price=serializers.SerializerMethodField(read_only=True)
    class Meta:
        model=Product   
        #2--add the name to the fields
        fields=['title','content','price','seler_price','discount_price']

    #3-- add function get_.. that return the original function from the model     
    def get_discount_price(self,obj):
            return obj.get_discount()
            

