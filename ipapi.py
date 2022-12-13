from flask import Flask, request


app = Flask(__name__)

@app.route('/')

def hello():
    url = str(input("enter url:"))



    headers = {
    "accept": "application/json",
    "x-apikey": "d0f2258cb348dd4d47b59f40e191e8003dbba66f15c1778eec0ec9462aa7558d"
    }
 
    response = request.get( "https://www.virustotal.com/api/v3/domains/%s" %url, headers=headers)

    print(response)


app.run()