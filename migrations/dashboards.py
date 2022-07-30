from redashAPI import RedashAPIClient
from supersetapiclient.client import SupersetClient

# create api client instance for superset
client = SupersetClient(
    host="http://localhost:8088",
    username="admin",
    password="admin",
)
API_KEY = 'LwVDxKku9xEyCBPGjidONYmoDDj1Ay9isqJAEJmS'
# Create API client instance for redash
Redash = RedashAPIClient(API_KEY)
res = Redash.get('dashboards')
print(res.json())


# adding the json file dashboard into superset
client.dashboards.add(res)