import paho.mqtt.client as mqtt
from elasticSearch import indexar_documento
import formatar_dados
#import json

def on_connect(client, userdata, flags, rc):
    client.subscribe("ssc/sensor/#")

def on_message(client, userdata, msg):
    topico = msg.topic
    mensagem = msg.payload

    #####################TESTE######################
    #print(type(mensagem.decode('utf-8'))) #resultado: <class 'str'>
    #print(type(formatar_dados.formatar(topico, mensagem))) # resultado: <class 'dict'>
    #print(type(json.dumps(formatar_dados.formatar(topico, mensagem)))) # resultado: <class 'str'>
    ################################################

    indexar_documento.indexar(formatar_dados.formatar(topico, mensagem))

def main():
    client = mqtt.Client()

    client.on_connect = on_connect
    client.on_message = on_message

    client.connect("test.mosquitto.org", 1883)

    print("Esperando mensagens...")
    client.loop_forever()

main()
