import requests

# Example DOI for which we want to retrieve citations. Replace with your DOI of interest
doi = "10.6017/ital.v40i1.12553"
### Note: this article in OC showing 2 citations (Google scholar has 3). 

# URL encode the DOI
encoded_doi = requests.utils.quote(doi)

# The API endpoint URL for retrieving citations of a specific DOI 
# API V1: 
url1 = f"https://opencitations.net/index/api/v1/citations/{encoded_doi}"

### API v2: 
url = f"https://opencitations.net/index/api/v2/citations/doi:{encoded_doi}"


META_CALL = f"https://opencitations.net/meta/api/v1/metadata/doi:{encoded_doi}"


# Making the GET request
response = requests.get(url)

# Checking if the request was successful
if response.status_code == 200:
    # Assuming the response is in JSON format
    data = response.json()
    print("Citations retrieved successfully:")
    for citation in data:
        print(citation)
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")

