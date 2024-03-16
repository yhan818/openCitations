### OpenCitations test

import requests

# OpenCitations API: https://opencitations.net/querying
# Index SPARQL endpoint: https://opencitations.net/index/sparql
#  Meta SPARQL endpoint: https://opencitations.net/meta/sparql
# OpenCitations Index REST API: https://opencitations.net/index/api/v2
# OpenCitations Meta REST API: https://opencitations.net/meta/api/v1 

# Pre-defined API URL and access token
access_token = "7bc5a60c-b5ca-43e1-ae79-1bdaa0f97155"

API_URL = "https://opencitations.net/index/api/v2"
META_URL = "https://opencitations.net/meta/api/v1"

doi = "10.6017/ital.v40i1.12553"
# URL encode the DOI to safely transmitted (e.g. /, :)
encoded_doi = requests.utils.quote(doi)

#API_CALL = f"{API_URL}/references/doi:{encoded_doi}"

# Hard code: worked! 
#META_CALL = f"https://opencitations.net/meta/api/v1/metadata/doi:{encoded_doi}"
META_CALL = f"{META_URL}/metadata/doi:{encoded_doi}"

print(META_CALL)

# Headers to include with the request, error code: 403
#headers = {"Authorization": f"Bearer {access_token}",    "Accept": "application/json"}

# Correct header
headers = {"Accept": "application/json"}
response = requests.get(META_CALL, headers = headers)

#response = requests.get(META_CALL)

# Checking if the request was successful
if response.status_code == 200:
    # Assuming the response is in JSON format
    data = response.json()
    print("Citations retrieved successfully:")
    for citation in data:
       print(citation)
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")
