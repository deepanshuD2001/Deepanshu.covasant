import os
import datetime

class File:
    def __init__(self, path="."):
        self.path = path

    def getMaxSizeFile(self, n=1):
        files = [f for f in os.listdir(self.path) if os.path.isfile(os.path.join(self.path, f))]
        files.sort(key=lambda f: os.path.getsize(os.path.join(self.path, f)), reverse=True)
        return files[:n]

    def getLatestFiles(self, after_date):
        files = [f for f in os.listdir(self.path) if os.path.isfile(os.path.join(self.path, f))]
        return [
            f for f in files
            if datetime.date.fromtimestamp(os.path.getmtime(os.path.join(self.path, f))) > after_date
        ]

import datetime
from pkg.file import File

fs = File(".")
print(fs.getMaxSizeFile(2)) 
print(fs.getLatestFiles(datetime.date(2018, 2, 1))) 
