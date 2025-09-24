Sotalcalcular — versión corregida (mínima CSS)

Motivo del cambio:
- Se eliminaron estilos agresivos que podían interferir con los inputs de Streamlit y provocar que los campos no fueran editables.
- Esta versión usa solo CSS seguro (botones y métricas) y mantiene la lógica previa.

Instrucciones (muy sencillas):
1. Descarga este ZIP y descomprímelo.
2. Entra en tu repositorio en GitHub.
3. Pulsa "Add file" -> "Upload files". Arrastra `app.py` y `requirements.txt` y confirma con "Commit changes". Acepta reemplazar app.py si se te pide.
4. En Streamlit Cloud selecciona tu app y fuerza un "Rerun" o espera a que detecte el commit y se redepliegue.
5. Si sigues viendo el error `TypeError: error loading dynamically imported module`, prueba estos pasos:
   - Pulsa "Rerun" en Streamlit Cloud.
   - Abre la app en modo incógnito o limpia la caché del navegador (Ctrl/Cmd+Shift+R).
   - Revisa los Logs de la app en Streamlit Cloud (tres puntos -> Logs) y copia el mensaje si persiste.
   - Si el problema continúa, dime y yo investigo el log y lo soluciono.

Si quieres que añada el estilo neomórfico con seguridad (sin romper inputs), lo implemento progresivamente en pequeñas iteraciones y te doy el ZIP listo para subir.
