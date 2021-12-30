# GA

### Generar Dataset

Para generar un dataset de usuarios a evaluar por la herramienta, en primera instancia se debe asociar o crear una cuenta de Twitter con permisos de desarrollador, esto se realiza en el sitio oficial https://developer.twitter.com/, siguiendo el paso a paso correspondiente. En el portal de desarrollo de Twitter se debe crear un nuevo proyecto, en el cual se le otorgarán Keys y Tokens (publicos y privados), cada par se debe ingresar en el código de ExtraccionTwitter.py de forma directa en las variables de nombre:

>API_KEY 

>API_KEY_SECRET 

>ACCESS_TOKEN 

>ACCESS_TOKEN_SECRET

Con dichas variables ya agregadas se puede ejecutar el código fuente para realizar una extracción de usuarios correspondientes al territorio chileno. En caso de querer cambiar el país de extracción se debe cambiar el país en la siguiente variable:

> places = api.search_geo(query="CHILE", granularity="country") [Línea 49]

### Botometer

Para trabajar con Botometer se utiliza el archivo IsABot.py que al ejecutarse, abre una ventana de navegador con el sitio https://botometer.osome.iu.edu/ . Una vez iniciada la ejecucion del programa, se cuenta con 120 segundos para realizar el login en el sitio con una cuenta de Tweeter propia. Se decidio un margen de 120 segundos puesto que, al realizar muchas consultas, el sitio solicita realizar el login mas de una vez.

IsABot.py tiene un "Modo A" y "Modo B". El "Modo A", permite, a partir de un dataset especificado y que contenga el screen name (@nombredeusuario) de una cuenta de Tweeter, generar un dataset nuevo pero con una columna adicional de nombre "botoscore". Esta columna contendrá el valor obtenido mediante Botometro para la cuenta especificada.

Por otro lado, el "Modo B" permite, a partir de un diccionario de usuarios previamente calificados como bot mediante el arbol de decision, comprobar su puntaje de Botometro, pudiendo asi identificar los falsos positivos. Se puede ver que este comportamiento se puede aplicar de igual forma para los usuarios calificados como humanos, con el fin de identificar los falsos negativos.

Tras ejecutar el "Modo B" de IsABot.py , los resultados obtenidos se podran interpretar mediante statometer.py . Esto permitirá obtener facilmente estadigrafos tales como la media, la cantidad de cuentas cuyos datos no se pidieron recuperar, ademas de las cuentas cuyos valores de Botometro se encuentran sobre ciertos umbrales que determinarian si son o no un bot, lo que permitiria identificar los falsos negativos/positivos segun sea el caso.

### Herramienta para crear el árbol

Para generar correctamente el árbol con la herramienta creada, se deben utilizar dos csv distintos entre si. Uno de ellos será el de entrenamiento, es imporante que este dataset tenga la columna 'bot'. Y el segundo dataset será el que tenga los usuarios a predecir.

![imagen](https://user-images.githubusercontent.com/69986261/147791533-5d88cbbe-d05d-4c0f-b24f-96617b3afb98.png)

Una vez listos ambos datasets, se deberá colocar el nombre donde se indica en la imagen anterior y correr el "notebook" completamente. El árbol será construido y además se realizaran las predicciones.



