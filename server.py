import json
import cherrypy
import os

class HelloWorld(object):
    def index(self):
        return "Hello World!"
    index.exposed = True

    def getContentsOfRootDirectory(self,*args, **kwargs):
		z= json.dumps(os.listdir('/'));
		callback=kwargs["callback"]
		print callback
		if callback:
			content = str(callback) + '(' + z + ')'
			return content
		else:
			return z
    getContentsOfRootDirectory.exposed=True

    def getContentsOfFolder(self,*args,**kwargs):
		callback=kwargs["callback"]
		folderName=kwargs["folderName"]
		print folderName
		print os.listdir('/'+str(folderName))
		z= json.dumps(os.listdir('/'+str(folderName)));
		if callback:
			content = str(callback) + '(' + z + ')'
			return content
		else:
			return z
    getContentsOfFolder.exposed=True


cherrypy.quickstart(HelloWorld())