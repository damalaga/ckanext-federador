
![Logo datos abiertos Málaga](https://github.com/damalaga/ckanext-malaga/blob/master/ckanext/malaga/public/images/logoportaldatosabiertos.png)
ckanext-federador
=================
Esta extensión federa el catálogo de datos de una plataforma CKAN en datos.gob.es

Esta extensión ha sido desarrollada por el [Centro Municipal de Informática](http://cemi.malaga.eu) para ser usada junto con el [Portal de Datos Abiertos del Ayuntamiento de Málaga](http://datosabiertos.malaga.eu) 

datosabiertos.malaga.eu
=======================

El [Portal de Datos Abiertos del Ayuntamiento de Málaga](http://datosabiertos.malaga.eu) se ha implantado a partir de la plataforma CKAN.

[CKAN](http://ckan.org) es un portal de código abierto, diseñado y desarrolado para que los gobiernos locales y estatales puedan publicar y compartir su datos abiertos fácilmente. 

<b>IMPORTANTE:</b>
Esta extensión funciona para CKAN 2.6.0 y superiores, no habiendo sido probadas en versiones anteriores.

## Instalación y configuración de la federación de datos

Partimos de una plataforma CKAN 2.6.0 (no está probada en versiones anteriores)

### Requisitos
* ckanext-federador requiere la instalación previa de la extensión [ckanext-dcat](https://github.com/ckan/ckanext-dcat).

### Descarga de la extensión

* Conectarse a la máquina de CKAN con el usuario de ckan.
* Ir al directorio de instalación de la extensión (en nuestro caso):
<p>cd ckan/lib/default/src</p>
* Clonar la extensión
<p>git clone https://github.com/damalaga/ckanext-federador</p>
* Desplegarla
<p>python setup.py develop</p>

### Configuración de la extensión
Añadir en el fichero .ini estos parámetros y, a continuacion, reiniciar apache2:
<pre>
<code>
Añadimos la extension en ckan.plugins
ckan.plugins = .... federador

ckanext.federador.datetime_pub = #incluir la fecha de alta en datos.gob.es con formato YYYY-MM-DDTHH:MI:SS
ckanext.federador.publisher = #URL del organismo publicados
ckanext.federador.spatial_res = #URL del spatial_res
ckanext.federador.theme_tax = #URL del theme_tax
ckanext.federador.license_res = #URL de la licencia

</code>
</pre>

<b>NOTA</b>: ckanext-dcat requiere este parámetro en el fichero .ini:
1- los plugins en dcat:
ckan.plugins = .... dcat dcat_rdf_harvester
2- la configuración del catálogo (añadir esta línea en la configuración, tal cual aparece) 
ckanext.dcat.catalog_endpoint=/catalog/{_format}

## Campos opcionales en la federación

### Campo accrualPeriodicity
Añade la periodicidad con la que se actualiza el fichero (opcional en la federación).
Para que el federador rellene el dct accrualPeriodicity debemos añadir un registro en "Campo Personalizado" con la clave "Frecuencia" y alguno de los siguientes valores:
anual, semestral, trimestral, bimensual, mensual, quincenal, semanal, diaria, X minuto, Y segundo (en estos dos últimos casos, los valores X e Y se escribirán en la etiqueta time).
Si fuese necesario incorporar un nuevo valor, tendrá que añadirse en _ds_frequency(freq) del fuente [plugin.py](https://github.com/damalaga/ckanext-federador/ckanext/federador/plugin.py)

### Campo relation
Añade URLs relacionadas con el conjunto de datos en cuestión (opcional en la federación).
Para que el federador rellene el dct relation debemos añadir un registro en "Campo Personalizado" con la clave "Relacionado" y su valor correspondiente, en caso de tener más de un relacionado lo enumeraremos:
"Relacionado 1", "Relacionado 2", .... de este modo aparecerán todos los relacionados en la federación.

### Fichero malaga.rdf
El fichero que genera el rdf final es [malaga.rdf](https://github.com/damalaga/ckanext-federador/ckanext/federador/templates/catalog/malaga.rdf)


## PROCESO DE FEDERACIÓN

El fichero RDF se genera llamando a la siguiente URL http://servidor/catalog/malaga.rdf. El fichero resultante es el que usamos para federarnos en datos.gob.es

Por ejemplo desde línea de comandos de Linux: wget http://servidor/catalog/malaga.rdf -O fed-malaga.rdf

##Licencia:

El código de esta aplicación puede ser reutilizado, modificado y adaptado a las necesidades de los distintos portales de forma libre. Si utilizas nuestro código o parte de él, por favor, incluye nuestro logo en el cabecero o pie de página a modo de reconocimiento a Datos abiertos Málaga. Gracias! 


![Logo datos abiertos Málaga](https://github.com/damalaga/ckanext-malaga/blob/master/ckanext/malaga/public/images/logoportaldatosabiertos.png)


