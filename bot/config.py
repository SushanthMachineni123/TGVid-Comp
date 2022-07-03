#    Copyright (c) 2021 Danish_00
#    Improved By @Zylern

from decouple import config

try:
    APP_ID = config("5441410", cast=int)
    API_HASH = config("a1a4fe7d23328f419d98a58339fd9980")
    BOT_TOKEN = config("5022902763:AAGamn2-frpgka0xrAiZjULMX7A7YVfNTTo")
    DEV = 1664850827
    OWNER = config("1451257129")
    ffmpegcode = ["ffmpeg -i '''{}''' -map 0 -c:v libx264 -crf 30.5 -preset veryfast -pix_fmt yuv420p -s 846x480 -c:a libopus -ac 2 -ab 32k -c:s copy '''{}''' -y]
    THUMBNAIL = config("THUMBNAIL", default="https://telegra.ph/file/f9e5d783542906418412d.jpg")
except Exception as e:
    print("Environment vars Missing! Exiting App.")
    print(str(e))
    exit(1)
