# Data-Warehouse Grupo 2

### Integrantes:

-Esquivel Luis <br />
-Montoya Uveda María <br />
-Navarro Chaves María José <br />
-Orozco Rojas Bryan <br />
-Vargas Vásquez Kennia <br />

### Profesor:

Ing. Marvin Solano Campos

### II CUATRIMESTRE 2023

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

Recuerda instalar lo siguiente:

```
pip install pyodbc
```

**debes crear una BD en blanco llamada: ProyectoGrupo2Depurado**

**El archivo .bak original está incluido en este repositorio.**
