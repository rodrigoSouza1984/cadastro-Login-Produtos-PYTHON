from rest_framework.serializers import ModelSerializer, ValidationError
from user.models import User
from django.contrib.auth.hashers import make_password

from userAvatar.models import UserAvatar
from product.models import UserProduct

from django.http import Http404

from django.forms.models import model_to_dict

from django.shortcuts import get_object_or_404

from rest_framework.response import Response

from rest_framework import status




from django.db.models import Subquery, OuterRef, Func, CharField, Subquery, OuterRef


class UserSerializer(ModelSerializer):    
    class Meta:
        model = User
        fields = '__all__'                        
        

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
    

    # def getUsers(self, request):
    #     try:

    #         default_page = 1
    #         default_take = 10

    #         page = request.GET.get('page', default_page)
    #         take = request.GET.get('take', default_take)

    #         try:
    #             page = int(page)
    #             take = int(take)
    #         except ValueError:
    #             return Response({"detail": "Os parâmetros 'page' e 'take' devem ser números inteiros."}, status=400)
            
    #         page = max(1, page)
    #         take = max(1, take)
    #         start_index = (page - 1) * take
    #         end_index = start_index + take

    #         avatar_subquery = UserAvatar.objects.filter(user=OuterRef('pk')).order_by('-id').values()[:1]

    #         queryset = User.objects.annotate(
    #             avatar_id=Subquery(avatar_subquery.values('id')),
    #             avatar_name=Subquery(avatar_subquery.values('name')),
    #             avatar_mimetype=Subquery(avatar_subquery.values('mimetype')),
    #             avatar_url=Subquery(avatar_subquery.values('url'))
    #         )            

    #         results = queryset.values()[start_index:end_index]

    #         if not results:
    #             return []                

    #         for result in results:                
    #             if result['avatar_id'] is not None:
    #                 result['avatar'] = {
    #                     'id': result['avatar_id'],
    #                     'name': result['avatar_name'],
    #                     'url': result['avatar_url'],
    #                     'mimetype': result['avatar_mimetype'],
    #                 }

    #             else:                
    #                 result['avatar'] = None

    #             del result['password']    
    #             del result['avatar_id']
    #             del result['avatar_name']
    #             del result['avatar_url']
    #             del result['avatar_mimetype']                           

    #         return results            
        
    #     except Exception as e:        
    #         raise e 
     




    def getUsers(self, request):
        try:

            
            user_with_products = get_object_or_404(User.objects.prefetch_related('products').select_related('avatar'), id=4)  


            
            if user_with_products:
                #avatar = user_with_products.avatar()

                print(user_with_products.avatar, 8888)
                products_list = user_with_products.products.all()

                response_data = {
                    'user': {
                        'id': user_with_products.id,
                        'username': user_with_products.username,
                        'name': user_with_products.name,
                        # Adicione outros campos do usuário conforme necessário

                        'avatar': {
                            'id': user_with_products.avatar.id,
                            'name': user_with_products.avatar.name,                            
                            'url':  user_with_products.avatar.url,                            
                            'mimetype': user_with_products.avatar.mimetype,                            
                            # Adicione outros campos do avatar conforme necessário
                        },

                        'products': [
                            {
                                'id': product.id,
                                'title': product.title,
                                'url': product.url,
                                'price': product.price,
                                'quantity': product.quantity,
                                # Adicione outros campos do produto conforme necessário
                            }
                            for product in products_list
                        ],
                    },

                    
                }
                print(response_data)

                return response_data
            else:
                print("Usuário não encontrado.")

            return True

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

            avatar_subquery = UserAvatar.objects.filter(user=OuterRef('pk')).order_by('-id').values()[:1]

            queryset = User.objects.annotate(
                avatar_id=Subquery(avatar_subquery.values('id')),
                avatar_name=Subquery(avatar_subquery.values('name')),
                avatar_mimetype=Subquery(avatar_subquery.values('mimetype')),
                avatar_url=Subquery(avatar_subquery.values('url'))
            )            

            results = queryset.values()[start_index:end_index]

            if not results:
                return []                

            for result in results:                
                if result['avatar_id'] is not None:
                    result['avatar'] = {
                        'id': result['avatar_id'],
                        'name': result['avatar_name'],
                        'url': result['avatar_url'],
                        'mimetype': result['avatar_mimetype'],
                    }

                else:                
                    result['avatar'] = None

                del result['password']    
                del result['avatar_id']
                del result['avatar_name']
                del result['avatar_url']
                del result['avatar_mimetype']                           

            return results            
        
        except Exception as e:        
            raise e 
   







    def getUserById(self, userId):
        try:
            avatar_subquery = UserAvatar.objects.filter(user=OuterRef('pk')).order_by('-id').values()[:1]#mais de 1 resultado tirar [:1]               

            queryset = User.objects.annotate(
                avatar_id=Subquery(avatar_subquery.values('id')),
                avatar_name=Subquery(avatar_subquery.values('name')),
                avatar_mimetype=Subquery(avatar_subquery.values('mimetype')),
                avatar_url=Subquery(avatar_subquery.values('url'))
            )

            queryset = queryset.filter(id=userId)
           
            result = queryset.values().first()  

            if result is None:
                raise ValidationError("User Not Found", code=status.HTTP_404_NOT_FOUND)          

            if result['avatar_id'] is not None:
                result['avatar'] = {
                        'id': result['avatar_id'],
                        'name': result['avatar_name'],
                        'url': result['avatar_url'],
                        'mimetype': result['avatar_mimetype'],
                    }
            else:                
                result['avatar'] = None

            del result['password'] 
            del result['avatar_id']
            del result['avatar_name']
            del result['avatar_url']
            del result['avatar_mimetype']              

            return result         

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