# SistemaExpertoGPI

### Instalación Motor Inferencia y Servidor

##### 1 Instalar Programas
  + Instalar Python 2.7
  + Instalar pip
  + Instalar gcc
  + Instalar python-virtualenv

##### 2 Ambiente de Desarrollo
  + Instalar virtualenv -> sudo pip install virtualenv
  + En el directorio del servidor ejecutar _'virtualenv venv'_
  + Luego ejecutar _'. venv/bin/activate'_
    * Para salir del Ambiente ejecutar _'deactivate'_

##### 3 Instalación Módulos Python en ambiente de Desarrollo
  + Instalar Flask
  + Instalar flask_restful
  + Instalar flask_cors

  >  pip install flask flask_restful flask_cors

##### 4 Correr Server
  + Ejercutar en el directorio del servidor *'FLASK_APP=server.py FLASK_DEBUG=1 python -m flask run'*

### Instalación Cliente

##### 1 Instalar Programas y módulos
  + Instalar Nodejs >=v6.x
  + En el directorio del cliente ejecutar _'npm install'_

##### 2 Correr cliente
  + En el directorio del cliente ejecutar _'npm start'_
