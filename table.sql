CREATE TABLE IF NOT EXISTS agrupado(
   fecha date PRIMARY KEY, 
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