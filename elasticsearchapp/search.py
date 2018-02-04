from elasticsearch_dsl.connections import connections
from elasticsearch_dsl import DocType, Text, Date, Search, analyzer, tokenizer
from elasticsearch.helpers import bulk
from elasticsearch import Elasticsearch
from . import models

# Create a connection to ElasticSearch
connections.create_connection()

# ElasticSearch "model" mapping out what fields to index
class BlogPostIndex(DocType):
    author = Text()
    posted_date = Date()
    my_analyzer = analyzer('my_analyzer',
        tokenizer=tokenizer('trigram', 'nGram', min_gram=3, max_gram=30),
        filter=['lowercase']
    )
    title = Text(analyzer=my_analyzer)
    text = Text()

    class Meta:
        index = 'blogpost-index'

    # Bulk indexing function, run in shell
    def bulk_indexing():
        BlogPostIndex.init()
        es = Elasticsearch()
        bulk(client=es, actions=(b.indexing() for b in models.BlogPost.objects.all().iterator()))

    # Simple search function
    def search(title):
        print(title)
        s = Search().filter('term', title=title.lower())
        response = s.execute()
        return response

