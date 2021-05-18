# import requests
import urllib.request,urllib.parse,urllib.error
from bs4 import BeautifulSoup
import ssl
class Query():
    def __init__(self):
        pass
    def display(self,names, prices, ratings,images):
        flag = 1
        n =[]
        p = []
        r = []
        im = []
        for name,price,rating, image in zip(names,prices,ratings,images):
            
            n.append(name.text)
            p.append(price.text)
            r.append(rating.text)
            im.append(image.get('src'))
            
            flag=0
        return n,p,r,im
        if flag:
            print("No results found")

    def scratch(self,item):
        url = "https://www.amazon.in/s?k=redmi+note+5&ref=nb_sb_noss_2"
    
        #ignore ssl certificates error
        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE

        # item = input("\n\nEnter name of product:").strip()
        # print("\n\n")

        # Amazon.............


        item = "+".join(item.split(" "))
        # url = "https://www.amazon.in/s?k="+item+"&ref=nb_sb_noss_2"


        # opener = urllib.request.Request(url)
        # opener.add_header('User-agent', 'Mozilla/5.0')
        # fhand = urllib.request.urlopen(opener,context = ctx).read()


        # soup = BeautifulSoup(fhand,'html.parser') 
        # names = soup.find_all(class_="a-size-medium a-color-base a-text-normal")
        # prices = soup.find_all(class_="a-price-whole")
        # ratings = soup.find_all(class_="a-icon a-icon-star-small a-star-small-4 aok-align-bottom")
        


        #FLipkart.................


        url = "https://www.flipkart.com/search?q="+item+"&&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"


        opener = urllib.request.Request(url)
        opener.add_header('User-agent', 'Mozilla/5.0')
        fhand = urllib.request.urlopen(opener,context = ctx).read()


        soup = BeautifulSoup(fhand,'html.parser') 
        self.names = soup.find_all(class_="_4rR01T")
        self.prices = soup.find_all(class_="_30jeq3 _1_WHN1")
        self.ratings = soup.find_all(class_="_3LWZlK")
        self.images = soup.find_all(class_="_396cs4 _3exPp9")

        # print(names)
        # self.display(names,prices,ratings)