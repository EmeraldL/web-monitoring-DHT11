#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
--> DHT11 como sensor de temperatura e umidade.
--> Raspberry Pi como coletora, processadora e submissora das informações do sensor.
--> ThingSpeak como nuven receptora e como plataforma de compartilhamento de
informações.

Para ajudar na montagem e com as instalações necessárias na Raspberry Pi,
indico estes artigos:
1. https://www.filipeflop.com/blog/temperatura-umidade-dht11-com-raspberry-pi
2. https://electronicshobbyists.com/raspberry-pi-sending-data-to-thingspeak-simplest-raspberry-pi-iot-project/

'''
 
#Importanto as bibliotecas necessárias.
import Adafruit_DHT #Para comunicação com o sensor DHT11.
import RPi.GPIO as GPIO #Para controle das GPIOs da Raspberry Pi.
import time #Para controle do intervalo de tempo time.sleep().
import urllib3 #Para comunicação com o ThingSpeak.

apikey = 'QDVJXCRKLWDRRQUW' #Chave de escrita.
url = 'https://api.thingspeak.com/update?api_key={}&field1={}&field2={}'

#Escolhendo o sensor a ser usado.
sensor = Adafruit_DHT.DHT11
#sensor = Adafruit_DHT.DHT22
 
#Para numeração do pino: BOARD,
GPIO.setmode(GPIO.BOARD) 
# Define a GPIO conectada ao pino de dados do sensor
pino_sensor = 18
 
# Informacoes iniciais
print("Leitura dos valores de temperatura e umidade:")
print("Laboratório Didático de Circuitos Elétricos - UNIR")
 
while(1):
   #Leitura das informações no sensor.
   umid, temp = Adafruit_DHT.read_retry(sensor, pino_sensor)
   #Exibição das informações no terminal
   if umid is not None and temp is not None:
     print("Temperatura = {0:0.1f}  Umidade = {1:0.1f}n").format(temp, umid)
     print("Nova leitura em 10 minutos...n")

     #Enviando as informações de leituras para o ThingSpeak:
     urllib3.PoolManager().request('GET', url.format(apikey,temp,umid))

     #Tempo de aguardo para nova leitura e novo envio de informação.
     time.sleep(600) # 600s = 10min.
   else:
     #Em caso de falta de comunicação com o sensor, uma mensagem de erro é exibida.
     print(".::. PROBLEMAS NA LEITURA DO DHT11... .::.")

