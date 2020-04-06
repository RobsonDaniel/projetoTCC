from elasticsearch import Elasticsearch

es = Elasticsearch()

# https://www.elastic.co/guide/en/elasticsearch/reference/current/mapping-types.html
schema = {
    'mappings':{
        'properties':{
            'cliente_id': {'type': 'keyword'},
            'topico': {'type': 'text'},
            'sala': {'type': 'integer'},
            'sensor': {'type': 'keyword'},
            'valor': {'type': 'integer'},
            'horario': {
                'type': 'date',
                'format': 'yyyy-MM-dd HH:mm:ss'
            }
        }
    }
}

criar_indice = es.indices.create(index='ssc', body=schema, ignore=400)
#criar_indice = es.indices.delete(index='ssc')

print(criar_indice)
