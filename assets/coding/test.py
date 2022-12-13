import requests 
from bs4 import BeaitfulSoup

print ("enter")
ip_add = input()
api_key = d0f2258cb348dd4d47b59f40e191e8003dbba66f15c1778eec0ec9462aa7558d
r = requests.get("https://www.virustotal.com/api/v3/ip_addresses/%s" % ip_add, headers={'user-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:62.0) Gecko/20100101 Firefox/61.0','x-apikey' : '%s' % api_key}).json()
dict_web = r["data"]["attributes"]["last_analysis_result"]
tot_engine_c = 0
tot_detect_c = 0
result_eng =[]
eng_name = []
count_harmless = 0
for i in dict_web:
    tot_engine_c = 1 + tot_engine_c
    if dict_wen[i]["category"] == "malicious" or dict_web[i]["category"] == "suspicious":
        result_eng.append(dict_web[i]["result"])
        eng_name.append(dict_wen[i]["engine_name"])
        tot_detect_c = 1 + tot_detect_c

res = []
for i in result_eng:
    if i not in res:
        res.append(i)

result_eng = res 

if tot_detect_c > 0:

    print("this is malicious")

else:
    print("not malicious")