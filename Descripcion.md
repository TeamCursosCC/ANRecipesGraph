# Descipcion

## Ideas

* Sugerencias de sustitucion de ingredientes
* Informacion sobre obtención
* Crear un Menu Diario
* Crear un Menu Semanal
* Crear un Menu Mensual
* Ubicación de los ingredientes
* Costo de los ingredientes y las recetas
* Balance Nutricional
* De una lista de ingredientes sugerir posibles recetas
* Estimacion de porciones de tipicas frases de la concina a una porcion con unidad de medida del SI

* Usando NLTK compilar las instrucciones de recetas de cocina para extraer:
  * ingrediente
  * cantidad
  * metodo de aplicacion

* A partir del balance nutricional escoger posibles ingredientes
* Filtrar ingredientes por zona
* Sugerir recetas a partir de ingredientes

## Modelo de Datos

Receta

```json
{
    "id": 1,
    "names": ["white rice Ball", "bola de arroz blanco", "oniguiri"],
    "regionalInfo": [
        {
            "region": "latam",
            "knownNames": ["bola de arroz blanco"],
            "elaborationMethod": ""
        }
    ],
    "portion": "3 porciones",
    "ingredients": [
        {"name": "salt", "amount": 0.5, "mUnit": "spoon"},
        ["oil", "sunflower oil"],
        "rice",
        "watter",
        "lettuce"
    ],
    "elaborationTime": 15,
}
```

## Ejemplo pedido a ChatGPT

### Pregunta

Sugiere un menu semanal para dos personas en Cuba que contemple un buen balance nutricional. Tener en cuenta desayuno, almuerzo y comida.

### Respuesta

¡Por supuesto! Aquí hay una sugerencia de menú semanal para dos personas en Cuba que incluye un buen balance nutricional:


Lunes:
Desayuno: Tortilla de huevos con vegetales y una rebanada de pan integral tostado.
Almuerzo: Arroz congrí (arroz con frijoles) con pollo a la plancha y ensalada de tomate y aguacate.
Cena: Ensalada de atún con lechuga, tomate, huevo duro y zanahoria rallada.

Martes:
Desayuno: Batido de frutas con yogur natural y granola.
Almuerzo: Frijoles negros con arroz blanco, chuletas de cerdo a la plancha y ensalada de lechuga y pepino.
Cena: Sándwich de jamón y queso con lechuga, tomate y mayonesa, acompañado de una ensalada de frutas.

Miércoles:
Desayuno: Tortilla de huevos con espinacas y una rebanada de pan integral tostado.
Almuerzo: Sopa de pollo con vegetales y arroz, acompañada de una ensalada de lechuga y tomate.
Cena: Hamburguesas de lentejas con pan integral, lechuga, tomate y ketchup, acompañado de una ensalada de repollo y zanahoria rallada.

Jueves:
Desayuno: Batido de frutas con yogur natural y avena.
Almuerzo: Ensalada de arroz con atún, maíz, tomate y lechuga.
Cena: Pescado a la plancha con puré de papas y ensalada de espinacas.

Viernes:
Desayuno: Huevos revueltos con tomate y cebolla, acompañados de una rebanada de pan integral tostado.
Almuerzo: Pollo al horno con papas y ensalada de lechuga, tomate y pepino.
Cena: Ensalada de garbanzos con lechuga, tomate, pepino y queso fresco.

Sábado:
Desayuno: Tortilla de huevos con jamón y una rebanada de pan integral tostado.
Almuerzo: Arroz con pollo y ensalada de lechuga, tomate y aguacate.
Cena: Vegetales salteados con arroz integral y una ensalada de espinacas y tomate.

Domingo:
Desayuno: Batido de frutas con yogur natural y avena.
Almuerzo: Frijoles colorados con arroz blanco, carne de res a la criolla y ensalada de lechuga y tomate.
Cena: Ensalada de pollo con lechuga, tomate, pepino y aguacate.

Espero que esto te sea de ayuda. ¡Buen provecho!

## Solicitud de Implementacion

