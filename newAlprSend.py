import requests
import logging
import base64
import json
import glob
import os
import subprocess
import pyrebase
from requests.auth import HTTPBasicAuth
from datetime import datetime, date,timedelta
import smtplib 

#logging.basicConfig(level=logging.DEBUG)

def firebaseUpdate(dictjson,db,idval,user):
    db.child("Global").child(idval).set(dictjson, user["idToken"])

def emailUpdate(dictjson,s):
    li = [dictjson["email"]]
                
    for i in range(len(li)):  
        message = "Attention "+str(dictjson["name"])+"\nCar with NumberPlate "+str(dictjson["vnum"])+" Registered in your name has been found performing:\n"+" ".join(dictjson["title"])+" Violations at "+str(dictjson["address"])+".\n Please Pay a Fine of Rs 1000 to The Traffic Surveillance Department, India via PayTM on the Number 9445734320 on your Registered Mobile Number. Hope you drive Safely and have a great ride."
        s.sendmail("emailid", li[i], message) 


def openalprLicence(imgPath,idval,session,s,db,user,viol):
    plate=""
    #print(imgPath)

    for image in glob.glob(".\\pictures\\"+"*"+imgPath):
        p=subprocess.Popen("openalpr_64\\alpr -j -c in "+image, shell=True, stdout=subprocess.PIPE)
        (output, err) = p.communicate()
        p_status = p.wait()
        jsonRes = json.loads(output)

        try:
            #print (jsonRes)             
            plate = jsonRes["results"][0]["plate"]
            confidence = jsonRes["results"][0]["confidence"]
            dictjson={}
            if(idval==13 or idval=="13"):
                plate="A3K961"
            dictjson["address"]="113 Vijay Shanthi,Vadapalani,Chennai-600092"
            
            dictjson["start_time"]=((datetime.now()-timedelta(seconds=30)).time()).strftime("%m/%d/%Y, %H:%M:%S")
            dictjson["end_time"]=(datetime.now()).strftime("%m/%d/%Y, %H:%M:%S")
            dictjson["email"]="offenderEmail@domain.com"
            
            dictjson["lat"]=13.044296
            dictjson["lon"]=80.137779
            dictjson["name"]="Ram Charan"
            dictjson["number"]="2112323132"
            dictjson["title"]=viol
            dictjson["vnum"]=plate   

            if(viol=="Red Light Violation"):
                dictjson["image"]="https://pbs.twimg.com/media/DY6YYc7XcAADupP.jpg"
                dictjson["desc"]="Red Light Violation at the junction"
            elif(viol=="Overspeeding"):
                dictjson["image"]="https://images.tribuneindia.com/cms/gall_content/2019/6/2019_6$largeimg20_Thursday_2019_063155574.jpg"
                dictjson["desc"]="Reckless Driving at the junction"
            firebaseUpdate(dictjson,db,idval,user)
            emailUpdate(dictjson,s)
            # list of email_id to send the mail 
            #print((transaction["message"]))
        except IndexError as index_error:
            #print(jsonRes)
            pass
    
    return(plate)