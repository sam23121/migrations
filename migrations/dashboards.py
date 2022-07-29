from redashAPI import RedashAPIClient
from supersetapiclient.client import SupersetClient

# create api client instance for superset
client = SupersetClient(
    host="http://localhost:8080",
    username="sam",
    password="sam123",
)
# Create API client instance for redash
Redash = RedashAPIClient()
res = Redash.get('dashboards')
res.json()


# adding the json file dashboard into superset
client.dashboards.add(res)