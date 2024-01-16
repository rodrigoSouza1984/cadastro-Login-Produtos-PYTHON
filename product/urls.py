from django.urls import path
from product.api.viewsets import addProduct, getProductsByUserId, getProductByProductId, updatePatchProductByProductId, deleteProductsByProductIds


urlpatterns = [
    path("<int:userId>/", addProduct),     
    path("getProductsByUserId/<int:userId>/", getProductsByUserId),  
    path("getProductByProductId/<int:productId>/", getProductByProductId), 
    path("updatePatchProductByProductId/<int:productId>/", updatePatchProductByProductId), 
    path("deleteProductsByProductIds/<int:userId>/", deleteProductsByProductIds), 
    # Adicione mais rotas conforme necessário
]


