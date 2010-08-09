from google.appengine.ext import db

class ComisionIniciativa(db.Model):
	
	comision	= db.StringProperty()
	tipo		= db.IntegerProperty()
	diputado	= db.ReferenceProperty(Iniciativa)
