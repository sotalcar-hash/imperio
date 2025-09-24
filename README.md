
Tipster Dashboard — Instrucciones de despliegue en Streamlit Cloud

He preparado una aplicación minimal para que tengas un dashboard online accesible desde cualquier sitio. Descarga el ZIP, descomprímelo y sube los archivos a GitHub (o usa la interfaz web de GitHub para subirlos). El repositorio debe tener al menos estos archivos en la raíz: app.py y requirements.txt.

Si no tienes cuenta en GitHub, créate una en https://github.com con tu correo. Es gratuito. Una vez dentro crea un nuevo repositorio (puede ser privado o público). Puedes crear el repo con la opción "Add file -> Upload files" y subir los archivos extraídos del ZIP.

Una vez los archivos estén en GitHub, ve a https://streamlit.io/cloud y accede con tu cuenta de GitHub (usa "Sign in with GitHub"). Después en Streamlit Cloud haz "New app", selecciona el repositorio que acabas de crear, branch 'main' (o el que uses) y el path al archivo principal: app.py. Pulsa "Deploy app". En unos segundos tendrás una URL pública que puedes compartir con otra persona.

Nota sobre uso por dos personas: la app es accesible por URL desde dos ubicaciones al mismo tiempo, pero la "Situación Actual" no se sincroniza automáticamente entre sesiones de usuario. Si necesitas sincronización en tiempo real del valor de "Situación Actual", puedo añadir integración con Google Sheets para que ambos veáis y editéis la misma fuente. Eso requiere crear credenciales de Google (te guiaré paso a paso) o darme acceso a la hoja compartida.

Si prefieres que yo prepare el repositorio en GitHub por ti, tengo que recibir acceso a una cuenta o a un repositorio donde pueda hacer commit; si no quieres eso, los pasos anteriores son los mínimos que debes ejecutar. 

Cambios futuros: si quieres que guarde tu histórico de apuestas o exporte un CSV, lo añado sin problema.