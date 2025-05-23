# Actualizador de precios para emprendimiento

Este proyecto permite obtener automáticamente los precios de insumos (por ejemplo, cera de soja) desde la página del proveedor y actualizarlos en una hoja de cálculo de Google Sheets.

## Funcionalidades

- Web scraping con Selenium para obtener precios actualizados.
- Uso de archivo `.env` para gestionar configuraciones.
- Posibilidad de integración con Google Sheets.

## Requisitos

Ver `requirements.txt`.

## Uso

1. Crear el archivo `.env` con las variables necesarias.
2. Ejecutar el script principal:

```bash
python src/actualizar_precio.py
