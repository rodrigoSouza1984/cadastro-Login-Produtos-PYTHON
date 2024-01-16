from rest_framework.viewsets import ModelViewSet
from product.models import UserProduct
from .serializers import UserProductSerializer

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated

class UserAvatarViewSet(ModelViewSet):
    queryset = UserProduct.objects.all()
    serializer_class = UserProductSerializer 
    
# cria um objeto de cada vez
# @api_view(['POST'])
# #@permission_classes([IsAuthenticated])
# def addProduct(request, userId):
    
#     if request.method == 'POST':               
#         serializer = UserProductSerializer(data=request.data)
#         if serializer.is_valid():            
#             serializer.addProduct(serializer.validated_data, userId)
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['POST'])
#@permission_classes([IsAuthenticated])
def addProduct(request, userId):
    if request.method == 'POST':        
        serialized_products = []
        # Iterar sobre cada produto nos dados recebidos
        for product_data in request.data:
            # Serializar o produto individualmente
            serializer = UserProductSerializer(data=product_data)
            if serializer.is_valid():
                # Adicionar o produto serializado à lista
                serialized_products.append(serializer.data)
            else:
                # Se houver erros de validação, retorne os erros
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)        
        
        productsCreateds = serializer.addProduct(serialized_products, userId)
        return Response(productsCreateds, status=status.HTTP_201_CREATED)
    
@api_view(['GET'])
def getProductsByUserId(request, userId): 
    print('aaaa')   
    if request.method == 'GET':
        serializer = UserProductSerializer()
        users = serializer.getProductsByUserId(request, userId)
        return Response(users, status=status.HTTP_200_OK)
    
    

@api_view(['GET'])
def getProductByProductId(request, productId): 
    print('aaaa')   
    if request.method == 'GET':
        serializer = UserProductSerializer()
        users = serializer.getProductByProductId(request, productId)
        return Response(users, status=status.HTTP_200_OK)
    

@api_view(['PATCH'])
def updatePatchProductByProductId(request, productId):
    if request.method == 'PATCH':

        serializer = UserProductSerializer()
        product = serializer.updatePatchProductByProductId(request.data, productId) 

    if isinstance(product, dict):  
        return Response(product, status=status.HTTP_200_OK)
    else:
        return Response(product, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['DELETE'])
def deleteProductsByProductIds(request, userId):
    if request.method == 'DELETE':
        serializer = UserProductSerializer()
        productsId = request.data
        
        if not productsId:
            return Response({"detail": "Nenhum ID de usuário fornecido para exclusão."}, status=status.HTTP_400_BAD_REQUEST)
                
        serializer.deleteProductsByProductIds(productsId, userId)

        return Response(status=status.HTTP_204_NO_CONTENT)