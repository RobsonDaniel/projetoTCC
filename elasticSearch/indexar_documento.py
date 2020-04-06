from elasticsearch import Elasticsearch

es = Elasticsearch()

def indexar(documento):
    indexacao = es.index(index='ssc', body=documento)
    #indexacao = es.create(index='ssc', doc_type='_doc', body=documento, ignore=409)
    print(indexacao)
