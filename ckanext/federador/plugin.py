# -*- coding: utf-8 -*-
#
# @author	CEMI Malaga
# @email        datosabiertos@malaga.eu
#
# Usa una libreria de python que hemos creado que asocia un tipo de dato con su mimetype y su tipo de fichero

import ckan.plugins as p
import os
import ckan.plugins.toolkit as toolkit
import pylons.config as config 
import filetypes as ft


#Lista de relacionados de un dataset que se pasa como parametro
def _ds_related(dsname):
	data_dict = {
		"id":dsname}
	related=toolkit.get_action('related_list')(data_dict=data_dict)
	return related

#Suma en bytes de todos los ficheros 
def _total_size():
	siz = 0
	ds_list = toolkit.get_action('package_list')(data_dict={})
	for dsname in ds_list:
		data_dict = {'id':dsname}
		dsitem = toolkit.get_action('package_show')(data_dict=data_dict)
		for res in dsitem['resources']:
			if res['size'] is not None:
				siz = siz + int(res['size'])
	return siz

#devuelve el valor que tiene en el .ini la propiedad que se pasa como parametro en el campo param
def _value(param):
	return config[param]

#devuelve la fecha actual en el formato correspondiente
def _datetime(self):
	from datetime import datetime, date, time
	today = str(datetime.now())
	return today[:10]+'T'+today[11:19]

#lista de datasets
def _ds_list():
	return toolkit.get_action('package_list')(data_dict={})

#lista de recursos de un dataset que se pasa como parametro
def _resources_list(dsname):
	data_dict = {'id':dsname}
	return toolkit.get_action('package_show')(data_dict=data_dict)

#calcular frecuencia 
def _ds_frequency(freq):

	if freq == '':
		return _format
	elif 'anual' in freq.lower():
		return {'frec':'years','times':'1'}
	elif 'trimestral' in freq.lower():
		return {'frec':'month','times':'3'}
	elif 'bimensual' in freq.lower():
		return {'frec':'month','times':'2'}
	elif 'mensual' in freq.lower():
		return {'frec':'months','times':'1'}
	elif 'quincenal' in freq.lower():
		return {'frec':'days','times':'15'}
	elif 'semanal' in freq.lower():
		return {'frec':'days','times':'7'}
	elif 'diaria' in freq.lower():
		return {'frec':'days','times':'1'}
	elif 'minuto' in freq.lower():
		return {'frec':'minutes','times':freq[:freq.index(' ')]}
	elif 'segundo' in freq.lower():
		return {'frec':'seconds','times':freq[:freq.index(' ')]}
	else:
		return {'frec':'years','times':'0'}


#Clase implementada
class FederadorPlugin(p.SingletonPlugin):
    p.implements(p.IConfigurer)
    p.implements(p.ITemplateHelpers)
    p.implements(p.IRoutes, inherit=True)


    def update_config(self, config_):

        p.toolkit.add_template_directory(config_, '/usr/lib/ckan/default/src/ckanext-federador/ckanext/federador/templates')
        p.toolkit.add_public_directory(config_, '/usr/lib/ckan/default/src/ckanext-federador/ckanext/federador/public')
        p.toolkit.add_resource('fanstatic', 'federador')

    def get_helpers(self):
        return {'fed_ds_related': _ds_related,
		'fed_total_size': _total_size,
		'fed_value': _value,
		'fed_datetime': _datetime,
		'fed_ds_list': _ds_list,
		'fed_resources_list': _resources_list,
		'fed_filetype': ft.mimetype_extension,
		'fed_frequency': _ds_frequency}
		
