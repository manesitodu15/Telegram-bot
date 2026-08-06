import os

print("BOT_TOKEN existe :", "BOT_TOKEN" in os.environ)
print("Variables :", list(os.environ.keys()))
TOKEN = os.environ["BOT_TOKEN"]
