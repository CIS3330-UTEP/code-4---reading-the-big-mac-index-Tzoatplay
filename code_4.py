import csv
import pandas as pd
big_mac_file = './big-mac-full-index.csv'
df = pd.read_csv(big_mac_file)
# print(df)


def get_big_mac_price_by_year(year,country_code):
    year = 2018
    query_text = f"((date >='{year}-01-01' and date <= '{year}-12-31'))"
    df_result = df.query(query_text)
    df_filter = df_result[df_result['iso_a3'].str.lower() == country_code.lower()]
    mean_price = df_filter['dollar_price'].mean()
    return round(mean_price, 2)

def get_big_mac_price_by_country(country_code):
    query_text = "(date >= '2000-01-01')"
    df_result = df.query(query_text)
    df_filter = df_result[df_result['iso_a3'].str.lower() == country_code]
    mean_price = df_filter['dollar_price'].mean()
    return round(mean_price, 2)

def get_the_cheapest_big_mac_price_by_year(year):
  query_text = f"(date >= '{year}-01-01' and date <= '{year}-12-31')"
  df_result = df.query(query_text)
  min_price_row = df_result[df_result['dollar_price'] ==df_result['dollar_price'].min()].iloc[0]
  country_name = min_price_row['name']
  country_code = min_price_row['iso_a3']
  dollar_price = min_price_row['dollar_price']
  result = f"{country_name}({country_code}): ${round(dollar_price, 2)}"
  return result


def get_the_most_expensive_big_mac_price_by_year(year):
    query_text = f"(date >= '{year}-01-01' and date <= '{year}-12-31')"
    df_result = df.query(query_text)
    max_price_row = df_result[df_result ['dollar_price'] == df_result['dollar_price'].max()].iloc[0]
    country_name = max_price_row['name']
    country_code = max_price_row['iso_a3']
    dollar_price = max_price_row['dollar_price']
    result = f"{country_name}({country_code}): ${round(dollar_price, 2)}"
    return result

if __name__ == "__main__":
   print("Average Big Mac Price 2016 USA:" ,get_big_mac_price_by_year(2018, 'usa'))
   print("Average Big Mac Price USA:" ,get_big_mac_price_by_country('usa'))
   print("Cheapest Big Mac 2004:",get_the_cheapest_big_mac_price_by_year(2004) )
   print("Most Expensive Big Mac 2004:" ,get_the_most_expensive_big_mac_price_by_year(2004))
