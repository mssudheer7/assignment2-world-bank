# importing the required libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

def transposedData(data):
    """Function for transposing the data"""
    print("Transposed Data : ")
    df = data.transpose()
    display(df.head(5))

def barGraph(data):
    """bar graph function"""
    plt.figure(figsize=(20, 8))
    x = np.arange(len(data['Country Name']))
    w = 0.1
    plt.bar(x,data['1970'],width=w,label=1970)
    x = x+w
    plt.bar(x,data['1980'],width=w,label=1980)
    x = x+w
    plt.bar(x,data['1990'],width=w,label=1990)
    x = x+w
    plt.bar(x,data['2000'],width=w,label=2000)
    x = x+w
    plt.bar(x,data['2010'],width=w,label=2010)
    x = x+w
    plt.bar(x,data['2020'],width=w,label=2020)
    plt.xticks(x-0.2,data['Country Name'])
    plt.legend(fontsize=15)
    plt.xlabel('Country Name', size='18')
    plt.ylabel('Urban Population Growth (annual %)',size='18')
    plt.title('URBAN POPULATION GROWTH OVER DECADES',size='24')
    plt.show()
    plt.close()

def linePlot(data):
    """line plot function"""
    l = []
    for i in range(len(data)):
        x = data.loc[i, :].values.flatten().tolist()[1:]
        l.append(x)
        x = []
    year = [1970,1980,1990,2000,2010,2020]
    plt.figure(figsize=(20, 8))
    for i in range(len(l)):
        plt.plot(year,l[i],label = data['Country Name'][i])
    plt.legend(fontsize=12)
    plt.xlabel('Year', size='18')
    plt.ylabel('Urban Population Growth (annual %)',size='18')
    plt.title('URBAN POPULATION GROWTH OVER DECADES FOR DIFFERENT COUNTRIES',size='24')

def statProperties(x,year):
    """Statistical properties"""
    print('Statistical Properties for',x,': ')
    print("Average: ", np.mean(year))
    print("Standard deviations:", np.std(year))
    print("Skewness: ", stats.skew(year))
    print("Kurtosis: ", stats.kurtosis(year))
    print()
def correlation(data):
    """Correlation function"""
    print("Correlation : ")
    display(data.corr())
    print("Kendall Correlation : ")
    display(data.corr(method = "kendall"))

data = pd.read_csv("urban_population_growth.csv")# reading the csv file
print("Original data : ")
display(data.head())
transposedData(data)
barGraph(data)
linePlot(data)
statProperties("2000",data["2000"])
statProperties("2010",data["2010"])
statProperties("2020",data["2020"])
correlation(data)