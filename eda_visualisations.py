import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 
from string import ascii_letters
import numpy as np

def all_variables(data):
    # retrieving a numpy array of dataset values
    values = data.values

    # getting index numbers of column names
    variables = [x for x in range(0,7)]
    i = 1
    plt.figure(figsize=(16,20))
    for var in variables:
        plt.subplot(len(variables), 1, i)
        plt.plot(values[:, var])
        plt.title(data.columns[var], y=0.5, loc='right')
        i += 1
        plt.yticks([])
        plt.xticks([])

def power_consumption_by_year(data, years):
    plt.figure(figsize = (16,20))
    for i in range(len(years)):
        #creating subplots
        plt.subplot(len(years), 1, i+1)
        #specifying the year
        year = years[i]
        #getting the data for the given year
        year_data = data[str(year)]
#         plotting global active power for each year
        plt.plot(year_data['global_active_power'])
        #adding a title
        plt.title("Household Energy Consumption in" + str(year), y=0, loc = 'right')
        plt.yticks([])

def power_consumption_by_month(data, year, months):
    """
    Arguments:
    data: dataframe
    year: string of year
    """
    plt.figure(figsize = (16,20))
    for i in range(len(months)):
        #creating subplots
        ax = plt.subplot(len(months), 1, i+1)
        #specifying the year
        month = year +'-' + str(months[i])
        #getting the data for the given year
        month_data = data[str(month)]
        #plotting global active power for each year
        plt.plot(month_data['global_active_power'])
        #adding a title
        plt.title(year + "Household Consumption in" + str(month), y=0, loc = 'right')
        plt.yticks([])


def day_plots(data, year, month, days):
    """
    Arguments:
    data: dataframe
    year: string of year
    month: string of month
    """
    days = ["%.2d" % x for x in range(1,29)]
    plt.figure(figsize = (16,40))
    for i in range(len(days)):
        #creating subplots
        ax = plt.subplot(len(days), 1, i+1)
        #specifying the year
        day = year +'-' + month + '-' + str(days[i])
        #getting the data for the given year
        day_data = data[str(day)]
        #plotting global active power for each year
        plt.plot(day_data['global_active_power'])
        #adding a title
        plt.title(day, y=0, loc = 'right')
        plt.yticks([])


def box_plots(data):
    plt.figure(figsize=(16,18))
    plt.subplots_adjust(wspace=0.2)
    months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']
    day = ['weekend', 'weekday']

    # weekday boxplots
    plt.subplot(3, 2, 1)
    sns.boxplot(x='weekday', y='global_active_power', data=data)
    plt.xlabel('Weekday (1 = yes)', fontdict={'fontsize':20})
    plt.ylabel('Global Active Power', fontdict={'fontsize':20})
    plt.title('Weekend vs Weekday Global Active Power Consumption', fontdict={'fontsize':20})
    plt.xticks(range(0, len(day)), day)
    sns.despine(left=True)
    plt.tight_layout()

    # month boxplots
    plt.subplot(3, 2, 2)
    sns.boxplot(x='month', y='global_active_power', data=data)
    plt.xlabel('Months', fontdict={'fontsize':20})
    plt.ylabel('Global Active Power', fontdict={'fontsize':20})
    plt.title('Monthly Global Active Power Consumption', fontdict={'fontsize':20})
    plt.xticks(range(0, len(months)), months)
    sns.despine(left=True)
    plt.tight_layout()

    # quarter subplot
    plt.subplot(3, 2, 3)
    sns.boxplot(x='quarter', y='global_active_power', data=data)
    plt.xlabel('Quarter', fontdict={'fontsize':20})
    plt.ylabel('Global Active Power', fontdict={'fontsize':20})
    plt.title('Quarterly Global Active Power Consumption', fontdict={'fontsize':20})
    sns.despine(left=True)
    plt.tight_layout()

    # yearly boxplots 
    plt.subplot(3, 2, 4)
    sns.boxplot(x='year', y='global_active_power', data=data)
    plt.xlabel('Year', fontdict={'fontsize':20})
    plt.ylabel('Global Active Power', fontdict={'fontsize':20})
    plt.title('Yearly Global Active Power Consumption', fontdict={'fontsize':20})
    sns.despine(left=True)
    plt.tight_layout()

    plt.subplot(3, 2, 5)
    sns.boxplot(x='month', y='temperature', color='r',data=data)
    plt.xlabel('Month', fontdict={'fontsize':20})
    plt.ylabel('Temperature in Degrees', fontdict={'fontsize':20})
    plt.title('Temperature across Year', fontdict={'fontsize':20})
    plt.xticks(range(0, len(months)), months)
    sns.despine(left=True)
    plt.tight_layout()

