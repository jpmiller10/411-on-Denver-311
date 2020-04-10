import numpy as np
import pandas as pd
import geopandas
import datetime
import json
import os
import matplotlib.pyplot as plt 
import seaborn as sns
sns.palplot('colorblind')
import calendar as cal
plt.style.use('tableau-colorblind10')
plt.rcParams.update({'font.size': 13})

df = pd.read_pickle('data/all_requests_2018_pickled_df')
dfgeo = pd.read_pickle('data/geo_requests_2018_pickled_df')

def filename(str_in):
    name = str_in.lower().replace(' ','_')
    return name

def plot_over_time(df, time_col1, time_col2, ax, title, interval):
    '''   
    Argument:
        df: pandas df
        time_col1: column with time data of initial report
        time_col2: column with time data of closed report
        ax - axis to plot on
        title - plot title
        interval - Datetime interval for plotting data  
    Return:
            ax - axis with plot
    '''
    ax.plot(df.groupby(pd.Grouper(key=time_col1, freq=interval))
            .size(), '*-', color = 'firebrick', linewidth=2, label='Opened')
    ax.plot(df.groupby(pd.Grouper(key=time_col2, freq=interval))
             .size(), '^-', color = 'blue', linewidth=1, label='Closed')
    ax.set_title(title)
    ax.set_ylabel('Number of 311 Requests')
    ax.legend(loc='best')
    name=filename(title)
    save_location='images/'+ name +'timeplot.png'
    plt.savefig(save_location)
    return ax

def plot_agency_and_response_time(df,ax, col = 'Agency', vals = ['NONE'], title = 'Response Time in Days'):
    '''
    Violin plot for categorical values  
    Arguments:
            df: pandas df
            ax: axis to plot on
            col: the column with categorical data
            vals: values we do not want to consider
            title = plot title
    Return:
            Violin Plot of Overall Response by agency
    '''
    df = df[['Agency', 'Response_Value']]
    df['Response_Value'].dropna()

    for val in vals:
        df[col] = df[col][df[col] != val]
    
    ordering = df.groupby(df[col]).size().sort_values(ascending=False).index
    

    #Violin plot
    sns.violinplot(y=col, x=df['Response_Value'], data=df, ax=ax, bw=.1, order=ordering)
    ax.set_title(title)
    ax.set_ylabel(None)
    ax.set_xlabel('Response Time in Days')
    name=filename(title)
    save_location='images/'+name + '_violin_plot.png'
    plt.savefig(save_location, bbox_inches="tight")
    return ax

def hist_of_requests(df,ax, col = 'Agency', vals = ['Denver Human Services'], title = '311 Requests by Agency'):
    '''
    Prints a histograms for categorical values
        Arguments:
            df: pandas df
            ax: axis to plot on
            col:  the column with categorical data
            vals:  values we do not want to consider
            title:  plot title
        Return:
            horizontal histogram 
    '''
    df[col].replace('  ', value='NOT RECORDED', inplace=True)

    for val in vals:
        df[col] = df[col][df[col] != val]
    
    ordering = df.groupby(df[col]).size().sort_values(ascending=False).index
    sns.countplot(y=col, data=df, order=ordering, ax= ax)
    ax.set_title(title)
    ax.set_ylabel(None)
    name=filename(title)
    save_location='images/'+name + '_side_hist.png'
    plt.savefig(save_location, bbox_inches="tight")
    return ax

def plot_elected_and_response_time(df,ax, polit, col = 'NBHD_NAME', vals = ['NONE'], title = 'Response Time in Days'):
    '''
    Violin plot for categorical values  
    Arguments:
            df: pandas df
            ax: axis to plot on
            polit: str of the office of elected official choice of:
                ["Mayor's Office", 'City Council', 'Clerk & Recorder']
            col: the column with categorical data
            vals: values we do not want to consider
            title = plot title
    Return:
           violin plot by neighborhood
    '''
    df = df.groupby('Agency').get_group(polit)
    df = df[['NBHD_NAME', 'Response_Value']]
    df['Response_Value'].dropna()

    for val in vals:
        df[col] = df[col][df[col] != val]
    
    ordering = df.groupby(df[col]).size().sort_values(ascending=False).index
    
    sns.violinplot(y=col, x=df['Response_Value'], data=df, ax=ax, bw=.1, order=ordering)
    ax.set_title(title)
    ax.set_ylabel(None)
    ax.set_xlabel('Response Time in Days')
    name=filename(title)
    save_location='images/'+name + '_violin_plot.png'
    plt.savefig(save_location, bbox_inches="tight")
    return ax

