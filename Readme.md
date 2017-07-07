![Logo datos abiertos Málaga](https://github.com/damalaga/ckanext-malaga/blob/master/ckanext/malaga/public/images/logoportaldatosabiertos.png)

ckanext-federador
=================
Esta extensión federa el catálogo de datos de una plataforma CKAN en datos.gob.es

Esta extensión ha sido desarrollada por el [Centro Municipal de Informática](http://cemi.malaga.eu) para ser usada junto con el [Portal de Datos Abiertos del Ayuntamiento de Málaga](http://datosabiertos.malaga.eu) 

¿Qué es la federación?
======================
Es el término que se emplea para describir la agregación de catálogos con el portal de datos abiertos del Gobierno [datos.gob.es](http://datos.gob.es), que es el portal de carácter nacional que organiza y gestiona el Catálogo de Información Pública del sector público. Asimismo, desde este portal se proporciona información general, materiales formativos y noticias de actualidad sobre la reutilización de la información. Esto quiere decir que, desde este momento, todo el catálogo de datos abiertos de la entidad federada está disponible desde el portal de datos abiertos del Gobierno, de forma que aumenta las posibilidades de reutilización de la información publicada.

Con este módulo se consigue la adaptación a los estándares marcados en la Norma Técnica de Interoperabilidad, que establece las condiciones comunes sobre selección, identificación, descripción, formato, condiciones de uso y puesta a disposición de los documentos y recursos de información elaborados o custodiados por el sector público, relativos a numerosos ámbitos de interés como la información social, económica, jurídica, turística, sobre empresas, educación, etc.

datosabiertos.malaga.eu
=======================

El [Portal de Datos Abiertos del Ayuntamiento de Málaga](http://datosabiertos.malaga.eu) se ha implantado a partir de la plataforma CKAN.

[CKAN](http://ckan.org) es un portal de código abierto, diseñado y desarrolado para que los gobiernos locales y estatales puedan publicar y compartir su datos abiertos fácilmente. 

## Instalación y configuración de la federación de datos.

Partimos de una plataforma CKAN 2.6.0 (no está probada en versiones anteriores)

### Requisitos
* ckanext-federador requiere la instalación previa de la extensión [ckanext-dcat](https://github.com/ckan/ckanext-dcat).

### Descarga de la extensión

* Conectarse a la máquina de CKAN con el usuario de ckan.
* Ir al directorio de instalación de la extensión (en nuestro caso): `cd ckan/lib/default/src`
* Clonar la extensión: `git clone https://github.com/damalaga/ckanext-federador`
* Desplegarla: `python setup.py develop`

### Configuración de la extensión
Añadir en el fichero .ini estos parámetros y, a continuacion, reiniciar apache2:
<pre>
<code>
#Añadimos la extension en ckan.plugins
ckan.plugins = .... federador

ckanext.federador.datetime_pub = #incluir la fecha de alta en datos.gob.es con formato YYYY-MM-DDTHH:MI:SS
ckanext.federador.publisher = #URL del organismo publicados
ckanext.federador.spatial_res = #URL del spatial_res
ckanext.federador.theme_tax = #URL del theme_tax
ckanext.federador.license_res = #URL de la licencia

</code>
</pre>

<b>NOTA</b>: ckanext-dcat requiere este parámetro en el fichero .ini:
* los plugins en dcat: `ckan.plugins = .... dcat dcat_rdf_harvester`
* la configuración del catálogo (añadir esta línea en la configuración, tal cual aparece) `ckanext.dcat.catalog_endpoint=/catalog/{_format}`

## Funcionalidades implementadas
* Metadato accrualPeriodicity
* Metadato relation

### accrualPeriodicity
Añade la periodicidad con la que se actualiza el fichero (opcional en la federación).
Para que el federador rellene el dct accrualPeriodicity debemos añadir un registro en "Campo Personalizado" con la clave "Frecuencia" y alguno de los siguientes valores:
anual, semestral, trimestral, bimensual, mensual, quincenal, semanal, diaria, X minuto, Y segundo (en estos dos últimos casos, los valores X e Y se escribirán en la etiqueta time).
Si fuese necesario incorporar un nuevo valor, tendrá que añadirse en _ds_frequency(freq) del fuente ckanext-federador/ckanext/federador/plugin.py/plugin.py

### relation
Añade URLs relacionadas con el conjunto de datos en cuestión (opcional en la federación).
Para que el federador rellene el dct relation debemos añadir un registro en "Campo Personalizado" con la clave "Relacionado" y su valor correspondiente, en caso de tener más de un relacionado lo enumeraremos:
"Relacionado 1", "Relacionado 2", .... de este modo aparecerán todos los relacionados en la federación.

### Fichero malaga.rdf
El fichero rdf que se genera usa como plantilla el fichero malaga.rdf que se encuentra en ckanext-federador/ckanext/federador/templates/catalog/malaga.rdf.


## Federación

El fichero RDF se genera llamando a la siguiente URL http://servidor/catalog/malaga.rdf. El fichero resultante es el que usamos para federarnos en datos.gob.es

Por ejemplo desde línea de comandos de Linux: wget http://servidor/catalog/malaga.rdf -O fed-malaga.rdf

## Licencia

El código de esta aplicación puede ser reutilizado, modificado y adaptado a las necesidades de los distintos portales de forma libre. Si utilizas nuestro código o parte de él, por favor, incluye nuestro logo en el cabecero o pie de página a modo de reconocimiento a Datos abiertos Málaga. Gracias! 


![Logo datos abiertos Málaga](https://github.com/damalaga/ckanext-malaga/blob/master/ckanext/malaga/public/images/logoportaldatosabiertos.png)


