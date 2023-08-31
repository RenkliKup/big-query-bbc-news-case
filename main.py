# Gerekli kütüphaneleri import ettim
import functions_framework
import os
from google.cloud import bigquery
import json
import flask
# Google Cloud kimlik doğrulama dosyasının belirttim
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "key.json"

# HTTP isteğini alan flask işlevi.
@functions_framework.http
def bbc_news(request):
    try:
        # title değerlerini saklamak için boş bir liste oluşturdum.
        titles = []
    
        # BigQuery istemcisini oluşturdum.
        client = bigquery.Client()

        # Sorguyu oluşturdum.
        query = """
            SELECT title
            FROM `bigquery-public-data.bbc_news.fulltext`
            WHERE category='tech' LIMIT 50
        """
        # Sorguyu çalıştırdım ve sonuçlarını results değişkenine atatım.
        results = client.query(query)
    
        # Sonuçlardan çıkan title değerini 'titles' listesine ekledim.
        for row in results:
            titles.append(row['title'])

        # titles listesini, sözlük nesnesine atatım.
        dict_object = {'title': titles}
        # Sözlüğü JSON biçiminde dönüştürdüm ve düzenledim.
        json_object = json.dumps(dict_object, indent=3)

        # JSON response'unu oluşturdum ve içerik türünü ayarladım.
        response = flask.Response(json_object, content_type='application/json')
        
        # Erişim izinleri için gerekli CORS başlığını ayarladım.
        response.headers['Access-Control-Allow-Origin'] = '*'

        # response'u döndürdüm.
        return response

    except Exception as e:
        # Hata durumunda boş bir sözlük oluşturdum.
        empty_response = {}
        
        # Boş JSON'ı oluşturdum
        empty_json = json.dumps(empty_response, indent=3)

        # JSON response'unu oluşturdum ve içerik türünü ayarladım.
        response = flask.Response(empty_json, content_type='application/json')

        # Erişim izinleri için gerekli CORS başlığını ayarladım.
        response.headers['Access-Control-Allow-Origin'] = '*'

        # response'u döndürdüm.
        return response





