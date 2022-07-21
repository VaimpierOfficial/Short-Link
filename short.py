import requests ,os ,sys #line:1:import requests,os,sys
try :#line:2:try:
	url =sys .argv #line:3:url = sys.argv
	url =str (sys .argv [1 ])#line:4:url = str(sys.argv[1])
	if requests .get (url ).status_code ==200 :#line:5:if requests.get(url).status_code==200:
		pass #line:6:pass
	else :#line:7:else:
		print ("\033[1;32mBad Requests")#line:8:print("\033[1;32mBad Requests")
		sys .exit ()#line:9:sys.exit()
	api =f"https://3c5.com/api/?key=FCaz1uUwPuU6&url={url}"#line:10:api = f"https://3c5.com/api/?key=FCaz1uUwPuU6&url={url}"
	a =requests .get (api )#line:11:a=requests.get(api)
	if a .status_code ==200 :#line:12:if a.status_code==200:
		vaim =a .text #line:13:vaim=a.text
		vaim =vaim [20 :len (vaim )-2 ]#line:14:vaim=vaim[20:len(vaim)-2]
		vaim =vaim .replace ("\/","/")#line:15:vaim=vaim.replace("\/","/")
		print ("Your Link is : "+vaim )#line:16:print("Your Link is : "+vaim)
	else :#line:17:else:
		print ("\033[1;32mBad Requests")#line:18:print("\033[1;32mBad Requests")
except :#line:19:except:
	print ("\033[1;32mBad Requests")#line:20:print("\033[1;32mBad Requests")
