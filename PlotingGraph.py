from concurrent.futures import ThreadPoolExecutor
from mathDraw import Plot
from pandas import DataFrame
from Country import Country

lebanon = Country('Lebanon')
yemen = Country('Yemen')
saudi = Country('Saudi Arabia')
qatar = Country('Qatar')
uae = Country('United Arab Emirates')
oman = Country('Oman')
egypt = Country('Egypt')
morocco = Country('Morocco')
syria = Country('Syria')
bahrain = Country('Bahrain')
algeria = Country('Algeria')
kuwait = Country('Kuwait')

countries = [lebanon , syria , saudi , algeria , morocco , kuwait , oman , uae , egypt , 
             yemen , qatar , bahrain]

names , confirmedList , population , tableData = [] , [] , [] , []
deathDictionary , recoveredDictionary , datesDictionary = dict() , dict() , dict()

def data(country : Country):
    country_data = country.getCountry('Country' , country.getName())
    recoveredDictionary[country.getName()] = country_data['Recovered']
    deathDictionary[country.getName()] = country_data['Deaths']
    datesDictionary[country.getName()] = country_data[country_data['Date'] == country.getDate()]
    confirmedList.append(datesDictionary[country.getName()].iloc[0]['Confirmed'])
    if country.getName() == "United Arab Emirates":
        names.append("UAE")
    else:
        names.append(country.getName())
    population.append(float(country.getPopulation()))
    return (recoveredDictionary , deathDictionary , datesDictionary , 
            confirmedList , names , population)

def runner(c : Country):
    with ThreadPoolExecutor(max_workers = 24) as executor:
        task = executor.submit(data , c)
        return task.result()
    
for country in countries:
    runner(country)

font1 = {
    'family':'serif',
    'color':'blue',
    'size':20
    }

font2 = {
    'family':'serif',
    'color':'darkred',
    'size':15
    }

mycolors = ["black", "red" , 'blue' , '#4953ff' , '#f2341d',
    'yellow' , 'orange' , 'green', "#4CAF50" , '#123456']

plotData = Plot()

def plotPie():
    plotData.pieDraw(
        "Number of countries",
        confirmedList,
        names,
        mycolors,
        90,
        "Countries",
        'best'
        )

def plotLine(name: str):
    plotData.plotDraw(deathDictionary[name],
              recoveredDictionary[name],
              'The curve of Recovered in terms of Deaths',
              deathDictionary[name].max(),
              recoveredDictionary[name].max(),
              'Deaths', 'Recovered',
              font1 , font2
            )

def plotBar():
    dataframe = DataFrame(dict(names = names , population = population))
    dataframe = dataframe.sort_values('population')
    plotData.barDraw(
        "Population of Countries",
        'names',
        'population',
        dataframe,
        mycolors,
        'Countries',
        'Population',
        14
    )