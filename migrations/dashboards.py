from redashAPI import RedashAPIClient
from supersetapiclient.client import SupersetClient

# create api client instance for superset
client = SupersetClient(
    host="http://localhost:8080",
    username="admin",
    password="admin",
)
# Create API client instance for redash
Redash = RedashAPIClient()
res = Redash.get('dashboard')
res.json()


# adding the json file dashboard into superset
client.dashboards.add(res)