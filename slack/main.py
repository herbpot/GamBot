from venv import logger
from slack_sdk import WebClient
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from slack_bolt.context.say.say import Say
from dotenv import load_dotenv
from schema import *
from .interfaces.notion.main import Notion

import os
import logging
load_dotenv()

client = WebClient(token=os.environ.get("SLACK_BOT_TOKEN"))
app = App(
    token=os.environ.get("SLACK_BOT_TOKEN"),
    signing_secret=os.environ.get("SLACK_SIGNING_SECRET")
)

logger.setLevel(logging.DEBUG)
logger.addHandler(logging.FileHandler("./slackBot.log"))
logger.addHandler(logging.StreamHandler())

channelId = ""

@app.command('/setup-db')
def setupDB(ack, respond, command):
    ack()
    userId = command['user_id']
    dbId = command['text']
    User(userId, dbId).save()
    logger.info(f"save [{dbId}] to [{userId}]")
    respond(f"your Notion DB is {dbId}")

@app.event("app_mention")
def bot_mention(event:dict, say: Say):
    user = event['user']
    u = User.find_one({"_id":user})
    if u:
        logger.debug(u)
        data = event['text'].replace("<@U07T4SM8NKY>", "")
        if "files" in event.keys():
            img_links = list(map(lambda x: x['url_private'], event['files']))
        else:
            img_links = []
        di = Diary(u, data,img_links)
        di.save()
        Notion.setDiary(di, u)
        logger.info(f"{event}")

if __name__ == "__main__":
    SocketModeHandler(app, os.environ.get("SLACK_APP_TOKEN")).start()