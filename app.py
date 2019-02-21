from gcloud_speech_text import GcloudSpeechText
from voice_record import VoiceRecord
import time
import os
import requests
import json_tricks

ip = os.getenv("raspberry_ip")
headers = {
    'content-type': 'application/json',
    'Accept-Charset': 'UTF-8'
}

if ip is None:
    print("Define la ip de la raspberry en el archivo .envrc y ejecute:\nsource .envrc")
    exit(1)

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

while(True):
    print("enter para grabar orden, 'q' para salir.")
    s = input()
    if s == "q":
        break

    print("grabando (3seg)...")
    record = VoiceRecord()
    file_name = "test"+str(time.time())+".wwav";
    if record.record(file_name):
        print("pasando orden a texto...")
        speech = GcloudSpeechText()
        text = speech.get_text(file_name)
        cls()
        print("enviando orden: ",text)
        payload = json_tricks.dumps({
            'action': text
        })
        url = "http://"+ip+"/api/action"
        response = requests.post(url=url, data=payload,headers=headers).json()
        print("raspberry responde: \n", str(response))

print("Exit script.")
exit(0)