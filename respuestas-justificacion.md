# Respuestas y justificación

## FRONT-END
1. **¿Cómo se lee el archivo que el usuario seleccionó en un <input type="file">?**
R./ El archivo que en este caso va a ser una imagen se lee con document.getElementById('imagen').files[0], la persona sube el archivo y con el id de 'imagen' esto captura solo la primera imagen(por eso el 0).

2. **Si ya manda el formulario con JSON.stringify(dataForm), ¿por qué eso no funciona para mandar un archivo?**
R./El atributo stringify no funciona en este caso porque json sirve para enviar datos de texto, y lo que necesitamos contiene una archivo que es la imagen. Aqui por eso usamos FormData que si acepta datos y archivos.

3. **¿Qué objeto de JavaScript se usa en su lugar para armar un cuerpo de petición que incluya archivos?**
R./ Usamos el FormData para capturar todos los campos incluida la imagen, se agregan a una const y luego se mandan al fetch.

4. **Cuando se manda ese objeto en el fetch, ¿hace falta seguir poniendo el header Content-Type: application/json?**
R./Ya no se necesita, al enviar FormData en el fetch, el navegador establece el formato correcto de formulario, en caso de que se ponga lo leera como json y como sabemos la imagen no es json, lo cual nos tirara error.

## BACK-END
1. **Cuando la petición trae un archivo, ¿en qué atributo del request llega ese archivo? (no es en request.body, que es donde leíamos el JSON hasta ahora).**
R./La imagen nos llegara a request.FILES, los demas campos se almacenan en request.POST

2. **Django necesita saber en qué carpeta del disco guardar los archivos, y con qué URL servirlos después. ¿Qué dos variables de settings.py controlan eso?**
R./Especificamente estas dos:
    `MEDIA_URL =  '/media/'` -> Este nos indica la URL donde se puede ver en el navegador.
    `MEDIA_ROOT= BASE_DIR / 'media'` -> Este nos indica en que direccion se guardan los archivos.

3. **Si guardan el archivo con las herramientas propias de Django (django.core.files.storage), ¿qué hace esa herramienta por ustedes que tendrían que programar a mano si lo hicieran con Python puro (abrir el archivo, generar un nombre, escribirlo en disco)?**
R./Django al tener su propia herramienta de gestion de guardado,  se encarga de guardar automaticamente en la ruta que nosotros le configuramos en MEDIA_ROOT, gestionar el nombre y guardar en el disco los archivos. Lo cual a nosotros nos tomaria mas tiempo si lo hicieramos manualmente.

4. **Una vez guardada la imagen, ¿qué dato exacto conviene guardar en la fila de la base de datos: la ruta completa del archivo en el disco del servidor, o una ruta relativa? ¿Por qué la respuesta importa si algún día cambian de servidor?**
R./ Es mejor la ruta relativa del archivo, porque los servidores pueden cambiar de ruta en el disco, entonces con la relativa siempre sera la misma asi hagamos las migraciones que sean. No se depende de la ruta especifica del computador.