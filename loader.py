from google.appengine.api import datastore_types
from google.appengine.tools import bulkloader
from google.appengine.ext import db
import datetime

class Diputado(db.Expando):
    
    uuid                  			= db.StringProperty()
    asistencias_url       			= db.StringProperty()
    biopic_url            			= db.StringProperty()
    curul                 			= db.StringProperty()
    distrito              			= db.StringProperty()
    email                 			= db.StringProperty(multiline=True)
    entidad               			= db.StringProperty()
    foto                  			= db.StringProperty()
    iniciativas_url       			= db.StringProperty()
    nombre                			= db.StringProperty()
    partido               			= db.StringProperty()
    proposiciones_url     			= db.StringProperty()
    tipo_mayoria          			= db.StringProperty()
    votaciones_url        			= db.StringProperty()
    fecha_nacimiento				= db.DateProperty()
    numero_iniciativas				= db.IntegerProperty()
    numero_iniciativas_aprobadas	= db.IntegerProperty()
    numero_iniciativas_pendientes	= db.IntegerProperty()
    numero_iniciativas_desechadas	= db.IntegerProperty()

class Iniciativa(db.Expando):

	uuid                = db.StringProperty()
	link_gaceta 		= db.StringProperty()
	rol_iniciativa		= db.StringProperty()
	sinopsis			= db.Text()
	titulo				= db.Text()
	tramite				= db.StringProperty()
	fecha				= db.DateProperty()
	fecha_aprobacion	= db.DateProperty()
	fecha_publicacion	= db.DateProperty()
	diputado			= db.StringProperty()

class ComisionIniciativa(db.Expando):

	id			= db.IntegerProperty()
	comision	= db.StringProperty(multiline=True)
	tipo		= db.IntegerProperty()
	iniciativa	= db.StringProperty()

	
class Partido(db.Expando):

	nombre							= db.StringProperty()
	numero_diputados				= db.IntegerProperty()
	numero_iniciativas				= db.IntegerProperty()
	numero_iniciativas_aprobadas	= db.IntegerProperty()
	numero_iniciativas_pendientes	= db.IntegerProperty()
	numero_iniciativas_desechadas	= db.IntegerProperty()


class DiputadosLoader(bulkloader.Loader):
   
    def __init__(self):
		bulkloader.Loader.__init__(self, 'Diputado',[
			                                          ('uuid',lambda s:unicode(s, 'utf-8') or None),
			                                          ('asistencias_url',lambda s:unicode(s, 'utf-8') or None),
			                                          ('biopic_url',lambda s:unicode(s, 'utf-8') or None),
			                                          ('curul',lambda s:unicode(s, 'utf-8') or None),
			                                          ('distrito',lambda s:unicode(s, 'utf-8') or None),
			                                          ('email',lambda s:unicode(s, 'utf-8') or None),
			                                          ('entidad',lambda s:unicode(s, 'utf-8') or None),
			                                          ('fecha_nacimiento',lambda x:datetime.datetime.strptime(x,'%Y-%m-%d').date() or None),			                                          
			                                          ('foto',lambda s:unicode(s, 'utf-8') or None),                                                                                                        
			                                          ('iniciativas_url',lambda s:unicode(s, 'utf-8') or None),
			                                          ('nombre',lambda s:unicode(s, 'utf-8') or None),
													  ('numero_iniciativas',lambda s:int(s) or None),
													  ('numero_iniciativas_aprobadas',lambda s:int(s) or None),
													  ('numero_iniciativas_pendientes',lambda s:int(s) or None),
													  ('numero_iniciativas_desechadas',lambda s:int(s) or None),
			                                          ('partido',lambda s:unicode(s, 'utf-8') or None),
			                                          ('proposiciones_url',lambda s:unicode(s, 'utf-8') or None),
			                                          ('tipo_mayoria',lambda s:unicode(s, 'utf-8') or None),
			                                          ('votaciones_url',lambda s:unicode(s, 'utf-8') or None)
			                                          ]
			                                )
			
    def generate_key(self,i,values):
        key = "%s" % (values[0])
        return key

class IniciativaLoader(bulkloader.Loader):
	
	def __init__(self):
		bulkloader.Loader.__init__(self, 'Iniciativa',[
                                                    ('uuid',lambda s:unicode(s, 'utf-8') or None),
                                                    ('diputado',lambda s:unicode(s, 'utf-8') or None),
													('fecha',parseFecha),			                                       											
													('fecha_aprobacion',parseFecha),
													('fecha_aprobacion',parseFecha),											
                                                    ('link_gaceta',lambda s:unicode(s, 'utf-8') or None),
                                                    ('rol_iniciativa',lambda s:unicode(s, 'utf-8') or None),
                                                    ('sinopsis',lambda s:datastore_types.Text(s, encoding='UTF-8') or None),
                                                    ('titulo',lambda s:datastore_types.Text(s, encoding='UTF-8') or None),
                                                    ('tramite',lambda s:unicode(s, 'utf-8') or None)
                                                    ]
									)
	

	def generate_key(self,i,values):
		key = "%s" % (values[0])
		return key
		
class ComisionIniciativaLoader(bulkloader.Loader):

	def __init__(self):
		bulkloader.Loader.__init__(self, 'ComisionIniciativa',[
		                                              ('id',lambda s:int(s) or None),
		                                              ('comision',lambda s:unicode(s, 'utf-8') or None),
													  ('iniciativa',lambda s:unicode(s, 'utf-8') or None),
		                                              ('tipo',lambda s:int(s) or None)
		                                              ]
									)


	def generate_key(self,i,values):
		key = "%s" % str(values[0])
		return key		

class PartidoLoader(bulkloader.Loader):

	def __init__(self):
		bulkloader.Loader.__init__(self, 'Partido',[
				                                   	('nombre',lambda s:unicode(s, 'utf-8') or None),
				                                   	('numero_diputados',lambda s:int(s) or None),			
				                                   	('numero_iniciativas',lambda s:int(s) or None),
												   	('numero_iniciativas_aprobadas',lambda s:int(s) or None),
													('numero_iniciativas_pendientes',lambda s:int(s) or None),
													('numero_iniciativas_desechadas',lambda s:int(s) or None)
				                                    ]
											)

	def generate_key(self,i,values):
		key = "%s" % str(values[0])
		return key		
    


def parseFecha(s):
	if s:
		return datetime.datetime.strptime(s,'%Y-%m-%d %H:%M:%S').date()				
	else:
		return None
	
loaders = [DiputadosLoader, IniciativaLoader, ComisionIniciativaLoader, PartidoLoader]