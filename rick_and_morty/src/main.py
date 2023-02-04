from functions import *

#### Main ####
if __name__ == "__main__":

    url_base = "https://rickandmortyapi.com/api"
    query_url = "/character"

    data = make_request(url_base, query_url)

    df = pd.DataFrame(data["results"])
    df = dictonnary_to_multi_columns(df, "origin", True)
    df = dictonnary_to_multi_columns(df, "location", True)    
    df = list_to_string(df, "episode")

    print(df)