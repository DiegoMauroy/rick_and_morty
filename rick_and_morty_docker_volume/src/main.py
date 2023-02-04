from functions import *

#### Main ####
if __name__ == "__main__":

    url_base = "https://rickandmortyapi.com/api"
    query_url = "/character"

    resample(data_api_to_sqlite3, url_base, query_url, "data/database.db", 'all_characters')