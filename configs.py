from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "29691422"))
    API_HASH = getenv("API_HASH", "7c2435a38e1c9f7417f62a5497db767a")
    BOT_TOKEN = getenv("BOT_TOKEN", "7175703585:AAHMGHu_ggfNh1D5EZakddJ0OeKK80AI5uI")

config = Config()
