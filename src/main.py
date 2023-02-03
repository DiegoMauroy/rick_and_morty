import requests

#### The function returns the data generated from an API call to url_base + query_url ####
def make_request(url_base, query_url):

    response = requests.get(url_base + query_url)

    if response.status_code == 200:

        data = response.json()

    return data

#### Main ####
if __name__ == "__main__":

    url_base = "https://rickandmortyapi.com/api"
    query_url = "/character"

    data = make_request(url_base, query_url)
