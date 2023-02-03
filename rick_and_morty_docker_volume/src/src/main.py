import requests
import pandas as pd

#### The function returns the data generated from an API call to url_base + query_url ####
def make_request(url_base, query_url):

    response = requests.get(url_base + query_url)

    if response.status_code == 200:

        data = response.json()

    return data

#### Transform a dictionary column into several columns (use only if the indexes are unique) ####
def dictonnary_to_multi_columns(df, col, replace):

    for index, row in df.iterrows():

        for ky, value in row[col].items():
            
            df.at[index, col + "_" + ky] = value
    
    if replace:

        df = df.drop([col], axis = 1)
    
    return df

#### Transform a list column into a string column ####
def list_to_string(df, col):

    df[col] = [", ".join(row[col]) for index, row in df.iterrows()]

    return df

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