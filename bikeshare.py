import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
CITIES = ['chicago', 'new york city', 'washington']

MONTHS= ['january', 'february', 'march', 'april', 'may', 'june']

DAYS = ['sunday', 'monday', 'tuesday', 'wednesday', \
        'thursday', 'friday', 'saturday' ]

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        try:
            city= input('\nEnter a city name you want to explore. Please enter chicago, new york city or washington\n').lower()
            
        except valueError:
            print('That\'s not a valid answer!')
            continue
    
        if city not in CITIES:
            print('That\'s not a valid answer. Please try again!')
            continue
    
        else:
            break


    # get user input for month (all, january, february, ... , june)

    while True:
    
        try:
            month= input('Enter the month you want to filter by. If you want all months type "all"\n').lower()
            
    
        except valueError:
            print('That\'s not a valid answer. Please try again!')
            break
            
        if month not in MONTHS:
            if month == "all":
                break
            print('That\'s not a valid answer. Please try again!')
            continue
        
        else: 
            break


    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        try:
            day= input('Enter the day you want to filter by.If you want all days type "all"\n').lower()
            
        except:
            print('That\'s not a valid answer.Please try again!')
            break
      
        if day not in DAYS:
            if day == "all":
                break 
            print('That\'s not a valid answer. Please try again!')
            continue
    
        else:
            break
        

    print('-'*40)
    return city, month, day
#city, month, day = get_filters()
#print("City is: " + str(city))
#print("Monday is: " + str(month))
#print("Day is: " + str(day))

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    #load file into the dataframe
    df = pd.read_csv(CITY_DATA[city])

    #convert start time to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    # extract month and day of week from Start Time and create a new column

    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()


    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = MONTHS
        month = MONTHS.index(month) + 1

    # filter by month to create the new dataframe
        df = df[df['month'] == month]

 # filter by day of week if applicable
    if day != 'all':

 # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df
#df = load_data('chicago', 'may', 'monday') 


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    most_common_month = df['month'].mode()[0]
    print('The most common month is:', most_common_month)

    # display the most common day of week
    most_common_day_week = df['day_of_week'].mode()[0]
    print('The most common day of week is:', most_common_day_week)

    # display the most common start hour
    df['hour']= df ['Start Time'].dt.hour
    most_common_hour= df['hour'].mode()[0]
    print('The most common start hour is:', most_common_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    most_common_start_station= df['Start Station'].mode()[0]
    print('The most commonly used start station is:', most_common_start_station)

    # display most commonly used end station
    most_common_end_station= df['End Station'].mode()[0]
    print('The most commonly used end is:', most_common_end_station)

    # display most frequent combination of start station and end station trip
    frequent_combination= df.groupby(['Start Station','End Station']).size().nlargest(1)
    print('The most frequent combination of start station and end station trip is:', frequent_combination)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('The total travel time is:', total_travel_time)

    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('The mean of travel time is:', mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types=df.groupby(['User Type'])['User Type'].count()
    print('User Type Count:', user_types)

    # Display counts of gender
    if city in ('chicago', 'new york city'):
        gender_count= df.groupby(['Gender'])['Gender'].count()
        print('Gender Count:', gender_count)

    # Display earliest, most recent, and most common year of birth
        earliest_yr_of_birth= int(df['Birth Year'].min())
        recent_yr_of_birth= int(df['Birth Year'].max())
        most_common_yr_of_birth=int(df['Birth Year'].mode())
        
        print('Earliest year of birth is {}. Most recent year of birth is: {}, Most common year of birth is {}'.format(earliest_yr_of_birth,recent_yr_of_birth,most_common_yr_of_birth))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def view_raw_data(df):
#view raw data
    index = 0
    while True:
        userinput = input('Would you like to see the raw data Enter yes or no.\n')
        if userinput.lower() == 'yes':
            print(df[index:index+5])
            index = index+5
        else:
            break
    

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        view_raw_data(df)


        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
