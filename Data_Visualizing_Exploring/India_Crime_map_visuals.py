import pandas as pd 
import geopandas as gpd
from pandas.core.reshape.merge import merge 
import matplotlib.pyplot as plt 

def readFile(filename):
    return pd.read_csv(filename)


def MapPlot(merged,Input_crime):
    if Input_crime == 1:
        fig, ax = plt.subplots(1,figsize=(10,6))
        ax.axis('off')
        ax.set_title('State Wise Cases_Property_Stolen',fontdict={'fontsize':'20', 'fontweight':'2'})

        merged.plot(column='Cases_Property_Stolen',cmap='YlOrRd',
        linewidth=0.8, ax=ax, edgecolor='0.2',legend=True,
        legend_kwds={'label': "Population by State",'orientation': "horizontal"})
        plt.show()
        return 
    if Input_crime == 2:
        fig, ax = plt.subplots(1,figsize=(10,6))
        ax.axis('off')
        ax.set_title('State Wise Crime against Women in India', fontdict={'fontsize':'20', 'fontweight':'2'})

        merged.plot(column='Victims_of_Rape_Total',cmap='YlOrRd',linewidth=0.8, ax=ax, edgecolor='0.2',legend=True,
        legend_kwds={'label': "Population by State",'orientation': "horizontal"})
        plt.show()
        return 
    if Input_crime == 3:
        fig, ax = plt.subplots(1,figsize=(10,6))
        ax.axis('off')
        ax.set_title('State Wise Crime Auto_Theft_Stolen', fontdict={'fontsize':'20', 'fontweight':'2'})

        merged.plot(column='Auto_Theft_Stolen',cmap='YlOrRd',linewidth=0.8, ax=ax, edgecolor='0.2',legend=True,
        legend_kwds={'label': "Population by State",'orientation': "horizontal"})
        plt.show()
        return 
    if Input_crime == 4:
        fig, ax = plt.subplots(1,figsize=(10,6))
        ax.axis('off')
        ax.set_title('State Wise Crime of Total_Murders', fontdict={'fontsize':'20', 'fontweight':'2'})

        merged.plot(column='Total_Murders',cmap='YlOrRd',linewidth=0.8, ax=ax, edgecolor='0.2',legend=True,
        legend_kwds={'label': "Population by State",'orientation': "horizontal"})
        plt.show()
        return 
    if Input_crime == 5:
        fig, ax = plt.subplots(1,figsize=(10,6))
        ax.axis('off')
        ax.set_title('State Wise Crime of Total_Kidnapp', fontdict={'fontsize':'20', 'fontweight':'2'})

        merged.plot(column='Total_Kidnapp',cmap='YlOrRd',linewidth=0.8, ax=ax, edgecolor='0.2',legend=True,
        legend_kwds={'label': "Population by State",'orientation': "horizontal"})
        plt.show()
        return 
    else:
        print('Not Input given')
        return 


filename = "D:/__studymaterial__/7-sem/Capston Project/Crimes_India/Data_Visualizing_Exploring/data/new_concat.csv"
df = readFile(filename)
# print(df.head(5))


fp = "D:/__studymaterial__/7-sem/Capston Project/Crimes_India/Data_Visualizing_Exploring/data/India_Geograph/India States/Indian_states.shp"
map_df = gpd.read_file(fp)

merged = map_df.set_index('st_nm').join(df.set_index('Area_Name'))
# print(merged.head())
# Create figure and axes for Matplotlib and set the title

print("-----/ Enter the Crime No. to get the result \-----\n\
    1.Cases_Property_Stolen,\n\
    2.Victims_of_Rape_Total,\n\
    3.Auto_Theft_Stolen,\n\
    4.Total_Murders,\n\
    5.Total_Kidnapp")
Input_crime_name = int(input("Enter The crime index:- "))
a = MapPlot(merged,Input_crime_name)

# fig, ax = plt.subplots(1,figsize=(10,6))
# ax.axis('off')
# ax.set_title('State Wise Crime against Women in India', fontdict={'fontsize':'25', 'fontweight':'3'})

# merged.plot(column='Victims_of_Rape_Total',cmap='YlOrRd',linewidth=0.8, ax=ax, edgecolor='0.8',legend=True)
# plt.show()