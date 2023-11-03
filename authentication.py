from azure.devops.connection import Connection
from msrest.authentication import BasicAuthentication
import pprint

personal_access_token = 'YOURPAT'
organization_url = 'https://dev.azure.com/YOURORG'

credentials = BasicAuthentication('', personal_access_token)
connection = Connection(base_url=organization_url, creds=credentials)
