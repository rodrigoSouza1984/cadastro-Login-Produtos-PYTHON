from rest_framework.serializers import ModelSerializer, ValidationError
from user.models import User
from django.contrib.auth.hashers import make_password

from django.http import Http404

from django.forms.models import model_to_dict

from django.shortcuts import get_object_or_404, get_list_or_404

from rest_framework.response import Response


class UserSerializer(ModelSerializer):    
    class Meta:
        model = User
        fields = ('id', 'name', 'username', 'email', 'password', 'age', 'ownerApp', 'height', 'weight')                        
        

    def create(self, body):        
                
        if 'name' not in body:
            raise ValidationError("Name is required")
            
        if 'email' not in body:
            raise ValidationError("email is required")
        
        if '@' not in body['email']:
            raise ValidationError("Email Invalid'")

        if 'password' not in body:
            raise ValidationError("password is required")
        
        body['password'] = make_password(body['password'])

        user = User.objects.create(**body)        

        return user 
     

    def getUsers(self, request):
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

            users = User.objects.prefetch_related('products', 'avatar').all()[start_index:end_index]
            
            usersToReturn = []

            for user in users:
                avatar_info = None

                if hasattr(user, 'products'):
                    # O usuário tem produtos, você pode acessá-los usando user.products.all()
                    products_info = [
                        {
                            'product_id': product.id,
                            'product_title': product.title,
                            'product_url': product.url,
                            'product_price': product.price,
                            'product_quantity': product.quantity,
                            # Adicione outros campos do produto conforme necessário
                        }
                        for product in user.products.all()
                    ]
                else:
                    # O usuário não tem produtos
                    products_info = None

                

                if hasattr(user, 'avatar') and user.avatar is not None:
                    if hasattr(user, 'avatar') and user.avatar is not None:                        
                        avatar_info = {
                            'avatar_id': user.avatar.id,
                            'avatar_name': user.avatar.name,
                            'avatar_url': user.avatar.url,
                            'mimetype': user.avatar.mimetype
                            # Adicione outros campos do avatar conforme necessário
                        }                    
                    else:                        
                        avatar_info = None               
                

                userData = {
                        'id': user.id,
                        'username': user.username,
                        'name': user.name,
                        'username': user.username,
                        'email': user.email,
                        'age': user.age,
                        'ownerApp': user.ownerApp,
                        'height': user.height,
                        'weight': user.weight,                        

                        'avatar': avatar_info,

                        'products': products_info
                    }

                usersToReturn.append(userData)                    

            return usersToReturn
                   
        except Exception as e:        
            raise e 


    def getUserById(self, userId):
        try:
            user= get_object_or_404(User.objects.prefetch_related('products').select_related('avatar'), id=userId)                          
                
            if user:
                                        
                #products_list = user_with_products.products.all()

                if hasattr(user, 'avatar') and user.avatar is not None:
                    avatar_info = {
                        'avatar_id': user.avatar.id,
                        'avatar_name': user.avatar.name,
                        'avatar_url': user.avatar.url,
                        'mimetype': user.avatar.mimetype
                        # Adicione outros campos do avatar conforme necessário
                }                    
                else:
                    avatar_info = None 

                if hasattr(user, 'products'):
                    # O usuário tem produtos, você pode acessá-los usando user.products.all()
                    products_info = [
                        {
                            'product_id': product.id,
                            'product_title': product.title,
                            'product_url': product.url,
                            'product_price': product.price,
                            'product_quantity': product.quantity,
                            # Adicione outros campos do produto conforme necessário
                        }
                        for product in user.products.all()
                    ]
                else:
                    # O usuário não tem produtos
                    products_info = None                                  

                response_data = {
                    'user': {
                                'id': user.id ,
                                'username': user.username,
                                'name': user.name,
                                'username': user.username,
                                'email': user.email,
                                'age': user.age,
                                'ownerApp': user.ownerApp,
                                'height': user.height,
                                'weight': user.weight,
                                # Adicione outros campos do usuário conforme necessário

                                
                                'avatar': avatar_info,   

                                'products': products_info                             
                            },                           
                }                            
            else:
                print("Usuário não encontrado.")

            return response_data     
                   

        except Exception as e:        
            raise e


    def getUserByEmail(self, email):
        try:            
            
            user = User.objects.get(email=email)

            userCovertedDicionary = model_to_dict(user)

            return userCovertedDicionary
        
        except User.DoesNotExist:            
            raise Http404("User does not exist")
           

    def updatePatchUserById(self, body, userId):
        user = get_object_or_404(User, id=userId)
        userUpdated = UserSerializer(user, data=body, partial=True)
        
        if userUpdated.is_valid():
            userUpdated.save()
            return userUpdated.data
        else:
            return userUpdated.errors
         
    
    def updatePutUserById(self, body, userId):
        user = get_object_or_404(User, id=userId)
        userUpdated = UserSerializer(user, data=body)
        
        if userUpdated.is_valid():
            userUpdated.save()
            return userUpdated.data
        else:
            return userUpdated.errors
 
    
    def deleteUserByIds(self, userIds, userId):
        user = get_object_or_404(User, id=userId)

        users = User.objects.filter(id__in=userIds)
        
        users.delete()

        return True