import requests
import pandas as pd
import sqlite3
import schedule

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

#### Excute periodicaly the function fct ####
#### args contains the params of fct ####
def resample(fct, *args):

    schedule.every().minute.do(fct, *args)

    fct(*args)
    while True:

        schedule.run_pending()

#### Transfer the data from the api to a sqlite db ####
def data_api_to_sqlite3(url_base, query_url, db_name, table_name):

    data = make_request(url_base, query_url)

    df = pd.DataFrame(data["results"])

    df = dictonnary_to_multi_columns(df, "origin", True)
    df = dictonnary_to_multi_columns(df, "location", True)    
    df = list_to_string(df, "episode")

    conn = sqlite3.connect(db_name)
    c = conn.cursor()

    df.to_sql(name = table_name, con = conn, if_exists='replace')

    c.execute('''SELECT * FROM all_characters''')

    for row in c.fetchall():
        
        print (row)

    conn.close()