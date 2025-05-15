# app/user/api/serializers.py
#from rest_framework import serializers
from user.models import Usuario

#~class UsuarioSerializer(serializers.ModelSerializer):
#~    rol_display = serializers.CharField(source='get_rol_display', read_only=True)
#~    date_joined = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')
#~
#~    class Meta:
#~        model = Usuario
#~        fields = ['id', 'username', 'email', 'first_name', 'last_name', 
#~                 'rol', 'rol_display', 'date_joined']