import time
import pandas as pd
import numpy as np

# picking up the data in csv files saved in the same folder as the python script.

CITY_DATA = {'Chicago': 'chicago.csv',
             'New York': 'new_york_city.csv',
             'Washington': 'washington.csv'}


def takerequest():
    # Asks the user to specify a city, month and day to analyze.
    # Returns:
    # City - name of the city to analyze
    # Month - name of the month or all months to analyze
    # Day - name of the day or all days to analyze
    days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    months = ['January', 'February', 'March', 'April', 'May', 'June']
    print('\nWelcome and hello, let\'s explore US BikeShare data\n')

    while True:
        city = input('Please select a city to explore data and type below: \n Chicago/New York/Washington:').title()
        if city not in CITY_DATA:
            print('Please select a city from the list Chicago/New York/Washington')
        else:
            print(CITY_DATA[city])
            break

    while True:
        month = input('Please select a month and type in exactly as per below choices: \n January/February/March/April/May/June OR "All" to get data for all months:').title()
        if month != 'All' and month not in months:
            print('Please select a month from (Please type in exactly as per below choices): \n January/February/March/April/May/June or "All" to get data for all months')
        else:
            print(month)
            break

    while True:
        day = input('Please select a week and type in exactly as per below choices: \n Sunday/Monday/Tuesday/Wednesday/Thursday/Friday/Saturday or All (to get data for all days): ').title()
        if day != 'All' and day not in days:
            print('That\'s not a valid choice \n Please select a week and type in exactly as per below choices: \n Sunday/Monday/Tuesday/Wednesday/Thursday/Friday/Saturday or All (to get data for all days): ')
        else:
            print(day)
            break
    return city, month, day


def loaddata(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    if month != 'all':
        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day_of_week'] == day.title()]
    return df


def showdata(city):
    # Displays 5 records from the selected city."""
    # Asks user to type 'yes' or 'no' if user wants to see more record or not"""

    df = pd.read_csv(CITY_DATA[city])
    answers = ['Yes', 'No']
    user_input = ''

    i = 0

    while user_input not in answers:
        print("\nShow first 5 data records : type Yes or No then press enter")
        user_input = input().title()

        if user_input == "Yes":
            print(df.head())
        elif user_input not in answers:
            print("\nInvalid selection, please type Yes or No then press enter")

    while user_input == 'Yes':
        print("\nShow more data? please type Yes or No then press enter \n")
        i += 5
        user_input = input().title()
        if user_input == "Yes":
            print(df[i:i + 5])
        elif user_input != "Yes":
            break


def showstats_time(city):
    # Displays stats on the most frequent times of travel"""

    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    # Displays stats on the most popular month"""

    popularmonth = df['month'].mode()[0]
    print('Most popular month:', popularmonth)

    # Displays stats on the most popular day of the week"""

    popularday = df['day_of_week'].mode()[0]
    print('Most popular day of the week:', popularday)

    # Displays stats on the most popular hour of the day"""

    df['hour'] = df['Start Time'].dt.hour
    popularhour = df['hour'].mode()[0]
    print('Most popular hour of the day:', popularhour)

    print('\n')

def showstats_station(city):
    # Displays stats on the most popular stations and trip"""

    df = pd.read_csv(CITY_DATA[city])

    # Displays stats on the most popular start station"""

    popularstartStatn = df['Start Station'].mode()[0]
    print('Most popular station to start:', popularstartStatn)

    # Displays stats on the most popular end station"""

    popularendStatn = df['End Station'].mode()[0]
    print('most popular station to end:', popularendStatn)

    # Displays stats on the most popular trip from start to end station"""

    popular_start_and_end_Statn = (df['Start Station'] + ' - ' + df['End Station']).mode()[0]
    print('Most popular trip from start to end stations:', popular_start_and_end_Statn)

def showstats_tripduration(city):
    # Displays stats on the total and average trip duration"""

    df = pd.read_csv(CITY_DATA[city])

    # Displays stats on the total travel time for the trip"""

    total_time = df['Trip Duration'].sum()
    print('\nTotal Travel Time:',total_time / 3600, ' hours')

    # Displays stats on the average travel time for the trip"""

    avg_time = df['Trip Duration'].mean()
    print('Average Travel time:',  avg_time / 3600, ' hours')

    print('\n')

def showstats_user(city):
    # Displays stats on Bike share users

    df = pd.read_csv(CITY_DATA[city])

    # Displays count of users by type

    print('Count of users by type:\n', df['User Type'].value_counts());

    # Displays count of users by gender

    if 'Gender' in df:
        print('Counts of users by gender:\n', df['Gender'].value_counts())

    # Displays earliest birth year, recent birth year and popular birth year"""

    if 'Birth Year' in df:
        earliestbirthyear = int(df['Birth Year'].min())
        print('\n Earliest birth year :\n', earliestbirthyear)
        recentbirthyear = int(df['Birth Year'].max())
        print('\n most recent birth year:\n', recentbirthyear)
        popularbirthyear = int(df['Birth Year'].mode()[0])
        print('\n Most common year of birth:\n', popularbirthyear)

def bikeshare_stats():
    while True:
        city, month, day = takerequest ()
        df = loaddata (city, month, day)
        showdata (city)
        showstats_time (city)
        showstats_station (city)
        showstats_tripduration(city)
        showstats_user (city)
# Asks user if user wants to start analysis again?"""
        repeat = input('\nJDo you want to Repeat analysis again?: please type Yes or No then press enter:\n')
        if repeat.Title() == 'No':
            break

bikeshare_stats()