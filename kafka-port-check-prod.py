#!/usr/bin/python3
# coding=utf-8
# Using UTF - 8 encoding

###############################
## Port check contra Marathon
## Creado en Febrero 2018
## Por: Karina Costa (RedBee)
## V14
## usage: python3 port-check-v14.py --ports 18081 --marathon http://localhost:18082
################################

###################
# Import libraries
###################
import json
import requests
import argparse

################################################
#Defino parametros a ser ingresados por el user
################################################
parser = argparse.ArgumentParser()
parser.add_argument('--ports', type=int, help='Puerto/s a chequear')
parser.add_argument('--marathon', type=str, default='localhost:8080', help='marathon a revisar')
args = parser.parse_args()
listapp=['boot-altamasivasites', 'coretx', 'cybersource', 'forms', 'notifications', 'persistor', 'soaptx' ,'tokenization', 'webtx', 'protocols/protocol-mastercard', 'protocols/protocol-pmc', 'protocols/protocol-visa',]

#####################################
#Creo la función que hara el chequeo
#####################################
def checkconnection():

    cone = requests.get('http://' + args.marathon + "/v2/info")
    conestatus = cone.status_code
    print("")
    print("#####################")
    print("Chequeo de conección")
    print("#####################")
    if str(conestatus) == '200':
       print("Hay conneción, el CODE STATUS es "+ str(conestatus))
       print("")
    else:
       print("curl no conecta.fin." + str(conestatus))


##------------------------------------------------------------------------------------------------------

def consultaconf():
   for n in listapp:
       #desa#properconf = ('broker-0.kafka-prod.mesos:9946,broker-1.kafka-prod.mesos:9236,broker-2.kafka-prod.mesos:9630')
       properconf = ('broker-1.kafka-prod.mesos:9361,broker-2.kafka-prod.mesos:9333,broker-0.kafka-prod.mesos:9155')
       r = requests.get('http://'+ args.marathon + "/v2/apps/decidir/" + n)
       rformat = r.json()
       #print(rformat)
       appid=rformat.get('app').get('id')
       apps=rformat.get('app').get('env').get('KAFKA_BOOTSTRAP_SERVERS')

       if apps == properconf:
           print("######################")
           print("-- Chequeo la conf --")
           print("######################")
           print("La configuracion de la app " + '"'+ n +'"' + " es correcta.")
           print(apps)
           print("\n")
       else:
           print("###############################")
           print("-- ERROR EN LA CONFIGURACION --")
           print("###############################")
           print("CUIDADO LA APP " + '"'+ n +'"' + " TIENE MAL SETEADO LOS BROKER KAFKA")
           print(apps)
           print("\n")




if __name__ == '__main__':
       checkconnection()
       consultaconf()

