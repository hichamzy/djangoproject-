
from rest_framework import generics
from rest_framework import permissions,authentication
from rest_framework import filters



from .models import Product
from .serializers import Productserializer
from .permissions import IsStaffPermissions  #ISstaffpermissions class that make the superuser the only one who can create update delete



#1
#  create  product 
class ProductCreateAPIView(generics.CreateAPIView):
    
    
    queryset=Product.objects.all()
    serializer_class=Productserializer
    permission_classes=[permissions.IsAdminUser ,IsStaffPermissions] #you can not create a product without being admin and name hicham 
    authentication_classes = [authentication.SessionAuthentication]


    def validate_data(self,serializer):
        title=serializer.validated_data.get('title')
        content=serializer.validated_data.get('content')
        price=serializer.validated_data.get('price')
        
        """if content is None:
            content=title"""          
    
        serializer.save() 

product_create_view=ProductCreateAPIView.as_view()



#2
#detail of the product
class ProductDetailAPIView(generics.RetrieveAPIView):
    
    
    queryset=Product.objects.all()
    serializer_class=Productserializer
    permission_classes=[permissions.IsAdminUser ,IsStaffPermissions]
    authentication_classes = [authentication.SessionAuthentication]
    #lookup_field='pk'

product_detail_view=ProductDetailAPIView.as_view()   #for detail view 





#3
#list and create product
class ProductListCreateAPIView(generics.ListCreateAPIView):
    
    
    queryset=Product.objects.all()
    serializer_class=Productserializer
    permission_classes=[permissions.IsAdminUser ,IsStaffPermissions]
    authentication_classes = [authentication.SessionAuthentication]
    

product_list_create_view=ProductListCreateAPIView.as_view()




#4
#update product 
class ProductUpdateAPIView(generics.UpdateAPIView):

    queryset=Product.objects.all()
    serializer_class=Productserializer
    permission_classes=[permissions.IsAdminUser ,IsStaffPermissions]
    authentication_classes = [authentication.SessionAuthentication]
    
    def update_data(self,serializer):
        instance=serializer.saved 
        title=serializer.validated_data.get('title')
        content=serializer.validated_data.get('content')
        price=serializer.validated_data.get('price')
        serializer.save() 

product_update_view= ProductUpdateAPIView.as_view()



#5
#delete product 
class ProductDestroyAPIView(generics.DestroyAPIView):
    
    queryset=Product.objects.all()
    serializer_class=Productserializer
    lookup_field='pk'
    permission_classes=[permissions.IsAdminUser ,IsStaffPermissions]
    
    
    def destoy_data(self,instance):
        super().perform_destroy(instance)


product_delete_view= ProductDestroyAPIView.as_view()





#6
#list product view
class ProductListAPIView(generics.ListAPIView):
    queryset=Product.objects.all()
    serializer_class=Productserializer
    authentication_classes = [authentication.SessionAuthentication] 
    permission_classes=[permissions.IsAuthenticated] 


product_list_view=ProductListAPIView.as_view()




class productListView(generics.ListAPIView):
    queryset=Product.objects.all()
    serializer_class=Productserializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title','content','price']


product_search=productListView.as_view()