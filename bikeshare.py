#add description:  Analyze Bike Share Data
import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
'new york city': 'new_york_city.csv',
'washington': 'washington.csv' }
months = {'all','january','february','march','april','may','june'}
days = { 'all','sunday','monday','tuesday','wednesday','thursday','friday','saturday'}
def get_filters():
    while True:
        global city
        city = input('What city would you like to analyze? Chicago, New York City or Washington?: ').lower()
        if city in (CITY_DATA.keys()):
            print('You selected: ', city)
            break
        else:
            print("Not a valid city, please choose either Chicago, New York City or Washington")
        #we're ready to exit the loop.
    while True:
        month = input('What month would you like to analyze? January, February, March, April, May, June or All?: ').lower()
        if month in (months):
            print('You selected: ', month)
            break
        else:
            print("Not a valid month, please choose from January, February, March, April, May, June or All")
    #we're ready to exit the loop.
    while True:
        day = input('What day of the week would you like to analyze? Sunday, Monday, etc: ').lower()
        if day in (days):
            print('You selected: ', day)
            break
        else:
            print("Not a valid day, please choose Sunday, Monday,etc: ")
    #we're ready to exit the loop.
    #================================================================================
    print('-'*40)
    print(city,month,day)
    return city, month, day

def load_data(city, month, day):
    global df  #tl7929
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day'] = pd.to_datetime(df['Start Time']).dt.day_name()
    df['hour'] = df['Start Time'].dt.hour
    print(CITY_DATA[city])
    print(df['Start Time'].dt.month)
    print(pd.to_datetime(df['Start Time']).dt.day_name())
    print(df['Start Time'].dt.hour)
    try:
        if month != 'all':
            months = ['january', 'february', 'march', 'april', 'may', 'june']
            month = months.index(month) + 1
            df = df[df['month'] == month]
        if day != 'all':
            days = ['sunday','monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
            day = days.index(day) + 1
            df = df[df['day'] == day]
            # tl7929
    except ValueError:
        print("Oops!")
        print("value error")
        return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time=time.time()
    # TO DO: display the most common month
    print("Most Common Month: ", df['month'].mode().to_frame())
    # TO DO: display the most common day of week
    print('Most Common Day: ', df['day'].mode().to_frame())
    # TO DO: display the most common start hour
    print('Most common Hour:', df['hour'].mode().to_frame())
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)




def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    # TO DO: display most commonly used start station
    print('Most popular start station: ', df['Start Station'].mode().values[0])
    # TO DO: display most commonly used end station
    print('Most popular end station: ', df['End Station'].mode().values[0])
    # TO DO: display most frequent combination of start station and end station trip
    print('Most popular station combination: ', (df['Start Station']+df['End Station']).mode().values[0])
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    return df

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    # TO DO: display total travel time
    print('Total travel time: ' + str(df['Trip Duration'].sum()))
    # TO DO: display mean travel time
    print('Average travel time: ', df['Trip Duration'].mean())
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""
    print('\nCalculating User Stats...\n')
    start_time = time.time()
    print("Started at " + str(start_time))
    # TO DO: Display counts of user types
    print(df["User Type"].value_counts().to_frame())
    # TO DO: Display counts of gender
    if CITY_DATA[city] != 'washington.csv':
        print(df['Gender'].value_counts().to_frame())
        print('Oldest year born: ', df["Birth Year"].min())
        print('Newest year born: ',df["Birth Year"].max())
        print('Most Common year born: ', df["Birth Year"].mode())
    else:
        print('\nSorry Gender and Birth Year not available in Washington\n')
    # TO DO: Display earliest, most recent, and most common year of birth
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def main():
    while True:
        city, month, day = get_filters()
        load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        disp_data = input('\nDo you want to see 5 lines of Raw Data? Yes or No\n').lower()
        if disp_data != 'yes':
            print('You have selected not to see raw data')
        else:
            print(df.head(5))
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
if __name__ == "__main__":
    main()
# end of program notice
