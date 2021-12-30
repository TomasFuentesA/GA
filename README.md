# GA


# Botometer

Para trabajar con Botometer se utiliza el archivo IsABot.py que al ejecutarse, abre una ventana de navegador con el sitio https://botometer.osome.iu.edu/ . Una vez iniciada la ejecucion del programa, se cuenta con 120 segundos para realizar el login en el sitio con una cuenta de Tweeter propia. Se decidio un margen de 120 segundos puesto que, al realizar muchas consultas, el sitio solicita realizar el login mas de una vez.

IsABot.py tiene un "Modo A" y "Modo B". El "Modo A", permite, a partir de un dataset especificado y que contenga el screen name (@nombredeusuario) de una cuenta de Tweeter, generar un dataset nuevo pero con una columna adicional de nombre "botoscore". Esta columna contendrá el valor obtenido mediante Botometro para la cuenta especificada.

Por otro lado, el "Modo B" permite, a partir de un diccionario de usuarios previamente calificados como bot mediante el arbol de decision, comprobar su puntaje de Botometro, pudiendo asi identificar los falsos positivos. Se puede ver que este comportamiento se puede aplicar de igual forma para los usuarios calificados como humanos, con el fin de identificar los falsos negativos.

Tras ejecutar el "Modo B" de IsABot.py , los resultados obtenidos se podran interpretar mediante statometer.py . Esto permitirá obtener facilmente estadigrafos tales como la media, la cantidad de cuentas cuyos datos no se pidieron recuperar, ademas de las cuentas cuyos valores de Botometro se encuentran sobre ciertos umbrales que determinarian si son o no un bot, lo que permitiria identificar los falsos negativos/positivos segun sea el caso.




