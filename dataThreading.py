import urlAPI
from requests import get , RequestException
from pandas import read_csv
from json import load
from concurrent.futures import ThreadPoolExecutor

def getData(url):
    try:
        responseCountries = get(url)
        jsonData = responseCountries.json()
        return jsonData
    
    except RequestException as e:
       return e

def countryRunner():
    with ThreadPoolExecutor(max_workers = 25) as executor:
        future = executor.submit(getData, urlAPI.countriesUrl)
        return future.result()
    
def universityRunner():
    with ThreadPoolExecutor(max_workers = 25) as executor:
        future = executor.submit(getData, urlAPI.univUrl)
        return future.result()
    
def jsonData(file):
    try:
        with open(file , 'r') as f:
            jsonData = load(f)
            return jsonData
    
    except OSError as e:
       return e

def populationRunner():
    with ThreadPoolExecutor(max_workers = 25) as executor:
        future = executor.submit(jsonData, urlAPI.populationfile)
        return future.result()

def csvData(url , usecols):
    try:
        dataset = read_csv(url , usecols = usecols)
        return dataset
    
    except OSError as e:
       return e
    
def csvRunner():
    l = ["Confirmed" , "Date" , "Country" , 'Recovered' , 'Deaths']
    with ThreadPoolExecutor() as executor:
        future = executor.submit(csvData , urlAPI.url_dataSet , l)
        return future.result()