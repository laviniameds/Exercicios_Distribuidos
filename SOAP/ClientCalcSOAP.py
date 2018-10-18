from soaplib.client import make_service_client
from test import HelloService
client = make_service_client('http://localhost:8080/hello', HelloService())
client.hello('John')