# speech-raspberry
---

Script for record a wav audio and transcript for send action to little server 
in a raspberry pi3.

## Requirements

* python >= 3.6
* gcloud credentials (speech-to-text api enabled).
## Env vars

load env vars from .envrc file

## Files

* app.py: main script file
* voice_record.py: implement record voice with microphone
* gcloud_speech_text.py: implement send wav file and return text. 

## Run:

```bash
$ pip3 install -r requirements.txt

$ python3 app.py
```

## Authors:

* Fabio Moreno <fabiomoreno@outlook.com>