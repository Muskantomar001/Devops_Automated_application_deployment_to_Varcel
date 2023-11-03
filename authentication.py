from azure.devops.connection import Connection
from msrest.authentication import BasicAuthentication
import pprint

personal_access_token = ''
url = 'https://dev.azure.com/'

credentials = BasicAuthentication('', personal_access_token)
connection = Connection(base_url=url, creds=credentials)
