# Data-Warehouse

Estos scripts permiten descargar información desde bases de datos, aplicar procesos de limpieza y transformación, y finalmente cargar los datos procesados en una nueva base de datos

Ejecute los scripts en el siguiente orden:

```
 python .\DBtoCSV.py
 python .\cleanCSV.py
 python .\noNulls.py
 python .\createCleanDB.py
```

Las siguientes carpetas se crearán automáticamente:

```
 DB-a-csv
 csv-depurado
 depurado-Sin_nulos
```
