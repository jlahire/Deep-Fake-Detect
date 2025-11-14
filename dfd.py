# Deep fake detector for free tier reality defender API

import os
import sys
import asyncio 
from realitydefender import RealityDefender
from dotenv import load_dotenv
from pathlib import Path


class DeepfakeDetector:
    
    audio = ['.mp3', '.wav', '.m4a', '.flac', '.alac']
    image = ['.jpg', '.jpeg', '.png', '.gif', '.webp']


    def __init__(self, apiKey):
        self.apiKey = apiKey
        self.client = None

    def checkFile(self, filePath):
        if not os.path.exists(filePath):
            print(f"file {filePath} not found...")
            return False
        
        fileExt = Path(filePath).suffix.lower()
        supported = self.audio + self.image

        if fileExt not in supported:
            print(f"file ext {fileExt} not supported...")
            print(f"supported ext are: {', '.join(supported)}")
            return False
        return True


    async def analyze(self, filePath):
        pass # async api call

    def results(self, result):
        pass # display results

    def score(self, score):
        pass # translate score

    
class Applicaiton:

    def __init__(self):
        self.apiKey = None
        self.detector = None

    def getAPI(self): # grab api from .env
        load_dotenv()
        apiKey = os.getenv("REALITY_DEFENDER_API_KEY")
        return apiKey

    def getFile(self):
        pass # read cli input

    async def run(self):
        pass # obvious....... -_-


def main():
    app = Applicaiton()
    asyncio.run(app.run())

if __name__ == "__main__":
    main()