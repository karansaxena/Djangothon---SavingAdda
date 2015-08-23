import requests
from bs4 import BeautifulSoup
import os
import webbrowser
rev = []
def scrape_flipkart(url, no_products):
    r = requests.get(url)

    soup = BeautifulSoup(r.content, "html.parser")

    data = soup.find_all("div", {"class":"product-unit"})
    #print data
    product_name = []
    image_url = []
    price = []
    link = []
    for item in data:
        name = item.find_all("a",{"class":"fk-display-block"})[0]
        product_name.append(name.get("title"))
        image = item.find_all("img")[0]

        if image.get("data-src"):
            img_url = image.get("data-src")
        else:
            img_url = image.get("src")
        image_url.append(img_url)
        price1 = item.find_all("div",{"class":"pu-final"})[0]
        price.append(price1.text.strip())
        link.append(name.get("href"))

    product_name_final = product_name[:no_products]
    image_url_final = image_url[:no_products]
    price_final = price[:no_products]
    link_final = link[:no_products]

    temp=str(link_final[0])
    listing=temp.split('/')
    listing[2]="product-reviews"
    #temp.replace("/p/", "product-reviews",1)
    temp="/".join(listing)
    urll= "http://flipkart.com"+temp+"&type=all"

    #print urll

    #webbrowser.open(urll,new=1,autoraise=True)
    return scrape_review(urll)



def scrape_review(url):
    r = requests.get(url)
    
    soup = BeautifulSoup(r.content, "html.parser")

    data = soup.find_all("div", {"class":"review-list"})

    for item in data:
        name = item.find_all("span",{"class":"review-text"})
    for item in name:
        #print item
        rev.append(item)
    return rev
    

    #print data

    


#if __name__ == '__main__':
#print "Starting Product population script..."
 
#print '\n\n----------------------Flipkart Scraping Script------------------------\n\n'

#print '\nMens Watches\n'

#scrape_flipkart('http://www.flipkart.com/search?q=sandals&as=off&as-show=off&otracker=start', 1)
