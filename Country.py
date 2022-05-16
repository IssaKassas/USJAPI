from dataThreading import csvRunner , countryRunner , populationRunner , universityRunner
from concurrent.futures import ThreadPoolExecutor

COUNTRYAPI = countryRunner()

DATASET = csvRunner()

UNIVAPI = universityRunner()

POPULATION = populationRunner()

# OOP : OBJECT ORIENTED PROGRAMMING
# OOP: CLASS AND OBJECT
# CLASS : HOME IN SHEET
# OBJECT : REAL HOME
# CLASS HAS ATTRIBUTES AND METHODS BEHAVIORS

class Country:
    def __init__(self , name , date = '2022-04-16'): # CONSTRUCTOR
        self.__date = date # OBJECT ATTRIBUTES PRIVATE PUBLIC PROTECTED encapsulation
        self.__name = name
        # THIS ==== SELF
        
    def getDate(self): # OBJECT METHOD
        return self.__date
    
    def getName(self):
        return self.__name
    
    def setDate(self , date):
        self.__date = date
    
    def setName(self , name):
        self.__name = name
    
    def getCountry(self , col , item):
        country_data = DATASET[DATASET[col] == item]
        return country_data
    
    def getPopulation(self):
        for pop in POPULATION:
            if pop['country'] == self.getName():
                return pop['pop2022']
    
    def getRow(self):
        def runner():
            for country in COUNTRYAPI:
                if country['name']['common'] == self.getName():
                    name = country['name']['common']
                    currencies = list(country['currencies'].values())[0]['name']
                    capital = country['capital'][0]
                    region = country['region']
                    languages = list(country['languages'].values())
                    latlng = f"{country['latlng'][0]}/{country['latlng'][1]}"
                    area = country['area']
                    population = country['population']
                    timezones = country['timezones'][0]
                    continent = country['continents'][0]
                    flag = country['flags']['png']
                    return (name ,currencies , capital , region , languages , latlng,
                            area , population , timezones , continent , flag)
                    
        with ThreadPoolExecutor(max_workers = 24) as Execcutor:
            future = Execcutor.submit(runner)
            return future.result()

    def getUniversity(self):
        pagesList , univList = [] , []
        
        if self.getName() == "Syria":
            self.setName("Syrian Arab Republic")
            
        country_name = ''
        for university in UNIVAPI:
            if university["country"] == self.getName():
                country_name = university["country"]
                web_page = university["web_pages"][0]
                univ_name = university["name"]
                pagesList.append(web_page)
                univList.append(univ_name)
            else:
                if len(country_name) == 0:
                    continue
                else: 
                    return {
                            "country" : country_name,
                            "universities": univList,
                            "pages": pagesList
                            }