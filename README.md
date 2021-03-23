# waze-bot

Bot built with Selenium to get max speed connecting with waze API

## Prerequisites

Selenium 3.141.0 or later

## Run Bot

For run the bot, first you must configure the bounding boxes filename and waze credentials in bot.py file and run this command: 

```sh
python bot.py
```

A firefox window will open and you must to solve the captcha in 90 seconds (you can to modify this value anyway) or less, finally a json file will be created with the segments from Waze API

## Load the segments

You must configure the segment json filename in loader.py and run the following commands:

```sh
docker build -t waze-bot .
docker run --rm -it waze-bot python loader.py
```