if __name__ == "__main__":
    fig, ax = plt.subplots(1, 1, figsize=(10, 5))
    plot_over_time(df, 'Case_Created_dttm', 'Case_Closed_dttm', ax, 'Cases Opened v. Closed', 'M')

    fig2, ax2 = plt.subplots(1, 1, figsize=(10, 10))
    hist_of_requests(df, ax2, col = 'Agency')

    fig3, ax3 = plt.subplots(1, 1, figsize=(10, 25))
    hist_of_requests(dfgeo, ax3, col = 'NBHD_NAME', title = '311 Requests by Neighborhood')

    fig4, ax4 = plt.subplots(1, 1, figsize=(10, 20))
    plot_agency_and_response_time(df,ax4, col = 'Agency', vals = ['NONE'], title = 'Response Time in Days')

    fig5, ax5 = plt.subplots(1, 1, figsize=(25, 15))
    plot_elected_and_response_time(dfgeo,ax5, "Mayor's Office", col = 'NBHD_NAME', vals = ['NONE'], title = 'Mayor Response Time in Days')

    fig6, ax6 = plt.subplots(1, 1, figsize=(25, 15))
    plot_elected_and_response_time(dfgeo,ax6, 'City Council', col = 'NBHD_NAME', vals = ['NONE'], title = 'City Council Response Time in Days')

    fig7, ax7 = plt.subplots(1, 1, figsize=(25, 15))
    plot_elected_and_response_time(dfgeo,ax7, 'Clerk & Recorder', col = 'NBHD_NAME', vals = ['NONE'], title = 'Clerk & Recorder Response Time in Days')

    fig8, ax8 = plt.subplots(1, 1, figsize=(25, 15))
    plot_elected_and_response_time(dfgeo,ax8, 'Parks & Recreation', col = 'NBHD_NAME', vals = ['NONE'], title = 'Parks & Recreation Response Time in Days')

    fig9, ax9 = plt.subplots(1, 1, figsize=(25, 15))
    plot_elected_and_response_time(dfgeo,ax9, 'External Agency', col = 'NBHD_NAME', vals = ['NONE'], title = 'External Agency Response Time in Days')

    fig10, ax10 = plt.subplots(1, 1, figsize=(25, 15))
    plot_elected_and_response_time(dfgeo,ax10, 'Environmental Health', col = 'NBHD_NAME', vals = ['NONE'], title = 'Environmental Health Response Time in Days')

    fig11, ax11 = plt.subplots(1, 1, figsize=(25, 15))
    plot_elected_and_response_time(dfgeo,ax11, 'Safety', col = 'NBHD_NAME', vals = ['NONE'], title = 'Safety Response Time in Days')

    fig12, ax12 = plt.subplots(1, 1, figsize=(25, 15))
    plot_elected_and_response_time(dfgeo,ax12, 'Community Planning & Development', col = 'NBHD_NAME', vals = ['NONE'], title = 'Community Planning & Development Response Time in Days')

    fig13, ax13 = plt.subplots(1, 1, figsize=(25, 15))
    plot_elected_and_response_time(dfgeo,ax13, 'Excise & License', col = 'NBHD_NAME', vals = ['NONE'], title = 'Excise & License Response Time in Days')

    fig14, ax14 = plt.subplots(1, 1, figsize=(25, 15))
    plot_elected_and_response_time(dfgeo,ax14, '311', col = 'NBHD_NAME', vals = ['NONE'], title = '311 Response Time in Days')

    fig15, ax15 = plt.subplots(1, 1, figsize=(25, 15))
    plot_elected_and_response_time(dfgeo,ax15, 'Finance', col = 'NBHD_NAME', vals = ['NONE'], title = 'Finance Response Time in Days')

    fig16, ax16 = plt.subplots(1, 1, figsize=(25, 15))
    plot_elected_and_response_time(dfgeo,ax16, 'Tech Services', col = 'NBHD_NAME', vals = ['NONE'], title = 'Tech Services Response Time in Days')

    