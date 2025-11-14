# Deep fake detector for free tier reality defender API

import os
import sys
import asyncio 
from realitydefender import RealityDefender



class DeepfakeDetector:
    

    def __init__(self, apiKey):
        self.apiKey = apiKey
        self.client = None

    def checkFile(self, filePath):
        pass # validate file

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

    def getAPI(self):
        pass # grab api

    def getFile(self):
        pass # read cli input

    async def run(self):
        pass # obvious....... -_-


def main():
    app = Applicaiton()
    asyncio.run(app.run())

if __name__ == "__main__":
    main()