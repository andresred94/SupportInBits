from django.contrib.auth import get_user_model
User = get_user_model()

# Listar todos los usuarios
usuarios = User.objects.all()
for usuario in usuarios:
    print(f"ID: {usuario.id}, Username: {usuario.username}, Email: {usuario.email}, Rol: {usuario.rol}")

# Contar usuarios registrados
print(f"\nTotal de usuarios registrados: {User.objects.count()}")

######################################################################
# Ver permisos para un modelo específico
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from user.models import Usuario

content_type = ContentType.objects.get_for_model(Usuario)
permisos = Permission.objects.filter(content_type=content_type)

print(f"Permisos disponibles para {Usuario.__name__}:")
for perm in permisos:
    print(f"- {perm.codename}: {perm.name}")

######################################################################

from django.contrib.auth import get_user_model
User = get_user_model()

# Obtener un usuario específico
usuario = User.objects.get(username='neo')

# Verificar si es superusuario
print(f"¿Es superusuario? {usuario.is_superuser}")

# Verificar si es staff
print(f"¿Es staff? {usuario.is_staff}")

# Ver todos los permisos directos
print("Permisos directos:")
for perm in usuario.user_permissions.all():
    print(perm.codename)

# Ver todos los permisos (incluyendo los de grupos)
print("\nTodos los permisos (incluyendo grupos):")
for perm in usuario.get_all_permissions():
    print(perm)