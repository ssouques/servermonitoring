	
from setuptools import setup, find_packages
	
setup(
	name="servermonitoring",
	version="0.1",
	packages=['servermonitoring'], # permet de récupérer tout les fichiers 
	install_requires=['flask', 'flask_restful', 'flask_jwt_extended'],
	description="Simple Server Monitoring API",
	url="https://github.com/ssouques/servermonitoring",
	author="ssouques",
	license="GNU/GPL",
	python_requires=">=3.7"
)