from models import Diputado
from models import Iniciativa
from google.appengine.ext import db

class PersistenceHelper:
	
	def getTopDiputadosIniciativas(self, limit, tipo):
		q = Diputado.all()	
		q.order("-%s" % tipo)
		results = q.fetch(limit)
		return results
		
	def getDownDiputadosIniciativas(self, limit, tipo):
		q = Diputado.all()
		q.order(tipo)
		results = q.fetch( limit )
		return results	
	
	def findDiputadoById( self, uuid ):
		
		q = Diputado.gql("WHERE uuid = :1",uuid )
		e = q.get()
		return e;
	
	def findIniciativasByDiputado( self, uuid ):
		q = Iniciativa.gql("WHERE diputado = :1 ORDER BY fecha ASC", uuid)		
		results = q.fetch(100)		
		return results;