# app/user/api/views.py (versión mejorada)
# from rest_framework import generics, permissions
# from rest_framework.response import Response
# from user.models import Usuario
# from .serializers import UsuarioSerializer

# class UsuarioListView(generics.ListAPIView):
#     serializer_class = UsuarioSerializer
#     permission_classes = [permissions.IsAdminUser]
# 
#     def get_queryset(self):
#         return Usuario.objects.all().order_by('id')
# 
#     def list(self, request, *args, **kwargs):
#         # Para depuración: verifica si el usuario es admin
#         if not request.user.is_authenticated or not (request.user.rol == 'administrador' or request.user.is_superuser):
#             return Response({"error": "No autorizado"}, status=403)
#         
#         queryset = self.get_queryset()
#         serializer = self.get_serializer(queryset, many=True)
#         
#         # Agrega esta línea para depuración
#         # print("Usuarios enviados por la API:", serializer.data)
#         
#         return Response(serializer.data)