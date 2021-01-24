# Raspberry Pi Print Server

This is an api server that prints documents sent through an endpoint. The target environment is tested specifically for a raspberry pi. 

## Prequesites 
Be sure your raspberry pi is configured to print documents. The 'lp fileToPrint' command is executed, and will target whatever the default printer used is.

Follow this Guide:
https://www.howtogeek.com/169679/how-to-add-a-printer-to-your-raspberry-pi-or-other-linux-computer/

## Installation
0. Move profiles/dev.env to the root folder. Rename new file in root to .env

1. Navigate to root directory. Install dependencies
```
pip3 install -r requirements.txt
```

2. Run the server. This will locally host on port 8000
```
python3 manage.py runserver
```

Alternatively, its likely the case you will be sending data to pi through another device. In this case, you'll need to add your raspberry pi's ip address to 'mysite/settings.py'
```
ALLOWED_HOSTS = ["raspberry.pi.ip.address"]
```
Then in the root directory, run your server with
```
python3 manage.py runserver 0.0.0.0:8000
```

## API Endpoints
Once the server is running at 'rpi-ip-address:port', the following endpoints are available
```
POST 'rpi-ip-address:port'/printer/print

{
    "fileToPrint": <b64-encoded-string>
}
```