Deseo crear un programa en python para estimar el costo de cada plato y el costo total de un menu diario, un menu semanal y un menu mensual, a aprtir de una sugerenciar de dichos menus, conociendo los ingredientes, sus cantidades por cada plato y el costo de cada ingrediente. Un problema que surge des este enfoque es la conversión entre diferentes sistemas de unidades sobre los ingredientes, atendiendo a sus cantidades y unidad de medida, por ejemplo, en las recetas se suele emplear denominaciones difusas como cucharadita, o taza, en la venta de productos se suelen utilizar pesos en diferentes unidadades como libras o gramos, en el caso de los líquitdos tapitas, litros, etc. Seria bueno construir una forma de abstracción que permita normalizar y homogeneizar estas unidades para realizar estimaciones precisas de las cantidades y por tanto costos implicados. Por ejemplo: un vendedor vende una libra de papas a x precio, pero para una comida quizas se necesiten 3 papas, en este caso hay una discrepancia por falta de informacion pues el tamaño y peso de cada papa no es conocido para realizar una división del precio por la cantidad, por tanto hay que realizar una estimacion difusa del costo tomando algun factor como el peso y tamaño medio de las papas. Todo esto debe quedar en el modelo de abstraccion de forma que sea ajustable en cualquier momento para ir mejorarndo las predicciones. Se puede dar la posibilidad de entrar el costo exacto de cada ingrediente en cada plato, a modo de reforzamiento de la predicción. La idea central es partir de tablas con los ingredientes, recetas y los datos necesarios y construir un grafo que mediante el analisis de grafos, permita obtener: sugerencias de platos a partir de ingredientes dados, estimar el costo de cada plato partir del costo estimado por el modelo descrito de cada ingrediente, sugerir subtitutos de ingredientes para una receta dada. Realizar un analisis de todos estos requerimientos y sugerir una posible implementacion teniendo en cuenta el lenguaje python, librerias como networkx y formato de datos json. Además sugerir métodos factibles para ir construyendo y mejorando la base de datos y el modelo de estimación de precios. Ver si hay articulos relacionados que puedan ser de utilidad.

### Respuesta a la solicitud por ChatGPT

Para abordar este problema, se pueden seguir los siguientes pasos:

1. Crear una tabla de ingredientes que contenga información sobre los nombres de los ingredientes, su costo por unidad de medida y la unidad de medida utilizada (por ejemplo, libras, gramos, cucharaditas, etc.).

2. Crear una tabla de recetas que contenga información sobre los nombres de los platos, los ingredientes necesarios para cada plato y la cantidad requerida de cada ingrediente (en la unidad de medida específica utilizada en la tabla de ingredientes).

3. Normalizar las unidades de medida de los ingredientes en la tabla de recetas. Para esto, se pueden crear funciones que conviertan las unidades de medida en una unidad común (por ejemplo, gramos) y que utilicen factores de conversión para hacer esta conversión.

4. Calcular el costo de cada plato a partir del costo estimado de cada ingrediente y la cantidad requerida de cada ingrediente para el plato. Si se dispone de información exacta sobre el costo de cada ingrediente, se puede utilizar esta información para mejorar la precisión de la estimación de costos.

5. Para sugerir platos a partir de ingredientes dados, se puede utilizar el grafo de ingredientes y recetas para encontrar las recetas que contengan los ingredientes dados y sugerir los platos correspondientes.

6. Para sugerir sustitutos de ingredientes para una receta dada, se pueden utilizar técnicas de análisis de similitud para encontrar ingredientes que sean similares en propiedades y características a los ingredientes originales y sugerir su uso como sustitutos.

Para implementar este modelo en Python, se puede utilizar la librería NetworkX para crear y analizar el grafo de ingredientes y recetas. Los datos de ingredientes y recetas se pueden almacenar en archivos JSON para facilitar su lectura y escritura en el programa. 

Para mejorar la base de datos y el modelo de estimación de precios, se pueden utilizar diversas técnicas, como:

- Recopilar información adicional sobre los ingredientes y sus propiedades, como su tamaño y peso promedio, para mejorar la precisión de las estimaciones de costos.

- Utilizar técnicas de aprendizaje automático para mejorar la precisión de las estimaciones de costos y sugerencias de platos y sustitutos de ingredientes.

- Utilizar técnicas de minería de datos para analizar patrones en los datos de ingredientes y recetas y mejorar la calidad de las sugerencias de platos y sustitutos de ingredientes.

Artículos relacionados que pueden resultar útiles para este proyecto incluyen:

- "Ingredient Network Analysis: Identifying Important Ingredients in Recipes" por Jisun An y Kyungsik Han. Este artículo describe un enfoque para analizar redes de ingredientes en recetas y utilizar esta información para sugerir sustitutos de ingredientes.

- "A survey of food recommendation systems" por Arun Pandian y S. Balamurugan. Este artículo revisa diversas técnicas utilizadas en sistemas de recomendación de alimentos y puede proporcionar ideas útiles para el proyecto.

- "Food pairing in molecular and cultural dimensions" por Yong-Yeol Ahn, Sebastian E. Ahnert, James P. Bagrow y Albert-László Barabási. Este artículo analiza las redes de alimentos y sabores y puede proporcionar información útil para el análisis de ingredientes en este proyecto.

## Buscando las mieles

cambiando un poco el enfoque, qué tipo de analisis de grafos y redes complejas se pueden aplicar sobre un grafo de recetas e ingredientes utilizando networkx? Por cada sugerencia numerar qué otros elementos se necesitarían. Un punto de partida puede ser sugerir platos a partir de ingredientes dados, sugerir ingredientes sustitutos para determinado ingrediente en una receta dada. Señalar en cada caso qué técnicas de análisis de grafos y redes complejas se utilizaron

### Respuesta con las mieles ChatGPT

Existen varias técnicas de análisis de grafos y redes complejas que se pueden aplicar a un grafo de recetas e ingredientes utilizando NetworkX. Algunas de ellas son:

