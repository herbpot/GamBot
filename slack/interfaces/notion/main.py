import requests
from ...schema import Diary, User

class Notion:
    url = "http://localhost:8010"

    def setDiary(data:Diary, user: User):
        requests.post(Notion.url + "/diary/set",{
            "title": data.title,
            "content": data.context,
            "files": data.files
        })