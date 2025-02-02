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
**Procesamiento:** 
<br>
Con Python, Pandas y Matplotlib con fondo `dark_background`, con el archivo adjunto en input: <br>
1. Elimina la columna `Unnamed: 0`. 
2. Analiza qué columnas tienen valores nulos. 
3. Si la columna `Neighborhood` no tiene valores nulos, reemplaza los valores nulos en función de la moda en su columna de cada valor de `neighborhood`. 
4. Chequea si `Square_meters_price` * `Square_meters` difieren con price con una tolerancia de 1000 euros. 
5. Elimina la columna `Square_meters_price`. Detecta si hay outliers con el método de IQR con k igual a 3 en `Price` y apartalos del dataframe. 
6. Analiza si hay una relación lineal entre `price` promedio y `Neighborhood`. Si tal valor es menor de 0.1, con get_dummies de Pandas, transforma la columna `Neighborhood` con drop_first True y dtype a int. 
7. Guarda dos archivos con extensión csv, uno con la tabla transformada con get_dummies y el otro sin transformarlo.