1. Análisis de centralidad: Este análisis se utiliza para identificar los nodos más importantes en una red. En el contexto de un grafo de recetas e ingredientes, se puede utilizar para identificar los ingredientes más utilizados en las recetas. Esto puede ser útil para sugerir platos a partir de ingredientes dados, ya que los ingredientes más comunes probablemente se utilizarán en muchas recetas diferentes.

2. Análisis de modularidad: Este análisis se utiliza para identificar grupos de nodos altamente interconectados en una red. En el contexto de un grafo de recetas e ingredientes, se puede utilizar para identificar grupos de ingredientes que se utilizan juntos con frecuencia en las recetas. Esto puede ser útil para sugerir ingredientes sustitutos para un ingrediente dado en una receta, ya que los ingredientes que se utilizan en los mismos grupos pueden ser intercambiables en cierta medida.

3. Análisis de caminos mínimos: Este análisis se utiliza para encontrar la ruta más corta entre dos nodos en una red. En el contexto de un grafo de recetas e ingredientes, se puede utilizar para encontrar la ruta más corta entre dos ingredientes dados. Esto puede ser útil para sugerir platos a partir de ingredientes dados, ya que los ingredientes que están conectados por una ruta corta probablemente se utilizan juntos con frecuencia.

4. Análisis de comunidades: Este análisis se utiliza para identificar grupos de nodos altamente interconectados que están más densamente conectados entre sí que con el resto de la red. En el contexto de un grafo de recetas e ingredientes, se puede utilizar para identificar grupos de recetas que comparten ingredientes comunes. Esto puede ser útil para sugerir platos a partir de ingredientes dados, ya que las recetas que comparten ingredientes comunes pueden ser similares en sabor y estilo.

En términos de técnicas específicas que se pueden utilizar para implementar estas técnicas en NetworkX, algunas opciones son:

- Para el análisis de centralidad, se pueden utilizar medidas como la centralidad de grado o la centralidad de intermediación.

- Para el análisis de modularidad, se pueden utilizar algoritmos de detección de comunidades como el algoritmo de Louvain o el algoritmo de Girvan-Newman.

- Para el análisis de caminos mínimos, se puede utilizar el algoritmo de Dijkstra.

- Para el análisis de comunidades, se pueden utilizar algoritmos de detección de comunidades como el algoritmo de Louvain o el algoritmo de Girvan-Newman.

Para sugerir platos a partir de ingredientes dados, se puede utilizar una combinación de estas técnicas, como la centralidad de grado para identificar los ingredientes más comunes, el análisis de caminos mínimos para encontrar los ingredientes conectados a los ingredientes dados y el análisis de comunidades para identificar grupos de recetas que comparten ingredientes comunes.

Para sugerir ingredientes sustitutos para un ingrediente dado en una receta, se puede utilizar el análisis de modularidad para identificar otros ingredientes que se utilizan en los mismos grupos que el ingrediente dado, lo que sugiere que pueden ser intercambiables en cierta medida. También se puede utilizar el análisis de caminos mínimos para encontrar ingredientes conectados al ingrediente dado que pueden ser utilizados como sustitutos.

En general, el análisis de grafos y redes complejas puede ser una herramienta útil para explorar y analizar datos de recetas e ingredientes. Al utilizar técnicas como la centralidad, la modularidad, los caminos mínimos y las comunidades, se pueden identificar patrones interesantes en los datos que pueden ser útiles para sugerir platos y sustitutos de ingredientes.

## Mejoras

What other types of data could we add to the graph to improve our recipe suggestions?

### Sugerencias

There are several types of data that could be added to the graph of recipes and ingredients to improve recipe suggestions. Some examples are:

1. Nutritional information: Adding nutritional information for each ingredient and recipe could allow for healthier recipe suggestions based on dietary restrictions or personal preferences. This information could include the number of calories, fat content, protein content, and other important nutritional values.

2. User ratings: Adding user ratings and reviews for each recipe could help to identify popular and highly-rated recipes that are likely to be enjoyed by others. This information could be used to suggest recipes that have a high rating or that are similar in taste and style to highly-rated recipes.

3. Cooking time and difficulty: Adding information about the cooking time and difficulty for each recipe could help to identify recipes that are quick and easy to make or that require more time and skill. This information could be used to suggest recipes that are appropriate for different skill levels and time constraints.

4. Seasonal ingredients: Adding information about the availability of ingredients based on the season could help to suggest recipes that are appropriate for different times of the year. This information could be used to suggest recipes that are made with seasonal ingredients or that are appropriate for different holidays and occasions.

5. Cuisine type: Adding information about the cuisine type (e.g., Italian, Chinese, Mexican, etc.) for each recipe could help to suggest recipes that are similar in taste and style to other recipes in the same cuisine. This information could be used to suggest recipes that are appropriate for different cultural preferences and occasions.

Overall, adding additional data to the graph of recipes and ingredients can improve the accuracy and relevance of recipe suggestions. By incorporating additional information about nutritional content, user ratings, cooking time and difficulty, seasonal ingredients, and cuisine type, the graph can provide more personalized and tailored recipe suggestions that better meet the needs and preferences of individual users.



