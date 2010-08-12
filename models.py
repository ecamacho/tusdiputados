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