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
        if not self.checkFile(filePath):
            return
        
        print("starting...")
        self.client = RealityDefender(api_key=self.apiKey)

        try:
            uploadResponse = await self.client.upload(file_path=filePath)
            requestId = uploadResponse["request_id"]
            result = await self.client.get_result(requestId)
            self.results(result, filePath, requestId)

        except Exception as error:
            print(f"error: {error}")

    def results(self, result, filePath, requestId):
        
        print("\n" + "="*10)

        fileName = Path(filePath).name
        status = result.get("status", "unknown")
        score = result.get("score", "n/a")

        print(f"File: {fileName}")
        print(f"Status: {status}")
        print(f"Score: {score}")
        print(f"Request ID: {requestId}")

        if 'models' in result:
            for model in result["models"]:
                modelName = model.get("model_name", "n/a")
                modelScore = model.get("score", "n/a")
                modelStatus = model.get("status", "n/a")
                print(f"{modelName}: score={modelScore}, status={modelStatus}")
        
        print("="*10)
        self.score(score)
        

    def score(self, score):
        if isinstance(score, str):
            print("str return instead of int/float...")
            return
        if score < 0.3:
            print("result: LIKELY AUTHENTIC")
        elif 0.3 <= score < 0.7:
            print("result: UNCERTAIN")
        else:
            print("result: LIKELY DEEPFAKE")

    
class Application:

    def __init__(self):
        self.apiKey = None
        self.detector = None

    def getAPI(self):
        load_dotenv()
        apiKey = os.getenv("REALITY_DEFENDER_API_KEY")
        if not apiKey:
            print("no api key found in .env...")
            return None
        return apiKey

    def getFile(self):
        if len(sys.argv) < 2:
            print("usage: python dfd.py <file_path>")
            return None
        return sys.argv[1]

    async def run(self):
        self.apiKey = self.getAPI()
        if not self.apiKey:
            return
        
        filePath = self.getFile()
        if not filePath:
            return

        self.detector = DeepfakeDetector(self.apiKey)
        await self.detector.analyze(filePath)

def main():
    app = Application()
    asyncio.run(app.run())

if __name__ == "__main__":
    main()