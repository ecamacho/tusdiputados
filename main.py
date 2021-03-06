#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import os
import logging

from google.appengine.ext import webapp
from persistence import PersistenceHelper
from google.appengine.ext.webapp import util
from google.appengine.ext.webapp import template



class MainHandler(webapp.RequestHandler):
    def get(self):
		helper = PersistenceHelper()
		topDiputados  = helper.getTopDiputadosIniciativas(  10, "numero_iniciativas" )
		downDiputados = helper.getDownDiputadosIniciativas( 10, "numero_iniciativas" )
		for d in downDiputados:
			if d.numero_iniciativas == None:
				d.numero_iniciativas = 0
		template_values = { "topDiputados"  :topDiputados, 
							"downDiputados" :downDiputados,
							"tipo"			:"presentadas" }
		path = os.path.join(os.path.dirname(__file__), 'index.html')
		self.response.out.write(template.render(path, template_values))
		
class TopIniciativasHandler(webapp.RequestHandler):
	def get(self):
		tipo  = self.request.get("tipo")
		helper = PersistenceHelper()
		topDiputados  = helper.getTopDiputadosIniciativas(  10, tipo )
		downDiputados = helper.getDownDiputadosIniciativas( 10, tipo )
		for d in downDiputados:
			if d.numero_iniciativas_pendientes == None:
				d.numero_iniciativas_pendientes = 0
			if d.numero_iniciativas_aprobadas == None:
				d.numero_iniciativas_aprobadas = 0
			if d.numero_iniciativas_desechadas == None:
				d.numero_iniciativas_desechadas = 0			
		for d in topDiputados:
			if d.numero_iniciativas_pendientes == None:
				d.numero_iniciativas_pendientes = 0
			if d.numero_iniciativas_aprobadas == None:
				d.numero_iniciativas_aprobadas = 0
			if d.numero_iniciativas_desechadas == None:
				d.numero_iniciativas_desechadas = 0			
					
		template_values = { "topDiputados"  :topDiputados, 
							"downDiputados" :downDiputados,
							"tipo"			:tipo }
		path = os.path.join(os.path.dirname(__file__), 'index.html')
		self.response.out.write(template.render(path, template_values))		
		
class DiputadoHandler(webapp.RequestHandler):
	def get(self):
		helper 	= PersistenceHelper()
		uuid    = self.request.get("id")
		d      	= helper.findDiputadoById(uuid)
		if d.numero_iniciativas == None:
			d.numero_iniciativas = 0
		if d.numero_iniciativas_pendientes == None:
			d.numero_iniciativas_pendientes = 0
		if d.numero_iniciativas_aprobadas == None:
			d.numero_iniciativas_aprobadas = 0	
		if d.numero_iniciativas_desechadas == None:
			d.numero_iniciativas_desechadas = 0	
					
		template_values = { "diputado" :d}
		path = os.path.join(os.path.dirname(__file__), 'diputado.html')
		self.response.out.write(template.render(path, template_values))	
		
class DiputadosHandler(webapp.RequestHandler):
	def get(self):
		tipo  = self.request.get("tipo")
		helper = PersistenceHelper()
		topDiputados  = helper.getTopDiputadosIniciativas(  500, tipo )
		downDiputados = helper.getDownDiputadosIniciativas( 500, tipo )

		
		for d in downDiputados:
			if d.numero_iniciativas_pendientes == None:
				d.numero_iniciativas_pendientes = 0
			if d.numero_iniciativas_aprobadas == None:
				d.numero_iniciativas_aprobadas = 0
			if d.numero_iniciativas_desechadas == None:
				d.numero_iniciativas_desechadas = 0			
		for d in topDiputados:
			if d.numero_iniciativas_pendientes == None:
				d.numero_iniciativas_pendientes = 0
			if d.numero_iniciativas_aprobadas == None:
				d.numero_iniciativas_aprobadas = 0
			if d.numero_iniciativas_desechadas == None:
				d.numero_iniciativas_desechadas = 0
		
		template_values = { "topDiputados"  :topDiputados, 
							"downDiputados" :downDiputados,
							"tipo"			:tipo }
		path = os.path.join(os.path.dirname(__file__), 'diputados.html')
		self.response.out.write(template.render(path, template_values))	
		
class IniciativasHandler(webapp.RequestHandler):
	def get(self):
		helper 	= PersistenceHelper()
		uuid	= self.request.get("id")
		d      	= helper.findDiputadoById(uuid)
		r		= helper.findIniciativasByDiputado(uuid)
		template_values = { "diputado" : d,
							"iniciativas" :r }
		path = os.path.join(os.path.dirname(__file__), 'iniciativas.html')
		self.response.out.write(template.render(path, template_values))			

class AboutHandler(webapp.RequestHandler):
	def get(self):
		template_values = {}
		path = os.path.join(os.path.dirname(__file__), 'about.html')
		self.response.out.write(template.render(path, template_values))
		
class DeleteCacheHandler(webapp.RequestHandler):
	def get(self):
		helper 	= PersistenceHelper()
		helper.deleteAllInCache()
		
def main():
	logging.getLogger().setLevel(logging.DEBUG)
	application = webapp.WSGIApplication([  ('/', MainHandler),
											('/about', AboutHandler),
											('/diputado', DiputadoHandler),
											('/diputados', DiputadosHandler),
											('/iniciativas', IniciativasHandler),
											('/deletecache', DeleteCacheHandler),
											('/topiniciativas', TopIniciativasHandler)											
										],
                                         debug=True)
	util.run_wsgi_app(application)


if __name__ == '__main__':
    main()
