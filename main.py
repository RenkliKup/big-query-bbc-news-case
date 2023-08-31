import functions_framework
import os
from google.cloud import bigquery
import json
import flask
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "key.json"
@functions_framework.http
def bbc_news(request):
    try:
        titles = []
    
        client = bigquery.Client()

        query = """
            SELECT title
            FROM `bigquery-public-data.bbc_news.fulltext`
            WHERE category='tech' LIMIT 50
        """
        results = client.query(query)
    
        for row in results:
            titles.append(row['title'])

        dict_object = {'title': titles}
        json_object = json.dumps(dict_object, indent=3)

        response = flask.Response(json_object, content_type='application/json')

        response.headers['Access-Control-Allow-Origin'] = '*'

        return response

    except Exception as e:
        
        empty_response = {}
        empty_json = json.dumps(empty_response, indent=3)

        response = flask.Response(empty_json, content_type='application/json')

        response.headers['Access-Control-Allow-Origin'] = '*'

        return response





