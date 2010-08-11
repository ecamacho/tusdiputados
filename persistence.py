from models import Diputado
from google.appengine.ext import db

class PersistenceHelper:
	
	def getTopDiputadosIniciativas(self, limit):
		q = Diputado.all()	
		q.order("-numero_iniciativas")
		results = q.fetch(limit)
		return results
		
	def getDownDiputadosIniciativas(self, limit):
		q = Diputado.all()
		q.order("numero_iniciativas")
		results = q.fetch( limit )
		return results	