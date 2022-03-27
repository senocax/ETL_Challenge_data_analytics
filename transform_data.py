import pandas as pd
from extraction_data import list_save 

df1 = pd.read_csv(list_save[0])
df1.columns
rename_columns = {'Cod_Loc':'cod_localidad',
         'IdProvincia':'id_provincia',
         'IdDepartamento':'id_departamento',
         'categoria': 'categoría',
         'Localidad':'localidad',
         'Nombre':'nombre',
         'direccion':'domicilio',
         'CP':'código postal',
         'telefono':'número de teléfono',
         'Mail':'mail',
         'Web':'web',
          }
df1.rename(columns = rename_columns, inplace=True)

list_columns = ['cod_localidad', 'id_provincia', 'id_departamento',
                'categoría','provincia' ,'localidad', 'nombre', 'domicilio',
                'código postal','número de teléfono', 'mail', 'web']

df_m = df1[list_columns]

df2 = pd.read_csv(list_save[1])
rename_columns = {'Cod_Loc':'cod_localidad',
         'IdProvincia':'id_provincia',
         'IdDepartamento':'id_departamento',
         'Categoría': 'categoría',
         'Localidad':'localidad',
         'Nombre':'nombre',
         'Provincia':'provincia',
         'Dirección':'domicilio',
         'CP':'código postal',
         'Fuente':'fuente',
         'Teléfono':'número de teléfono',
         'Mail':'mail',
         'Web':'web',
          }
df2.rename(columns = rename_columns, inplace=True)


list_columns = ['cod_localidad', 'id_provincia', 'id_departamento',
                'categoría','provincia' ,'localidad', 'fuente', 'nombre', 'domicilio',
                'código postal','número de teléfono', 'mail', 'web','Pantallas', 'Butacas' , 'espacio_INCAA']
df_c = df2[list_columns]

df3 = pd.read_csv(list_save[2])
df3.columns
rename_columns = {'Cod_Loc':'cod_localidad',
         'IdProvincia':'id_provincia',
         'IdDepartamento':'id_departamento',
         'Categoría': 'categoría',
         'Localidad':'localidad',
         'Nombre':'nombre',
         'Provincia':'provincia',
         'Domicilio':'domicilio',
         'CP':'código postal',
         'Teléfono':'número de teléfono',
         'Mail':'mail',
         'Web':'web',
          }

df3.rename(columns = rename_columns, inplace=True)

list_columns = ['cod_localidad', 'id_provincia', 'id_departamento',
                'categoría','provincia' ,'localidad', 'nombre', 'domicilio',
                'código postal','número de teléfono', 'mail', 'web']

df_b = df3[list_columns]

df_table = pd.concat([df_m,df_b,df_c])

group_list = {0:['categoría'], 1:['provincia','categoría']}
df_total_category = []

# procesamiento categorias
for i, category in group_list.items(): 
    freq = df_table.groupby(category,as_index= False).size() 
    df_total_category.append(freq) 
 

df_total_category[0]
df_total_category[1]

# cantidad por fuente
tot_source = {'Museo': df_m.size, 'Biblioteca':df_b.size , 'Cine':df_c.size }
pd.DataFrame(tot_source.items(), columns = ['source', 'count'])
# procesamiento cine
cine_columns = ['provincia','Pantallas', 'Butacas', 'espacio_INCAA']

#df_cine_total
df_c.groupby(['provincia'], as_index = False).count()[cine_columns]
print(df_c)
#df_cine_total
