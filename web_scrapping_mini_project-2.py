import requests
from bs4 import BeautifulSoup
from selenium import webdriver

def download_image(particular_image_url):
    #this function takes the specific image url and downloads the image locally as 001.jpg
    resource = requests.get(particular_image_url)
    
    #saving the image locally
    output_file = open("001.jpg","wb")
    output_file.write(resource.content)
    output_file.close()

def image_address_extract(url_image):
    #this function extracts the address of 1st image from the webpage
    response = requests.get(url_image)
    
    #parsing the response as html
    page_soup = BeautifulSoup(response.content,'html.parser')
    
    #searching for the first img tag
    addresses=page_soup.find('img')
    
    #extracting the address of the image from the src attribute of the img tag
    #after extraction it is passed on to the next function to download
    download_image(addresses['src'])

def search_for_keyword(input_key):
    
    local_executable_path="C:/Users/DAcharyya/Desktop/Vacation/To-Do/Web-Crawling/chromedriver.exe"
    browser=webdriver.Chrome(executable_path=local_executable_path)
    
    #first step is to navigate to google images
    url1="https://images.google.com/"
    browser.get(url1)
    
    #searching the keyword via google images
    #entering the keyword into the search field
    search=browser.find_element_by_css_selector("#sbtc > div > div.a4bIc > input")
    search.send_keys(keyword)
    #clicking the search button
    search_button=browser.find_element_by_css_selector("#sbtc > button")
    search_button.click()
    #retrieving the url for further processing
    img_url=browser.current_url
    #exiting the browser
    browser.quit()
    #passing on the url of the resultant google image webpage to the next function
    image_address_extract(img_url)

def main():
    #Input
    keyword=str(input("Enter the keyword :"))
    
    search_for_keyword(keyword)

if if __name__ == "__main__":
    main()