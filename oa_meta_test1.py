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

DOI = "10.6017/ital.v40i1.12553"

API_CALL = f"{API_URL}/references/doi:{DOI}"
#API_CALL = f"https://opencitations.net/index/api/v2/references/doi:{DOI}"
META_CALL = f"{META_URL}/doi:{DOI}"



# Headers to include with the request
#headers = {    "Authorization": f"Bearer {access_token}",    "Accept": "application/json",  # Assuming you want the response in JSON format }

HTTP_HEADERS = {"authorization": "7bc5a60c-b5ca-43e1-ae79-1bdaa0f97155"}


# Making the GET request
#response = requests.get(API_CALL, headers = HTTP_HEADERS)

#if response.status_code == 200:
    # Assuming the response is in JSON format
 #   data = response.json()
  #  print("Data retrieved successfully:")
   # print(data)
#else:
 #   print(f"Failed to retrieve data. Status code: {response.status_code}")


response = requests.get(META_CALL, headers = HTTP_HEADERS)

# Checking if the request was successful
if response.status_code == 200:
    # Assuming the response is in JSON format
    data = response.json()
    print("METAData retrieved successfully:")
    print(data)
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")

