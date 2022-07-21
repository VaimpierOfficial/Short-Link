import requests,os,sys
try:
	url = sys.argv
	url = str(sys.argv[1])
	if requests.get(url).status_code==200:
		pass
	else:
		print("\033[1;32mBad Requests")
		sys.exit()
	api = f"https://3c5.com/api/?key=FCaz1uUwPuU6&url={url}"
	a=requests.get(api)
	if a.status_code==200:
		vaim=a.text
		vaim=vaim[20:len(vaim)-2]
		vaim=vaim.replace("\/","/")
		print("Your Link is : "+vaim)
	else:
		print("\033[1;32mBad Requests")
except:
	print("\033[1;32mBad Requests")
