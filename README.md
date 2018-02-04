# elasticsearch-example
Simple example using ElasticSearch with Django and autocomplete

<a href='https://medium.com/@adamwattis/elasticsearch-with-django-the-easy-way-909375bc16cb#.le6690uzj'>Link to Medium article.</a>

This project is modified to include elasticsearch delete, autocomplete using ajax, and custom analyzer using ngram.


TypeError: string indices must be integers

if this error then there is a mismatch between versions of elasticsearch and elasticsearch-dsl, uninstall both and install again.

brew uninstall --force elasticsearch
pip uninstall elasticsearch-dsl
brew install elasticsearch
pip install elasticsearch-dsl

project setup:
Python 3.6.4
python -m django --version
1.10.5
elasticsearch -V
Version: 6.1.3

Successfully installed elasticsearch-6.1.1 elasticsearch-dsl-6.1.0 ipaddress-1.0.19 urllib3-1.22


