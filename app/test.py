from django.contrib.auth.models import User

# Obtener todos los usuarios
usuarios = User.objects.all()

# Mostrar usernames
for usuario in usuarios:
    print(f"ID: {usuario.id}, Username: {usuario.username}, Email: {usuario.email}, Superusuario: {usuario.is_superuser}")