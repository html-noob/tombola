import requests

def main():

	headers = {
		'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'
	}

	with requests.session() as s:
		url = "https://www.patreon.com/login"
		cookies = requests.get(url).cookies

		r = s.get(url, cookies = cookies, headers=headers)
		#print(r.content)
		f = open("result.html", "w")
		f.write(str(r.content))
		f.close()
    
    #testa: https://www.tutorialspoint.com/python_web_scraping/python_web_scraping_processing_captcha.htm
main()