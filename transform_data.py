import logging
import pandas as pd

def transform (data_downloaded):

    list_save =[data_downloaded[0][0],data_downloaded[0][1],data_downloaded[0][2]]
    fecha = data_downloaded[1]
    df1 = pd.read_csv(list_save[0])

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

    df_m = df1[list_columns].assign(fecha=fecha)

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
            'Teléfono':'número de teléfono',
            'Mail':'mail',
            'Web':'web',
            }
    df2.rename(columns = rename_columns, inplace=True)

    df_c = df2[list_columns].assign(fecha=fecha)

    df3 = pd.read_csv(list_save[2])

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

    df_b = df3[list_columns].assign(fecha=fecha)

    df_table = pd.concat([df_m,df_b,df_c])

    group_list = {0:['categoría'], 1:['provincia','categoría']}
    df_total_category = []

    # categories and province count Dataframes
    for i, category in group_list.items(): 
        freq = df_table.groupby(category,as_index= False).size().assign(fecha=fecha)
        df_total_category.append(freq) 
        

    # source count and cine result Dataframes
    tot_source = {'Museo': df_m.size, 'Biblioteca':df_b.size , 'Cine':df_c.size }
    table_total_source = pd.DataFrame(tot_source.items(), columns = ['source', 'cantidad']).assign(fecha=fecha)
    cine_columns = ['provincia','Pantallas', 'Butacas', 'espacio_INCAA']
    df_cine_total = df2.groupby(['provincia'], as_index = False).count()[cine_columns].assign(fecha=fecha)
    logging.info('Data Transformation success')

    return [df_table, df_cine_total,df_total_category, table_total_source]
