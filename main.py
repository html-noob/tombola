import mechanicalsoup

def main():
    print("hello world")
    browser = mechanicalsoup.StatefulBrowser()
    print(browser.open("https://www.patreon.com/login"))
    print(browser.url)
main()