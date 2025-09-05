import pandas as pd

def load_and_preview_data(file_path):
    # Загрузка данных
    df = pd.read_csv('ncr_ride_bookings.csv')


    print("Первые 5 строк датасета:")
    print(df.head())

    print("\nОбщая информация о датасете:")
    print(df.info())

    print("\nСтатистическое описание числовых столбцов:")
    print(df.describe())

    print("\nКоличество строк и столбцов:")
    print(df.shape)

    return df

def filter_data(df):

    selected_columns = ['Booking ID', 'booking_datetime', 'Booking Status', 'Vehicle Type', 'Payment Method']
    selected_df = df(selected_columns)
    print("Первые 5 строк выбранных столбцов:")
    print(selected_df.head())


    cancelled_by_driver = df[df['Booking Status'] == 'Cancelled by Driver']
    print("\nБронирования, отмененные водителем:")
    print(cancelled_by_driver)


    auto_high_value = df[(df['Vehicle Type'] == 'Auto') & (df['Booking Value'] > 500)]
    print("\nБронирования с Vehicle Type 'Auto' и Booking Value больше 500:")
    print(auto_high_value)


    df['booking_datetime'] = pd.to_datetime(df['booking_datetime'])
    march_2024_bookings = df[(df['booking_datetime'] >= '2024-03-01') & (df['booking_datetime'] <= '2024-03-31')]
    print("\nБронирования, сделанные в марте 2024 года:")
    print(march_2024_bookings)

# Использование функций
file_path = 'uber_rides_bookings.csv'
df = load_and_preview_data(file_path)
filter_data(df)
