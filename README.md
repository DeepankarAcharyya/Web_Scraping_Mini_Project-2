# Web_Scraping_Mini_Project-2
*The program takes a keyword as an input and downloads an image after googling for that keyword.*

## Libraries Used:
- requests
- BeautifulSoup
- Selenium Webdriver

### Gist/Concept/Working of the program:
- The program first takes input of the keyword from the user.
- Then the program googles for the keyword via google images (using the selenium module).
- The program then retrieves the web address of the resultant google image page and passes it to another function.
- The next function extracts the web address of the first image tag and passes on the address to the third function (using BeautifulSoup Module).
- The third function is programmed to download the image from the provided web address (the requests module is used here).



