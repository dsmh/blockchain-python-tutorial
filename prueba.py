import requests
import socket

def buscar():
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.connect(("8.8.8.8", 80))

	mask = s.getsockname()[0].split('.')
	ip_mask = mask[0]+'.'+mask[1]+'.'+mask[2]

	print(ip_mask)

	for i in range(255):
		try:
			response = requests.get('http://'+ip_mask+'.'+str(i)+':5000/estoy_vivo', timeout=0.02)
		except:
			print('ip muerta '+ str(i))
			

if __name__=="__main__":
	buscar()