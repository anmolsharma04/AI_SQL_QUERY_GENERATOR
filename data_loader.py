import pandas as pd
import requests


def load_csv(uploaded_file):
    return pd.read_csv(uploaded_file)


def load_api(api_url):
    response = requests.get(api_url)
    data = response.json()
    return pd.DataFrame(data)
