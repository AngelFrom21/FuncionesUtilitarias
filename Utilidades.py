#           Funciones utilitarias
#funciones miscelaneas en procesamiento de datos:

#1. Null pinger:
"""

busca valores que representen a los valores nulos dentro d un dataset, puede configurarse para funcionar
en todas o solo en algunas columnas, por defecto funciona comparando el tipo del dato y probando si es posible
convertirlo de str a float, para columnas numéricas los valores se añaden a una lista, errs.

Es posible sustituir la secuencia if-else mediante to_numeric de pandas, esto convierte directamente esos valores en NaN


"""

def null_pinger(df: pd.DataFrame):
  errs = []
  for columna in df.columns[6:]:
    for elemento in df[columna]:
      if type(elemento) is str and elemento not in errs and len(elemento)<4:
        try:
          float(elemento)
        except:
          errs.append(elemento)
      else:
        continue
  return errs
  
#version alternativa la cual elimina el valor nulo y lo sustituye drectamente por NaN

"""
nota: esta función alternativa funciona solo para columnas de valores numéricos, si se usa en una columna de otro tipo
esa columna sera convertida toda a NaN

"""

def column2numeric(df: pd.DataFrame):
    for col in df.columns[0:]:
        df[col] = pd.to_numeric(df[col], errors = 'coerce')
        return df



#2 carga de datos 'CSV':

"""
funcion que permite leer datos de un archivo csv, se puede establecer un header mediante un indice de entrada,
se puede recortar un segmento del conjunto mediante skiprows,
los valores nulos, si se sabe cuales son pueden ser convertidos a NaN con na_values.

en caso de que el lector diera error al leer un archivo csv, se debe añadir:

#           encoding = 'latin-1'


"""


def dtaaChargeCSV(x: str, hdr: int, si_a: int, si_b: int, naval: list):
    data = pd.read_csv('x', header = hdr, skiprows = [y for y in range(si_a,si_b)], na_valuea = naval)
    return data
    


#3 carga de datos desde excel:

"""

lo mismo que la función anterior pero ahora para excel, se debe proporcionar el nombre de la hoja cuando el archivo
contenga más de una

"""

def dataChargeXCel(sh: str):
    data = pd.read_excel(sh, sheet_name = '')
    return data
    
    
#               Funciones para visualización: MATPLOTLIB

#para una estructura de datos tipo df:

#4 gráfico básico:

def b_plot(x,y,plotName: str, xlabel: str, ylabel: str):
  plt.plot(x,y)
  plt.title(plotName)
  plt.xlabel(xlabel)
  plt.ylabel(ylabel)
  return plt.show()
  
  
#5 multiples gráficos en una celda:

def m_Plot(x1,x2,y1,y2, plotName: str, xlabel: str, ylabe: str):
    
  plt.plot(x1,y1, label='data1', ls = '--', color = 'red')
  plt.plot(x2,y2, label='data2')
  
  plt.legend()
  
  
  plt.title(plotName)
  plt.xlabel(xlabel)
  plt.ylabel(ylabel)
  
  return plt.show()
  
  
#6 gráfico comparativo usando figure y subplot:

def c_Plot(x1,x2,y1,y2, plotName: str):
    
  plt.figure(figsize=(9,3))
  
  
  plt.subplot(1,2,1)
  plt.plot(x1,y1, label='experimento 1', ls = '--', color = 'red')

  plt.xlabel('time [s]')
  plt.ylabel('pH')
  plt.legend()

  plt.subplot(1,2,2)
  plt.scatter(x2,y2, label = 'experimento 2', color = 'green')

  plt.xlabel('time [s]')
  plt.legend()


  plt.suptitle(plotName)
  return plt.show()
  
#7 gráfico con mapa de calor:

"""

el siguiente gráfico de tipo scatter permite visualizar la información mediante un mapa de calor, los argumentos
se pueden modificar, sus significados en este caso son:

    lon: es el eje x, en la función base es la longitud 
    lat: es el eje y, en la función original es la latitud.
    alp: es el argumento de contraste y transparencia de los puntos, permite ver mejor los puntos en el gráfico.
    s: es el radio de los puntos, se puede ajustar a una columna o función.
    c: el color de los puntos, puede ser una columna o función, pero debe ser un iterable o str.
    cmap: es el tipo de gradiente de color, es un str que puede cambiarse, existen varios, se encuentran en:
        https://matplotlib.org/stable/gallery/color/colormap_reference.html
    plt.colorbar(): muestra la escala de color y su valor segun los argumentos proporcionados.

"""
  
