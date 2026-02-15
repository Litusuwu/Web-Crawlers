# TikTok

keyword search for public videos. Restricted to approved academic/enterprise researchers. Free but highly selective.

Evaluate all available TikTok official APIs:
Research API: keyword search for public videos. Restricted to approved academic/enterprise researchers. Free but highly selective.
Display API: /user/info/, /video/list/, 600 calls/min. Requires user auth. Not useful for general content discovery.
Data Portability API: user's own data only.
Commercial Content API: ad library queries (EU only).

Document approval process, timeline, and likelihood of approval for a commercial threat monitoring product.

## Pasos previos


Los pasos a seguir para obtener un **Client Key** y **Client Secret**, los cuales son items necesarios para acceder a cualquier API, son:

> Registrarse en la web de TikTok Dev

> Crear una organizacion (o individual)
>>![Create organization](/imgs/SS7.png)

> Dirigirse a 'Manage Apps' y crear un App
>>![Developer Portal](/imgs/SS8.png)
>>![Create App](/imgs/SS9.png)

> Despues de crear el App, se tendrá que aplicar para review de TikTok para su aprobación dependiendo del API al que nosotros queramos acceder, las preguntas son:

> Basic information 
>![Basic Information](/imgs/SS10.png)
Basic information 2
>![Basic Information](/imgs/SS11.png)
> App review (Describir el producto y un demo)
>![App Review](/imgs/SS11.png)
> Products (APIs que necesita tu APP)
>![Products](/imgs/SS13.png)
> Ejemplo de Products 
> ![Example 1 Products](/imgs/SS14.png)
> Ejemplo de Products 2
>![Example 2 Products](/imgs/SS15.png)


### <u>Research API:</u>

Es un API dirigido a la comunidad académica, y bastante restringido a ella, no esta dirigida a enterprises debido a que pasa por un proceso riguroso de selección; similar a Reddit, tienes que enviar un ticket con la aplicación/investigación a realizar y esperar una respuesta de parte del equipo de TikTok para poder recien emplear el uso del API, el cual brinda tambien rate-limits moderados en su uso.

* **Ref:** https://developers.tiktok.com/doc/research-api-get-started?enter_method=left_navigation.

Los pasos a seguir son:

* Aplicar al Research API mediante una solicitud con los pasos previos
* Una vez aprobada tu solicitud por TikTok, se te generará un cliente de research, este podras ver todos los proyectos/apps/investigaciones aprobadas de parte de TikTok para el Research API; cada uno esta asociado a un **Client Key** y **Client Secret** que serán necesarios para conectarse al Research API endpoints.
* Una vez obtenidos estos 2, podras generar un **Client Access Token** con el cual se tendrá acceso al API de ResearchAPI.

>>>![TK Instructions Basic](/imgs/SS16.png)

* El estimado para obtener respuesta del Research API son <u>4 semanas o 1 mes calendario.</u>

* Los requerimientos estan justo debajo, considerando que Fuzzy realizará Web Scrapping y se lucrará de ello, es muy posible que no se pueda o acepten en su programa de TikTok research (como tal tampoco Fuzzy es researcher)

>>> ![TK Instructions](/imgs/SS6.png)


### <u>Display API</u>

Este API no es para el use-case de Fuzzy, debido a que este sirve principalmente con OAuth para self-profile; para mostrar información o posts de un profile propio, esto principalmente parece que esta hecho para promocionarse a uno mismo en una landing o content creator social difussing, un use case se puede ver como en la imagen siguiente:

![TK Display Information](/imgs/SS17.png)

Si en un futuro se quisiera hacer uso de este, el procedimiento es el que le sigue con **Pasos previos**, solo que se especifica el **Login Kit** en el apartado de **Products**.

## Data Portability API & Commercial Content API

Mismo caso que Display API, está fuera del scope. Sirve para transferir datos como nombres, usuarios entre tiktok y aplicaciones de terceros con autorización del usuario dueño de la cuenta, no está para el scope de Fuzzy, puesto que Fuzzy busca descubrir keywords y navegar por la web.

De parte de Commercial Content API, realmente lo unico que es su usecase es para evaluar los ADs que existen, esto podría servir pero a la vez no, puesto que no cubre el scope para lo que está pensado Fuzzy.

## Personal Thoughts

Tras realizar una revisión de la documentación de las APIs oficiales de Tk, y revisar cautelosamente sus T&C; TikTok no aprueba el uso de ningún API (Research API tampoco) para scrapear sea para vigilancia o uso comercial, si llega a ser de lucro no dejará scrapear.

## Evaluate third-party scraping services


