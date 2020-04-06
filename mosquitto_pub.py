import paho.mqtt.client as mqtt
from time import strftime
import json

def format_json(dicionario):
    return json.dumps(dicionario)

def data_e_hora():
    return strftime('%Y-%m-%d %H:%M:%S')

dados = [
    ["ssc/sensor/26/presenca", {"client_id": "1", "valor": 1, "horario": data_e_hora()}],
    ["ssc/sensor/26/presenca", {"client_id": "1", "valor": 0, "horario": data_e_hora()}],
    ["ssc/sensor/26/temperatura", {"client_id": "2", "valor": 20, "horario": data_e_hora()}],
    ["ssc/sensor/26/temperatura", {"client_id": "2", "valor": 27, "horario": data_e_hora()}],
    ["ssc/sensor/26/luminosidade", {"client_id": "3", "valor": 0, "horario": data_e_hora()}],
    ["ssc/sensor/26/luminosidade", {"client_id": "3", "valor": 1023, "horario": data_e_hora()}],
    ["ssc/sensor/26/umidade", {"client_id": "4", "valor": 45, "horario": data_e_hora()}],

    ["ssc/sensor/27/presenca", {"client_id": "1", "valor": 1, "horario": data_e_hora()}],
    ["ssc/sensor/27/presenca", {"client_id": "1", "valor": 0, "horario": data_e_hora()}],
    ["ssc/sensor/27/temperatura", {"client_id": "2", "valor": 20, "horario": data_e_hora()}],
    ["ssc/sensor/27/temperatura", {"client_id": "2", "valor": 22, "horario": data_e_hora()}],
    ["ssc/sensor/27/luminosidade", {"client_id": "3", "valor": 0, "horario": data_e_hora()}],
    ["ssc/sensor/27/luminosidade", {"client_id": "3", "valor": 1023, "horario": data_e_hora()}],
    ["ssc/sensor/27/umidade", {"client_id": "4", "valor": 50, "horario": data_e_hora()}],

    ["ssc/sensor/28/presenca", {"client_id": "1", "valor": 1, "horario": data_e_hora()}],
    ["ssc/sensor/28/presenca", {"client_id": "1", "valor": 0, "horario": data_e_hora()}],
    ["ssc/sensor/28/temperatura", {"client_id": "2", "valor": 22, "horario": data_e_hora()}],
    ["ssc/sensor/28/temperatura", {"client_id": "2", "valor": 23, "horario": data_e_hora()}],
    ["ssc/sensor/28/luminosidade", {"client_id": "3", "valor": 0, "horario": data_e_hora()}],
    ["ssc/sensor/28/luminosidade", {"client_id": "3", "valor": 1023, "horario": data_e_hora()}],
    ["ssc/sensor/28/umidade", {"client_id": "4", "valor": 45, "horario": data_e_hora()}]

]

def main(topico, mensagem):
    client = mqtt.Client()

    client.connect("test.mosquitto.org", 1883)

    client.publish(topico, format_json(mensagem))

    client.disconnect()

for indice in range(len(dados)):
    topico, mensagem = dados[indice]
    main(topico, mensagem)
