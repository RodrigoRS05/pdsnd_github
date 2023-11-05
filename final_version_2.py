import pandas as pd
import time

# Define data files for each city
CITY_DATA = {
    'chicago': 'C:/Users/rruan/Desktop/UDACITY/project_Python/project/chicago.csv',
    'new york city': 'C:/Users/rruan/Desktop/UDACITY/project_Python/project/new_york_city.csv',
    'washington': 'C:/Users/rruan/Desktop/UDACITY/project_Python/project/washington.csv'
}

def get_filters():
    print('Hello! Let\'s explore some US bikeshare data!')
    
    # Handle city input
    while True:
        city = input("Which city's data would you like to view? Chicago, New York City, or Washington? ").lower()
        if city in ['chicago', 'new york city', 'washington']:
            break
        else:
            print("Invalid city. Please enter either Chicago, New York City, or Washington.")

    month = input("Which month would you like to filter by? January, February, March, April, May, June, or type 'all' if you do not have any preference? ").lower()
    day = input("Which day would you like to filter by? Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday or type 'all' if you do not have any preference? ").lower()

    return city, month, day

def load_data(city, month, day):
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    most_common_month = df['Start Time'].dt.month.mode()[0]
    most_common_day = df['Start Time'].dt.day_name().mode()[0]

    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df, most_common_month, most_common_day

def display_data(df):
    view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n').lower()
    start_loc = 0
    while view_data == 'yes':
        print(df.iloc[start_loc:start_loc+5])
        start_loc += 5
        view_data = input("\nDo you wish to view the next 5 rows? Enter yes or no: ").lower()

def station_stats(df):
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    common_start_station = df['Start Station'].mode()[0]
    print('Most Common Start Station:', common_start_station)
    
    common_end_station = df['End Station'].mode()[0]
    print('Most Common End Station:', common_end_station)

    df['Start End Combination'] = df['Start Station'] + ' to ' + df['End Station']
    common_combination = df['Start End Combination'].mode()[0]
    print('Most Frequent Start-End Combination:', common_combination)

    print("\nThis took %s seconds." % (time.time() - start_time))

def trip_duration_stats(df):
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    total_duration = df['Trip Duration'].sum()
    print('Total Duration:', total_duration)

    average_duration = df['Trip Duration'].mean()
    print('Average Duration:', average_duration)

    print("\nThis took %s seconds." % (time.time() - start_time))

def user_stats(df):
    print('\nCalculating User Stats...\n')
    start_time = time.time()

    print('User Types:\n', df['User Type'].value_counts())

    if 'Gender' in df.columns:
        print('\nGender Breakdown:\n', df['Gender'].value_counts())

    if 'Birth Year' in df.columns:
        print('\nEarliest Year of Birth:', int(df['Birth Year'].min()))
        print('Most Recent Year of Birth:', int(df['Birth Year'].max()))
        print('Most Common Year of Birth:', int(df['Birth Year'].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))

def main():
    while True:
        city, month, day = get_filters()
        df, most_common_month, most_common_day = load_data(city, month, day)
        print(f"The most common month is: {most_common_month}")
        print(f"The most common day of the week is: {most_common_day}")

        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
    main()
