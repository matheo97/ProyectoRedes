#!/usr/bin/python

import socket
import sys
import subprocess
import os
import datetime
from time import gmtime, strftime

# Method used to determine MEMORY usage. Command to be used 'vmstat'

def mem(param):
	vmstat = subprocess.Popen(['vmstat'], stdout = subprocess.PIPE)
	tail = subprocess.Popen(['tail','-n','+3'], stdin = vmstat.stdout, stdout = subprocess.PIPE)
	tr = subprocess.Popen(['tr', '-s', ' '], stdin = tail.stdout, stdout = subprocess.PIPE)
	
	### Memoria libre, "5"

	### Eliminar primer y ultimo caracter, por presentar problemas.
        memoria_bytestring = subprocess.check_output(['cut', '-d', ' ', '-f', "5"], stdin = tr.stdout)
	memoria = ""
	for i in range(1, len(memoria_bytestring)-1):
		memoria += str(memoria_bytestring[i])
	
	fecha = strftime("%Y-%m-%d")
	hora = strftime("%H:%M:%S")
        
	comando = """curl -H "Content-type: application/json" -X POST  -d '{"Memoria":" """ + memoria + """ ","Fecha":" """ + fecha + """ ","Hora":" """ + hora + """ "}' http://demo-redes2016.rhcloud.com:80/"""
		
	os.system(comando)

if __name__ == '__main__':
	mem("free")
