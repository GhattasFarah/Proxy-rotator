import requests
import time

#URL to check the Ip and list of proxies
#url = 'https://ip.oxylabs.io/ip'
url = 'http://ident.me/'
proxies = ['http://27.79.63.200:50003', 'http://27.107.27.13:80', 'http://64.225.8.115:9996']

#The get function to send request, get response, and print status code and Ip returned. This has a timeout function of 60 seconds.
def get_req(url, proxy, session):
	#Try-catch to catch any exceptions thrown
	try:
		resp = session.get(url,proxies={'http':proxy}, timeout=60)
		print(resp.status_code, resp.text)
		
	#Catches exception and prints the type of exception thrown.
	except Exception as e:
		print("Exception: ", type(e))
		
#acts as the main function of the program.
def run():
	#creates a session and passes it through with the request
	with requests.Session() as session:
		for p in proxies:
			get_req(url, p, session)
			time.sleep(2) #2 sec delay between requests

run()