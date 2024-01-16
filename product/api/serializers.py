from rest_framework.serializers import ModelSerializer, ValidationError
from product.models import UserProduct
from user.models import User
from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

class UserProductSerializer(ModelSerializer):    
    class Meta:
        model = UserProduct
        fields = '__all__'

# cria Um produto de cada vez
#     def addProduct(self, body, userId):          

#             userExists = User.objects.filter(id=userId).first()            
            
#             if userExists == None:                
#                  raise ValidationError("User Not Found", code=status.HTTP_404_NOT_FOUND)                             
            
#             body['user'] = userExists            

#             userProductCreated = UserProduct.objects.create(**body)                               

#             return userProductCreated 

     
        
    def addProduct(self, body, userId):                 

            userExists = User.objects.filter(id=userId).first()            
            
            if userExists == None:                
                 raise ValidationError("User Not Found", code=status.HTTP_404_NOT_FOUND)           

            for product in body:
                 print(product['user'])
                 product['user'] = userExists 

            user_products = [UserProduct(**data) for data in body]
            productCreated = UserProduct.objects.bulk_create(user_products)                                            

            # Serializar os objetos UserProduct criados
            serializer = UserProductSerializer(productCreated, many=True)
            returnListProducts = serializer.data
            
            return returnListProducts
    
    
    def getProductsByUserId(self, request, userId):
        try:

            default_page = 1
            default_take = 10

            page = request.GET.get('page', default_page)
            take = request.GET.get('take', default_take)

            try:
                page = int(page)
                take = int(take)
            except ValueError:
                return Response({"detail": "Os parâmetros 'page' e 'take' devem ser números inteiros."}, status=400)
            
            page = max(1, page)
            take = max(1, take)
            start_index = (page - 1) * take
            end_index = start_index + take

            #products = UserProduct.objects.filter(user_id=userId).order_by('-id').values()[:1]   
            products = UserProduct.objects.filter(user_id=userId).order_by('-id').values()                     

            results = products.values()[start_index:end_index]

            if not results:
                return []                               

            return results            
        
        except Exception as e:        
            raise e 
    

    
    def getProductByProductId(self, request, productId):
        try:            

            products = UserProduct.objects.filter(id=productId).order_by('-id').values()[:1]                                  

            results = products.values()

            if not results:
                raise ValidationError("Product Not Found", code=status.HTTP_404_NOT_FOUND)                                 

            return results[0]            
        
        except Exception as e:        
            raise e 
        
        
    def updatePatchProductByProductId(self, body, productId):
        userProduct = get_object_or_404(UserProduct, id=productId)

        productUpdated = UserProductSerializer(userProduct, data=body, partial=True)
        
        if productUpdated.is_valid():
            productUpdated.save()
            return productUpdated.data
        else:
            return productUpdated.errors
        

        
    def deleteProductsByProductIds(self, productsId, userId):
        user = get_object_or_404(User, id=userId)

        products = UserProduct.objects.filter(id__in=productsId)
        
        products.delete()

        return True