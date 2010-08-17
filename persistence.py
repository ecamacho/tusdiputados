import logging
from models import Diputado
from models import Iniciativa
from google.appengine.ext import db
from google.appengine.api import memcache

class PersistenceHelper:
				
	def getTopDiputadosIniciativas(self, limit, tipo):		
		key = "top_%s_%d" % (tipo, limit)
		results = memcache.get( key )
		if results is None:
			q = Diputado.all()	
			q.order("-%s" % tipo)
			results = q.fetch(limit)
			if not memcache.add( key, results ):
				logging.error("Memcache set failed.")
		else:
			logging.info("using cache in gettop")		
		return results
		
	def getDownDiputadosIniciativas(self, limit, tipo):
		key = "down_%s_%d" % (tipo, limit)
		results = memcache.get( key )
		if results is None:
			q = Diputado.all()
			q.order(tipo)
			results = q.fetch( limit )
			if not memcache.add( key, results ):
				logging.error("Memcache set failed.")
		else:
			logging.info("using cache in getdown")		
		return results	
	
	def findDiputadoById( self, uuid ):
		key = "dip_%s" % (uuid)		
		e   = memcache.get( key )
		if e is None:
			q = Diputado.gql("WHERE uuid = :1",uuid )
			e = q.get()
			if not memcache.add( key, e  ):
				logging.error("Memcache set failed.")
		else:
			logging.info("using cache")		
		return e
	
	def findIniciativasByDiputado( self, uuid ):
		q = Iniciativa.gql("WHERE diputado = :1 ORDER BY fecha ASC", uuid)		
		results = q.fetch(100)		
		return results
		
	def deleteAllInCache(self):
		memcache.flush_all()
		logging.info("cache deleted")	