def power_line_plots(data):
    sns.set_style('whitegrid')
    plt.figure(figsize = (25,10))
    plt.subplots_adjust(wspace=0.1, hspace=0.5)
    months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']
    plt.suptitle('Global Active Power Consumption between 2007-2010', fontsize=20)

    # plotting 2007
    plt.subplot(2, 2, 1)
    sns.lineplot(x='month', y='global_active_power', data=data.loc[data['year']==2007],)
    plt.xlabel('Months', fontdict={'fontsize':12})
    plt.ylabel('Average Global Active Power (kWh)', fontdict={'fontsize':12})
    plt.title('2007', fontdict={'fontsize':15})
    plt.xticks(range(1, len(months)+1), months, fontsize=12, rotation=45)
    sns.despine(left=True)

    # plotting 2008
    plt.subplot(2, 2, 2)
    sns.lineplot(x='month', y='global_active_power', color='orange',data=data.loc[data['year']==2008])
    plt.xlabel('Months', fontdict={'fontsize':12})
    plt.ylabel('Average Global Active Power (kWh)', fontdict={'fontsize':12})
    plt.title('2008', fontdict={'fontsize':15})
    plt.xticks(range(1, len(months)+1), months, fontsize=12, rotation=45)
    sns.despine(left=True)

    # plotting 2009
    plt.subplot(2, 2, 3)
    sns.lineplot(x='month', y='global_active_power', color='r', data=data.loc[data['year']==2009])
    plt.xlabel('Months', fontdict={'fontsize':12})
    plt.ylabel('Average Global Active Power (kWh)', fontdict={'fontsize':12})
    plt.title('2009', fontdict={'fontsize':15})
    plt.xticks(range(1, len(months)+1), months, fontsize=12, rotation=45)
    sns.despine(left=True)

    # plotting 2010
    plt.subplot(2, 2, 4)
    sns.lineplot(x='month', y='global_active_power', color='g', data=data.loc[data['year']==2009])
    plt.xlabel('Months', fontdict={'fontsize':12})
    plt.ylabel('Average Global Active Power (kWh)', fontdict={'fontsize':12})
    plt.title('2010', fontdict={'fontsize':15})
    plt.xticks(range(1, len(months)+1), months, fontsize=12, rotation=45)
    sns.despine(left=True)

def factor_plots(data):
    plt.figure(figsize=(16,10))
    plt.subplots_adjust(wspace=0.1, hspace=0.5)
    plt.suptitle('Factor Plots of Global Active Power')
    # weekday
    plt.subplot(211)
    sns.factorplot('year','global_active_power',hue='weekday',
                   data=data.loc[data['year'] != 2006], size=6, aspect=1.5, legend=False)                                                   
    plt.title('Factor Plot of Global active power by Weekend/Weekday') 
    plt.yticks([])
#     plt.tight_layout() 
    plt.legend(loc='upper right')                                                                                                             
    
    # quarter
    plt.subplot(212)
    sns.factorplot('year','global_active_power',hue='quarter',
                   data=data.loc[data['year'] != 2006], size=6, aspect=1.5, legend=False)                                               
    plt.title('Factor Plot of Global active power by Quarter') 
    plt.yticks([])
#     plt.tight_layout()
    plt.legend(loc='upper right') 
    
    plt.show()

def correlation_matrix_plot(data):
    sns.set(style="white")
    corr = data.corr()
    mask = np.zeros_like(corr, dtype=np.bool)
    mask[np.triu_indices_from(mask)] = True
    f, ax = plt.subplots(figsize=(11, 9))

    # Generate a custom diverging colormap
    cmap = sns.diverging_palette(200, 15, as_cmap=True)

    # Draw the heatmap with the mask and correct aspect ratio
    sns.heatmap(corr, mask=mask, cmap=cmap, vmax=.3, center=0,
                square=True, linewidths=.5, cbar_kws={"shrink": .5})