# Sistema de Gestión Empresarial

## Descripción del proyecto

La empresa de desarrollo de software realiza una reunión con el equipo, con la finalidad de organizar un primer sprint para simular la fabricación de productos farmacéuticos.

Las tecnologías y herramientas ocupadas son las siguientes:
- Python
- Django
- PostgreSQL
- Bootstrap

## Consideraciones

- Las empresas de laboratorio farmacéuticos pueden realizar varios productos, y a su vez, ésta posee un director general que no puede pertenecer a otro laboratorio.
- Se pueden crear nuevos laboratorios.
-  Realice pruebas unitarias al modelo Laboratorio, donde se verifique:
1. Que los datos en nuestra base de datos simulada coincidan con los que se crearon inicialmente en setUpTestData para un laboratorio dado.
2. La URL para confirmar que devuelve una respuesta HTTP 200 para laboratorio.
3. Que la página usando reverse para llamar al nombre de la URL, busca una respuesta HTTP 200, verifica que se use la plantilla correcta, y confirma que el contenido HTML coincide con lo esperado.

## Instalación 🚀

Estas instrucciones te permitirán obtener una copia del proyecto en funcionamiento en tu máquina local para propósitos de desarrollo y pruebas.

### Pre-requisitos 📋

Que cosas necesitas para instalar el software.

```
Visual Studio Code, Node, Git, Github
```

## Instrucciones para crear la Base de Datos 

Se debe persistir la información de los usuarios en PostgreSQL, por lo que deberás usar las siguientes sentencias SQL para la creación de la base de datos y la tabla de participantes.

## Instrucciones para crear la base de datos

Abrir PG Admin
   - Acceder con el usuario y contraseña de administrador.
   - Crear un nuevo usuario: 
     ```sql
     CREATE USER userdjango WITH PASSWORD 'userdjango';
     ```
   - Crear una nueva base de datos llamada 'django_laboratorio', asignando el usuario 'userdjango'.

### Instalación 🔧
Realizar un fork o clon del proyecto.
Importar proyecto al IDE de preferencia para ejecutar.
Para ejecutar en consola realizar el build (empaquetado) de la aplicación.

```bash
git clone https://github.com/VictorPenafiel/Django_Laboratorio.git
cd proyecto
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## Construido con 🛠️

* [Python](https://www.python.org/django)
* [Visual Studio Code](https://code.visualstudio.com/)
* [Git](https://git-scm.com/)
* [GitHub](https://github.com/)

## Contribuye 🖇️

```bash
# Fork → Crea rama → Cambios → Commit → Pull Request
```

## Autores ✒️

https://github.com/victorpenafiel

## Licencia 📄

Ningún Derecho Reservado.  [Creative Commons Atribución/Reconocimiento 4.0 ](https://creativecommons.org/licenses/by/4.0/deed.es).

Este proyecto está bajo la Licencia - mira el archivo [LICENSE.md](LICENSE.md) para detalles