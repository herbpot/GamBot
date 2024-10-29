import requests, logging
from schema import Diary, User

logger = logging.getLogger("notion")
logger.addHandler(logging.FileHandler('./notion.log'))
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.DEBUG)
class Notion:
    url = "http://localhost:8010"

    def setDiary(data:Diary):
        logger.info(f"data: {data.__dict__}")
        requests.post(Notion.url + "/diary/set",{},{
            "title": data.title,
            "context": data.context,
            "files": data.files,
            "userId": data.user
        })

    def checkDatabase(data:str):
        logger.info(f"checking db id [{data}]")
        res = requests.post(Notion.url+"/setting/verificate", {}, {
            "dId": data
        })
        return res.json()