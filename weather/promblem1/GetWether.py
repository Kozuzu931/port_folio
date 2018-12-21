import requests
import json
import sys
import sqlite3
import datetime
import pandas as pd

# Arguments error blocck
select_date = sys.argv
if len(select_date) <= 1 and len(select_date) <= 2:
    raise ArgumentsError("Short of arguments. must need to 2 arguments YearMonth(YYMM) and HourMinute(HHmm) ex.20180101 1500")
elif len(str(select_date[1])) !=   8 and len(str(select_date[2])) !=   4:
    raise ValueError("invalid value error")


# api propaty
API_KEY = "ccfb0fd6db35eaf936907c745ebee993"
Poly_ID = "5c0f769ab83b0a000999031d"
api = "http://api.openweathermap.org/data/2.5/forecast?id={city}&APPID={key}"
city_ID = [1850144, 1853909]
date_format = "{year}-{month}-{date} {hour}:{minutes}:00".format(year=select_date[1][0:4], month=select_date[1][4:6], date=select_date[1][6:8], hour=select_date[2][:2], minutes=select_date[2][2:])

# country_name = "JP"
# city_name = ["Tokyo", "Osaka-shi"]

 # get json data from open weather map firecast api
url_tokyo = api.format(city = city_ID[0], key = API_KEY)
url_osaka = api.format(city = city_ID[1], key = API_KEY)

response_tokyo = requests.get(url_tokyo)
response_osaka = requests.get(url_osaka)
data_tokyo = json.loads(response_tokyo.text)
data_osaka = json.loads(response_osaka.text)

tokyo = json.loads(response_tokyo.text)
osaka = json.loads(response_osaka.text)

# formating json data to pandas DataFrame 
df_tokyo = pd.io.json.json_normalize(tokyo["list"])
df_osaka = pd.io.json.json_normalize(osaka["list"])
pre_weather_t = pd.DataFrame([df_tokyo["weather"][i][0] for i in range(len(df_tokyo["weather"]))])
pre_weather_o = pd.DataFrame([df_osaka["weather"][i][0] for i in range(len(df_osaka["weather"]))])
df_tokyo = df_tokyo.drop("weather", axis=1)
df_osaka = df_osaka.drop("weather", axis=1)

# reshape DataFrame for sqlite3
for_deploy_df_tokyo = pd.concat([df_tokyo, pre_weather_t], axis=1)
for_deploy_df_osaka = pd.concat([df_osaka, pre_weather_o], axis=1)

connect = sqlite3.connect("weather")
cur = connect.cursor()

# deploy sqlite3
for_deploy_df_tokyo.to_sql("Tokyo", con=connect, if_exists="replace")
for_deploy_df_osaka.to_sql("Osaka", con=connect, if_exists="replace")

connect.commit()
connect.close()

connect = sqlite3.connect("weather")
tokyo_sql = pd.read_sql("SELECT * FROM Tokyo", con=connect)
osaka_sql = pd.read_sql("SELECT * FROM Osaka", con=connect)
pd.set_option("display.max_rows", 100)
print("Tokyo\n\n", tokyo_sql[tokyo_sql.dt_txt == date_format])
print("Osaka\n\n", osaka_sql[osaka_sql.dt_txt == date_format])

connect.close()
