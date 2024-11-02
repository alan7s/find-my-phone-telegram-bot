from datetime import datetime
import dropbox
import geojson
import telebot
import re

##Dropbox config##
DROPBOX_APPKEY = ''
DROPBOX_APPSECRET = ''
DROPBOX_REFRESH_TOKEN = ''
GEOJSON_PERSON_A_PATH = '/Aplicativos/GPSLogger for Android/file_YYYY-MM-DD.geojson'
GEOJSON_PERSON_B_PATH = ''
GEOJSON_PERSON_C_PATH = ''

##Telegram config##
TELEGRAM_API = ''
CHAT_ID = ''

##BOT config##
FORMAT_TIME = '%d/%m/%Y %H:%M'
DEFAULT_MENU_TEXT = """Hi, I'm a GPSLogger Bot!
Click on an option to continue:
/getPersonA location
/getPersonB location
/getPersonC location
"""

bot = telebot.TeleBot(TELEGRAM_API)

def get_geojson_from_dropbox(file_path):
    dbx = dropbox.Dropbox(
        app_key=DROPBOX_APPKEY,
        app_secret=DROPBOX_APPSECRET,
        oauth2_refresh_token=DROPBOX_REFRESH_TOKEN
    )
    
    try:
        metadata, response = dbx.files_download(file_path)
        geojson_content = response.content.decode('utf-8')
        return geojson.loads(geojson_content)
    
    except dropbox.exceptions.ApiError as err:
        print(f"Error accessing Dropbox: {err}")
        return None

def get_last_feature(geojson_data):
    if "features" in geojson_data and geojson_data["features"]:
        return geojson_data["features"][-1]
    else:
        print("No features found in GeoJSON")
        return None

def init_dropbox(geojon_file_path):
    geojson_data = get_geojson_from_dropbox(geojon_file_path)

    if geojson_data:
        last_feature = get_last_feature(geojson_data)
        if last_feature:
            longitude = last_feature["geometry"]["coordinates"][0]
            latitude = last_feature["geometry"]["coordinates"][1]
            accuracy = last_feature["properties"]["accuracy"]
            altitude = last_feature["properties"]["altitude"]
            time = datetime.fromisoformat(last_feature["properties"]["time"]).strftime(FORMAT_TIME)

    return latitude, longitude, accuracy, altitude, time

def getLOG(geojon_file_path):
    current_date = datetime.now().strftime("%Y-%m-%d")
    new_filename = re.sub(r'\d{4}-\d{2}-\d{2}', current_date, geojon_file_path)

    lat, lon, acc, alt, time = init_dropbox(new_filename)
    description = f"""Location {lat},{lon}
Last seen {time} | Altitude {alt} | Accuracy {acc}"""
    bot.send_location(chat_id=CHAT_ID,latitude=lat,longitude=lon)
    bot.send_message(chat_id=CHAT_ID,text=description)

@bot.message_handler(commands=["getPersonA"])
def getLOG_1(message):
    getLOG(GEOJSON_PERSON_A_PATH)

@bot.message_handler(commands=["getPersonB"])
def getLOG_2(message):
    bot.send_message(chat_id=CHAT_ID,text="Not setup yet")

@bot.message_handler(commands=["getPersonC"])
def getLOG_3(message):
    bot.send_message(chat_id=CHAT_ID,text="Not setup yet")

def verify_msg(message):
    return True

@bot.message_handler(func=verify_msg)
def default_response(message):
    #print(message.chat.id) #Print your CHAT_ID after interact with the BOT
    bot.send_message(chat_id=CHAT_ID,text=DEFAULT_MENU_TEXT)

def main():
    print("Bot server running...")
    bot.polling()

if __name__ == "__main__":
    main()
