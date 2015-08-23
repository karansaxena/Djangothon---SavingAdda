import requests
from bs4 import BeautifulSoup
import os
import webbrowser

def scrape_amazon(url, no_products):
    r = requests.get(url)

    soup = BeautifulSoup(r.content, "html.parser")

    data = soup.find_all("li", {"id":"result_0"})
    ans = data[0].find_all("a",{"class":"a-link-normal"})[0]
    answer= ans.get("href")
    
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
    link_final = link[:no_products] #

    #temp=str(link_final[0])
    listing=answer.split('/')
    listing[4]="product-reviews"
    #temp.replace("/p/", "product-reviews",1)
    #print listing
    temp="/".join(listing)
    urll=temp+"/&type=all"

    #print urll

    #webbrowser.open(urll,new=1,autoraise=True)
    return scrape_review(urll)

    



def scrape_review(url):
    r = requests.get(url)
    revs = []
    soup = BeautifulSoup(r.content, "html.parser")

    data = soup.find_all("table", {"id":"productReviews"})

    for item in data:
        name = item.find_all("div",{"class":"reviewText"})
    for item in name:
        #print item
        revs.append(item)
    return revs

    

    #print data

    


#if __name__ == '__main__':
#print "Starting Product population script..."
 
#print '\n\n----------------------Flipkart Scraping Script------------------------\n\n'

#print '\nMens Watches\n'

#scrape_flipkart('http://www.amazon.in/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=moto+g3', 1)
