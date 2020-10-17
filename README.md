# Cloud Computing and Cyber Security - Homework 2

The web app provides news to clients based on their geolocation.

![](https://i.imgur.com/Z15JNv5.png)
Server initiates request to Google cloud function with client's IP address. The cloud function gets the location of the IP and returns the news based on the location.

## Usage
```bash
$ python ./app.py
```
(The function won't work locally. It must be deployed on some server and accessed remotely.)

## Files
* app.py: The flask server source file
* ./templates/index.html: template html file
* function-source.zip: Lambda function source files