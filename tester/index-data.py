# ----------------------------------------------------------------------------------------------------------------------
# test project transform-doc-pipeline-ELK

from elasticsearch import Elasticsearch

import config

def main():

    # connect to Elasticsearch server
    es_client = Elasticsearch(config.ES_URL)

    # every line of data is a doc, Python uses the dict structure
    for data in config.VENDING_MACHINE_DATA:
        try:
            response = es_client.index(index=config.ES_INDEX,
                                       doc_type=config.ES_DOC, body=data,
                                       pipeline=config.ES_PIPELINE)
            print(data['data'] + ' -> ' + response['result'])
        except Exception:
            print('ERROR INDEXING -> ' + data['data'])


if __name__ == '__main__':
    main()

# ----------------------------------------------------------------------------------------------------------------------
