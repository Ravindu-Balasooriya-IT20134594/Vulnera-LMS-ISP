from flask import Flask, render_template, request, url_for
import requests
app = Flask(__name__)

@app.route("/form",methods=["GET","POST"])
def testurl():


    url = str(input("enter url: "))

    headers = {
        "accept": "application/json",
        "x-apikey": "d0f2258cb348dd4d47b59f40e191e8003dbba66f15c1778eec0ec9462aa7558d"
    }

    response = requests.get("https://www.virustotal.com/api/v3/domains/%s" %url, headers=headers)
    urlfromreq = response.json()["data"]["attributes"]["last_analysis_stats"]

         #print(urlfromreq)


    # totalenginecount = 0
    # totalenginesdetectedcount = 0
    # resultengines =[]
    # enginenames =[]
            
    # for i in urlfromreq:
    #     totalenginecount = totalenginecount + 1
    #     if urlfromreq[i]["malicious"] == "malicious" or urlfromreq[i]["category"] == 'suspicious':
    #         resultengines.append(urlfromreq[i]["result"])
    #         enginenames.append(urlfromreq[i]["engine_name"])
    #         totalenginesdetectedcount = totalenginesdetectedcount + 1
            
    #     if totalenginesdetectedcount > 0:
    #         return("The " + str(url) + " is rated as unsafe on " + str(totalenginesdetectedcount) + " engines out of " + str(totalenginecount) + " engines.") 
    #         #return ("success")
    #         #return (resultengines)

    #     elif totalenginesdetectedcount > -1:
    #         return("The " + str(url) + " is rated as Safe on " + str(totalenginecount) + " engines.")
    #         #return("success")
    #         #return(resultengines)

    # #response = requests.get(response.json())

    return(response.json())

app.debug =True

app.run()

