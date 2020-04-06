import json

def formatar(topico, mensagem):
    dados = json.loads(mensagem.decode('UTF-8'))
    id = dados['client_id']
    valor = dados['valor']
    data = dados['horario']

    lista = topico.split('/')
    sala = lista[-2]
    sensor = lista[-1]

    documento = {
        'cliente_id': id,
        'topico': topico,
        'sala': sala,
        'sensor': sensor,
        'valor': valor,
        'horario': data
    }

    return documento
    #return json.dumps(documento)
