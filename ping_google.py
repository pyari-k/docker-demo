import requests
def ping_google():
	response = requests.get('https://google.com/')
	print("\n pinged google and the response = {}".format(response))

