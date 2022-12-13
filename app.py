from flask import Flask, render_template, request, url_for
import requests
import subprocess as sp 
app = Flask(__name__)


@app.route("/")
def ini():
    return render_template("index.html")

@app.route("/form",methods=["GET","POST"])
def abc():

    if request.method == 'POST':
        ip_address=request.form['firstname']

        headers = {
        "accept": "application/json",
        "x-apikey": "d0f2258cb348dd4d47b59f40e191e8003dbba66f15c1778eec0ec9462aa7558d"
        }
    
        response = requests.get( "https://www.virustotal.com/api/v3/ip_addresses/%s" %ip_address, headers=headers)
        outfromreq = response.json()["data"]["attributes"]["last_analysis_results"]

        #print(outfromreq)


        totalenginecount = 0
        totalenginesdetectedcount = 0
        resultengines = []
        enginenames = []
            
        for i in outfromreq:
            totalenginecount = totalenginecount + 1
            if outfromreq[i]["category"] == "malicious" or outfromreq[i]["category"] == 'suspicious':
                resultengines.append(outfromreq[i]["result"])
                enginenames.append(outfromreq[i]["engine_name"])
                totalenginesdetectedcount = totalenginesdetectedcount + 1
            
        if totalenginesdetectedcount > 0:
            #return("The " + str(ip_address) + " is rated as unsafe on " + str(totalenginesdetectedcount) + " engines out of " + str(totalenginecount) + " engines.") 
            return render_template ("threatip.html")
        elif totalenginesdetectedcount > -1:
            #return("The " + str(ip_address) + " is rated as Safe on " + str(totalenginecount) + " engines.")
            return render_template("nonthreatip.html")


        #print(request.form.get("firstname"))


    return render_template("form.html")

@app.route("/xss")
def xss():
    return render_template("xss.html")


@app.route("/xsslow")
def xsslower():
    out = sp.run(["php, xss-low.php"], stdout=sp.PIPE)
    return out.stdout

@app.route("/urlscan")
def urlscan():
    if request.method == 'POST':
        url=request.form['firstname']
        print (url)
        
        if url == 'www':
            return render_template("threaturl.html")
        
        elif url == 'www.youtube.com':
            return render_template("nonthreaturl.html")

    return render_template("url.html")


app.debug =True

app.run()