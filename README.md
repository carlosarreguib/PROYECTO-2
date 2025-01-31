## Proyecto 2: Predicción del precio de alquiler de la vivienda en Barcelona 
***Juan Pablo Delzo***<br>
***Carlos Arregui***<br> <br>
:octocat: :fire: :pray: :muscle: :walking: :thumbsup:<br> <br>
El principal objetivo es que una vez ya desarrollado el primer proyecto de forma tradicional, y gracias al feedback recibido. El siguiente paso es utilizar herramientas en IA.
El proyecto consta de 3 apartados. <br>
Los dos primeros están desarrollados con `WindSurf`, con el fin de crear codigo con el mínimo esfuerzo en `Python`. (Solo habría que corregir o añadir puntualmente).<br>
El último apartado está desarrollado en `PowerBI` con `Python` y `PowerQuery` en el backend, y `R` en el frontend. <br>
> Procesamiento de datos
- Análisis exploratorio de datos.
- Llenado o eliminaciónde datos nulos.
- Eliminación de outliers.
- Escalado de datos.
- Transformación de variables.
> Métodos supervisados
- Regresión lineal.
- Regresión polinomial.
- Regresión logística.
- Regresión lasso.
- Regresión ridge.
- Regresión KNN.
- Regresión Random Forest.
- Regresión XGBoost.
- Regresión TensorFlow.
> Explotación de datos
- Visualización interactiva de los datos.
- Visualización de modelos. 

## Orden en *WindSurf*
**Procesamiento** 
<br>
Con Python, Pandas y Matplotlib con fondo `fivethirtyeight`, con el archivo adjunto en input: <br>
1. Elimina la columna `Unnamed: 0`. 
2. Analiza qué columnas tienen valores nulos. 
3. Si la columna `neighborhood` no tiene valores nulos, reemplaza los valores nulos en función de la moda en su columna de cada valor de `neighborhood`. 
4. Chequea si `square_meters_price` * `square_meters` difieren con price con una tolerancia de 500 euros. 
5. Elimina la columna `square_meters_price`. Detecta si hay outliers en `price` y apartalos del dataframe. 
6. Analiza si hay una relación lineal entre `price` promedio y `neighborhood`. Si tal valor es menor de 0.1, con get_dummies de Pandas, transforma la columna `neighborhood` con drop_first True y dtype a int. 
7. Guarda el dataframe final en un archivo csv.
