import os
from datetime import datetime, timedelta
import shutil
import random 

def makeCommits (days : int):
    if days < 1:
        os.system('git push')
        return 0
    else:
        dates = f"{days} days ago"
        d = datetime.today() - timedelta(days=days)
        year = d.strftime("%Y")
        month = d.strftime("%m")
        day = d.strftime("%d")
        fileName = 'Log_'+str(day+'-'+month+'-'+year)+'.txt'

        logFile = open(fileName,"w+")
        shutil.copy('log.txt', fileName)
        logFile.write(str(day+'-'+month+'-'+year)+' '+str(random.randint(1, 1000)))
        logFile.close()
       

        # staging 
        os.system('git add '+fileName)
        # commit 
        os.system('git commit --date="'+ dates +'" -m "Test & Log Report"')
        diff = random.randint(1, 45)
        return days+makeCommits(days - diff)

n = 10
while(n>0):
    makeCommits(512)
    n=n-1; 
