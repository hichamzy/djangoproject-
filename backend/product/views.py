
from rest_framework import generics
from rest_framework import permissions,authentication




from .models import Product
from .serializers import Productserializer


#  create  product 
class ProductCreateAPIView(generics.CreateAPIView):
    
    
    queryset=Product.objects.all()
    serializer_class=Productserializer
    permission_classes=[permissions.IsAuthenticated] #you can not create a product without being autenticated 
    authentication_classes = [authentication.SessionAuthentication]


    def validate_data(self,serializer):
        title=serializer.validated_data.get('title')
        content=serializer.validated_data.get('content')
        price=serializer.validated_data.get('price')
        
        """if content is None:
            content=title"""          
    
        serializer.save() 

product_create_view=ProductCreateAPIView.as_view()


#detail of the product
class ProductDetailAPIView(generics.RetrieveAPIView):
    
    
    queryset=Product.objects.all()
    serializer_class=Productserializer
    permission_classes=[permissions.IsAuthenticated]
    authentication_classes = [authentication.SessionAuthentication]
    #lookup_field='pk'

product_detail_view=ProductDetailAPIView.as_view()   #for detail view 




#list and create product
class ProductListCreateAPIView(generics.ListCreateAPIView):
    
    
    queryset=Product.objects.all()
    serializer_class=Productserializer
    permission_classes=[permissions.IsAuthenticated]
    authentication_classes = [authentication.SessionAuthentication]
    

product_list_create_view=ProductListCreateAPIView.as_view()



#update product 
class ProductUpdateAPIView(generics.UpdateAPIView):

    queryset=Product.objects.all()
    serializer_class=Productserializer
    permission_classes=[permissions.IsAuthenticated]
    authentication_classes = [authentication.SessionAuthentication]
    
    def update_data(self,serializer):
        instance=serializer.saved 
        title=serializer.validated_data.get('title')
        content=serializer.validated_data.get('content')
        price=serializer.validated_data.get('price')
        serializer.save() 

product_update_view= ProductUpdateAPIView.as_view()


#delete product 
class ProductDestroyAPIView(generics.DestroyAPIView):
    
    queryset=Product.objects.all()
    serializer_class=Productserializer
    lookup_field='pk'
    permission_classes=[permissions.IsAuthenticated]
    
    
    def destoy_data(self,instance):
        super().perform_destroy(instance)


product_delete_view= ProductDestroyAPIView.as_view()




#list product view
class ProductListAPIView(generics.ListAPIView):
    queryset=Product.objects.all()
    serializer_class=Productserializer
    authentication_classes = [authentication.SessionAuthentication] 
    permission_classes=[permissions.IsAuthenticated]


product_list_view=ProductListAPIView.as_view()