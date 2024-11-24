# Find My Phone Telegram BOT

This project is a Telegram bot to access location data stored in Dropbox as GeoJSON files from GPSLogger app. The bot allows users to query the latest location information for different individuals.

## Features

- Retrieves location information from GeoJSON files in Dropbox.
- Sends the last recorded location to Telegram, including details such as:
  - Latitude and Longitude
  - Altitude
  - Accuracy
  - Last update
- Interactive menu with configurable commands for different users.

## Configuration

### Prerequisites

- GPSLogger configured.
- Dropbox account with an app set up.
- Telegram bot configured, and token obtained.

### Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/alan7s/find-my-phone-telegram-bot
   cd find-my-phone-telegram-bot

2. Install dependencies:
   ```bash
   pip install dropbox geojson telebot

3. Configure the variables in the code:
- Dropbox:
  - DROPBOX_APPKEY: Dropbox app key.
  - DROPBOX_APPSECRET: Dropbox app secret.
  - DROPBOX_REFRESH_TOKEN: OAuth2 refresh token.
- Telegram:
  - TELEGRAM_API: Telegram bot token.
  - CHAT_ID: Chat ID where messages will be sent.
- GeoJSON Paths:
  - Paths to the GeoJSON files in Dropbox:
    - GEOJSON_PERSON_A_PATH
    - GEOJSON_PERSON_B_PATH
    - GEOJSON_PERSON_C_PATH

4. Start the bot:
   ```bash
   python bot-server.py

## Usage

### Available Commands
  - /getPersonA: Retrieves the last recorded location for Person A.
  - /getPersonB: (Pending configuration).
  - /getPersonC: (Pending configuration).

### Default Response
The bot displays the menu with available options if the sent command is not recognized.

## Contribution
Contributions are welcome! Feel free to open issues or submit pull requests. perl Copiar código
