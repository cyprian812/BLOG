from dj_rest_auth.registration.views import RegisterView
# from rest_framework.response import Response
# from rest_framework.permissions import BasePermission
# from rest_framework.permissions import IsAdminUser
from.serializers import RegisterSerializer
class registerview(RegisterView):
    serializer_class= RegisterSerializer

    # def get(self, request):
    #     return Response({"message": "This is admin data accessible to admin users only"})

# class isstaff(RegisterView):
#     permission_classes=[isstaff]
    
#     def get(self, request):
#         # Your view logic here
#        return Response({"message": "This is staff data accessible to staff users only"})