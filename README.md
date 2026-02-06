# CDE Documento Maestro - Sitio estático

Este repositorio contiene el sitio web estático para presentar el **Documento Maestro Definitivo**
(Sistema web privado para lectura de desprendibles de pago y cálculo de CDE).

## Cómo ejecutar el sitio

Requiere Python 3 instalado.

```bash
python server.py
```

Luego abre en tu navegador:

```
http://localhost:8000/index.html
```

## Despliegue en Render

El archivo `render.yaml` configura el despliegue automático como servicio web en Render.
Si ves un **503 Service Unavailable**, verifica que el servicio esté activo y que el
comando de inicio sea `python server.py`.

Si Render muestra el error `Could not open requirements file`, el script
`render-build.sh` crea automáticamente un `requirements.txt` vacío antes de instalar
dependencias. También confirma que el servicio esté apuntando al `rootDir` correcto (`.`).

## Archivos principales

- `index.html`: contenido del documento en formato web.
- `styles.css`: estilos del sitio.
- `server.py`: servidor local para previsualización.
- `render.yaml`: configuración de despliegue en Render.
- `requirements.txt`: archivo requerido por Render durante el build.
- `render-build.sh`: script de build para Render (crea requirements.txt si falta).
