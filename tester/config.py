# ----------------------------------------------------------------------------------------------------------------------
# Config file to test project transform-doc-pipeline-ELK

# access to Elasticsearch server
ES_URL = '127.0.0.1:9200'
ES_INDEX = 'vending-machine'
ES_PIPELINE = 'vending-pipeline'
ES_DOC = '_doc'

# ----------------------------------------------------------------------------------------------------------------------
# lines of data to ingest into elasticsearch
# schema:
#   machine_cod -> internal machine code, alphanumeric
#   machine_model -> machine brand, alphanumeric
#   product_apple -> number of apples items
#   product_salad -> number of salads items
#   product_juice -> number of juice briks
#   product_pear -> number of pears items
#   location.lat -> machine location, latitude
#   location.lon -> machine location, longitude
#   tags -> labels to help marketing staff
#   last_filling -> last time this machine was refilled (timestamp YYYY-MM-DDTHH:MM:SS.MMMZ)
#   collection_timestamp -> just the time when this info was collected

# list of dictionaries
VENDING_MACHINE_DATA = [{'data': 'VM001 MODEL-5289 0 2 5 9 40.415363 -3.707398 [fruit, salad] 2019-08-01T10:55:25.000Z 2019-08-15T01:00:00.000Z'}]

VENDING_MACHINE_DATA.\
    append({'data': 'VM002 MODEL-5289 0 0 5 0 40.615221 -3.894582 [fruit, university] 2019-08-02T09:25:25.000Z 2019-08-15T01:05:00.000Z'})

VENDING_MACHINE_DATA.\
    append({'data': 'VM003 MODEL-5258 10 1 5 10 40.415363 -3.999911 [new] 2019-08-02T15:01:00.000Z 2019-08-15T01:10:00.000Z'})

VENDING_MACHINE_DATA.\
    append({'data': 'VM004 MODEL-5200 10 18 15 1 40.415363 -3.707398 [gray, old] 2019-08-03T16:00:20.000Z 2019-08-16T01:00:00.000Z'})

# Machine Code is missing on purpose
VENDING_MACHINE_DATA.\
    append({'data': 'MODEL-5200 1 0 0 0 40.415355 -3.123398 [yellow, old, fruit] 2019-08-03T16:00:20.000Z 2019-08-16T01:00:00.000Z'})

VENDING_MACHINE_DATA.\
    append({'data': 'VM005 MODEL-5200 1 0 0 0 40.415355 -3.123398 [yellow, old, fruit] 2019-08-03T16:00:20.000Z 2019-08-16T01:00:00.000Z'})

# ----------------------------------------------------------------------------------------------------------------------

