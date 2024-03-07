import requests

def get_citations(doi):
    """
    Fetches citation data for a given DOI from OpenCitations API.

    Parameters:
    doi (str): The DOI of the publication for which citation data is required.

    Returns:
    json: Citation data in JSON format.
    """
    # Replace spaces and special characters in DOI
    formatted_doi = requests.utils.quote(doi)

    # OpenCitations API endpoint for citation data
    url = f"https://opencitations.net/index/coci/api/v1/citations/{formatted_doi}"

    # Make a GET request to the OpenCitations API
    response = requests.get(url)

    if response.status_code == 200:
        # Return the JSON response if the request was successful
        return response.json()
    else:
        # Return an error message if something goes wrong
        return f"Error: Unable to fetch data, status code {response.status_code}"

# Example usage
doi = "10.1038/nature12373"  # Replace with the DOI you're interested in
citations = get_citations(doi)
print(citations)

