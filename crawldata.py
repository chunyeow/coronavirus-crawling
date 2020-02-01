#!/usr/bin/python
import requests
import json
import schedule
import time
requests.packages.urllib3.disable_warnings()

import conf
__author__ = 'Chun-Yeow Yeoh'

def get_confirmed_case():
    try:
       headers = {'charset':'utf-8','Content-Type':'application/json', 'Accept':'application/json' }
       url = conf.api_confirmedcase
       get_resp = requests.get(url, headers=headers, verify=False)
       if get_resp.status_code == 200:
          return get_resp
       else:
          return
    except requests.exceptions.ConnectionError:
       return

def get_death_case():
    try:
       headers = {'charset':'utf-8','Content-Type':'application/json', 'Accept':'application/json' }
       url = conf.api_deathscase
       get_resp = requests.get(url, headers=headers, verify=False)
       if get_resp.status_code == 200:
          return get_resp
       else:
          return
    except requests.exceptions.ConnectionError:
       return

def get_recover_case():
    try:
       headers = {'charset':'utf-8','Content-Type':'application/json', 'Accept':'application/json' }
       url = conf.api_recovercase
       get_resp = requests.get(url, headers=headers, verify=False)
       if get_resp.status_code == 200:
          return get_resp
       else:
          return
    except requests.exceptions.ConnectionError:
       return

def get_country_case():
    try:
       headers = {'charset':'utf-8','Content-Type':'application/json', 'Accept':'application/json' }
       url = conf.api_countrycase
       get_resp = requests.get(url, headers=headers, verify=False)
       if get_resp.status_code == 200:
          return get_resp
       else:
          return
    except requests.exceptions.ConnectionError:
       return

def query_scheduler():
    try:
       print("[Tracking-Apps] Crawling Scheduler")
       print("==================================")
       res = get_confirmed_case()
       data = res.json()
       print "Global Confirmed Case: %d" % data['features'][0]['attributes']['value']
       res = get_death_case()
       data = res.json()
       print "Global Deaths Case: %d" % data['features'][0]['attributes']['value']
       res = get_recover_case()
       data = res.json()
       print "Global Recover Case: %d" % data['features'][0]['attributes']['value']
       print("==================================")
       res = get_country_case()
       data = res.json()
       countrylen = len(data['features'])
       for n in range (countrylen):
          details = data['features'][n]['attributes']
          #print data['features'][n]['attributes']
          if details['Recovered'] is None and details['Deaths'] is None:
             print "Country: " + details['Country_Region'] + "\t Confirmed: %d" % details['Confirmed'] + "\t Deaths: None" + "\t Recovered: None"
          elif details['Recovered'] is None and details['Deaths'] is not None:
             print "Country: " + details['Country_Region'] + "\t Confirmed: %d" % details['Confirmed'] + "\t Deaths: %d" % details['Deaths'] + "\t Recovered: None" 
          elif details['Recovered'] is not None and details['Deaths'] is None:
             print "Country: " + details['Country_Region'] + "\t Confirmed: %d" % details['Confirmed'] + "\t Deaths: None" + "\t Recovered: %d" % details['Recovered']
          else:
             print "Country: " + details['Country_Region'] + "\t Confirmed: %d" % details['Confirmed'] + "\t Deaths: %d" % details['Deaths'] + "\t Recovered: %d" % details['Recovered']
          print("===========================================================================================")
       return
    except IndexError:
       print "[Tracking-Apps] Error"
       return

schedule.every(2).seconds.do(query_scheduler)
#schedule.every().hour.do(query_scheduler)

while True:
    schedule.run_pending()
    time.sleep(1)

