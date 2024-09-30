import os

class Config(object):
    TG_BOT_TOKEN = os.environ.get("BOT_TOKEN", "7490926656:AAHG-oUUzGPony9xfyApSI0EbbymhneDU1k") # Make a bot from https://t.me/BotFather and enter the token here
    
    APP_ID = int(os.environ.get("API_ID", 22420997)) # Get this value from https://my.telegram.org/apps
    
    API_HASH = os.environ.get("API_HASH", "d7fbe2036e9ed2a1468fad5a5584a255") # Get this value from https://my.telegram.org/apps
    
    OWNER_ID = int(os.environ.get("OWNER_ID", None)) # Your(owner's) telegram id
    
    MONGO_STR = os.environ.get("MONGO_STR", "mongodb+srv://chaiwala:autqio99wvMJEr0l@cluster0.nupdo.mongodb.net/chai?retryWrites=true&w=majority") # Get from MongoDB Atlas

    DOWNLOAD_LOCATION = "app//DOWNLOADS//" # The download location for users. (Don't change anything in this field!)
