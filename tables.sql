CREATE TABLE IF NOT EXISTS table_principal(
   fecha INTEGER PRIMARY KEY, 
   cod_localidad INTEGER NOT NULL,
   id_provincia INTEGER NOT NULL,
   id_departamento INTEGER NOT NULL,
   categoría VARCHAR(255) NOT NULL ,
   provincia VARCHAR(255) NOT NULL,
   localidad VARCHAR(255) NOT NULL,
   nombre VARCHAR(255) NOT NULL,
   domicilio VARCHAR(255) NOT NULL,
   código VARCHAR(255) NOT NULL,
   número VARCHAR(255) NOT NULL,
   mail VARCHAR(255) NOT NULL,
   web VARCHAR(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS table_category(
   fecha date PRIMARY KEY, 
   categoría VARCHAR(255) NOT NULL ,
   size VARCHAR(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS table_province_category(
   fecha date PRIMARY KEY, 
   provincia VARCHAR(255) NOT NULL ,
   categoría VARCHAR(255) NOT NULL ,
   size VARCHAR(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS cine_result(
   fecha date PRIMARY KEY, 
   provincia VARCHAR(255) NOT NULL ,
   Pantallas VARCHAR(255) NOT NULL ,
   Butacas VARCHAR(255) NOT NULL,
   Espacio_INCAA VARCHAR(255) NOT NULL 
);

CREATE TABLE IF NOT EXISTS table_source(
   fecha date PRIMARY KEY, 
   source VARCHAR(255) NOT NULL ,
   cantidad VARCHAR(255) NOT NULL 
);