def dataInsight(lon: pd.DataFrame, lat: pd.DataFrame, alp: float, char: str, df: pd.DataFrame):
  plt.scatter(lon,lat,alpha = alp, s = 25, #s = df['pobtot']/250
              c = df[char],
              cmap = 'jet')
  plt.title('Mapa del estado')
  plt.colorbar()
  return plt.show()

#8 gráfico comparativo mediante mapa de calor:

"""

lo mismo que lo anterior pero ahora usando un gráfico multiple con figure y subplot,
en este caso un subplot de 1 renglon x 2 columnas, esta es la versión generalizada, dondé:
    
    x: el eje x que es de tipo pd.DataFrame.
    y: el eje y, lo mismo que en x.
    char: es la característica que se desea visualizar.

"""

def hmap_Insight(x: pd.DataFrame, y: pd.DataFrame, char: str, xl: str, yl: str):
  plt.figure(figsize=(9,3))
  
  
  plt.subplot(1,2,1)
  plt.scatter(
      df[x],
      df[y],
      alpha = 0.5,
      s = 25,
  )
  plt.xlabel(xl)
  plt.ylabel(yl)
  
  
  plt.subplot(1,2,2)
  plt.scatter(
      df[x],
      df[y],
      alpha = 0.5,
      s = 25,
      c = df[char],
      cmap = 'jet'
  )
  plt.xlabel(xl)
  #plt.ylabel('latitud')
  
  
  plt.colorbar()
  plt.suptitle('Comparativa')
  return plt.show()
  
  
#funciones para dar formato a str:

def coordFormatterLONG(x):
  if type(x) is str:
    x = x.replace('°','')
    x = x.replace('W', '')
    x = x.replace(' ','')
    x = x.replace('"','')
    x = x.replace("'","")
  else:
    pass
  return float(x)


#9 matriz de correlacion para columnas

"""

la función obtiene la matriz de correlacion entre las columnas de tipo numéricas, por lo que se deberá aplicar
solo a aquellas columnas de este tipo

"""


def lr_corr(df: pd.DataFrame, corr_col: str):
    corr_matrix = df.corr(numeric_only = True)
    local_corr = corr_matrix[corr_col]
    pCorr = local_corr[local_corr>0.25]
    nCorr = local_corr[local_corr<-0.25]
    print(f'positive correlations: {pCorr}\nnegative correlations {nCorr}')
    
#funcion para localizar columnas numéricas:

def numericCols(df: pd.DataFrame):
    numerics = []
    for indx in range(len(df.dtypes.index)):
        if df.dtypes.iloc[indx] != 'object':
            numerics.append(df.dtypes.index[indx])
        else:
            pass
    return numerics
#ACTUALIZACIÖN: despues de probar con diversas sugerencias, la función anterior es obsoleta y sera sustituida por:
#se puede usar el argumento include para dejar un tipo de dato en particular y tambien se puede usar exclude para
#remover un tipo de dato, en este caso podria ser mejor usar exclude para remover el tipo objetc
def numericOnly(x:pd.DataFrame):
    return x.select_dtypes(include = ['float64','int64'])

#función para 

#función de mapa de color, esta funcion regrese un mapa usando atributos de longitud y latitud
#la funcion es para un solo mapa:

def mapvis(df: pd.DataFrame, color):
  fig, ax = plt.subplots()

  ax.scatter(
      
      df['longitud'],
      df['latitud'],
      alpha = 0.5,
      s = 25,
      c = df[color],
      cmap = 'jet'
  )

  ax.set_xlabel('longitud')
  ax.set_ylabel('latitud')
  ax.set_title('Mapa del estado')
  fig.colorbar(ax.collections[0])
  return plt.show()

#versión generalizada para k mapas usando longitud, latitud y una caracteritica para el color.
