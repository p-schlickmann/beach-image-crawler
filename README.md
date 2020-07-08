# image-extractor
Web Robot (Crawler) that I used for a private project. This bot searches for the beach name on https://snazzymaps.com/style/124771/google-maps-clean# and saves the satelite view image on your computer  

# How to use it
0. Download [Lightshot](https://app.prntscr.com/en/index.html) and set the print key to 'f10'
1. You need python installed on your computer  
2. Clone this repository into your machine  
3. Install the required libraries specified in the requirements.txt file
4. Open your **terminal** (MacOS, Linux) or **cmd** (Windows), navigate to the project folder and run:  
if you are using pipenv: `pipenv run python app.py` 
if not: `python app.py`
5. You will need a .db file specifying at least city and beach for each Beach 

6. You need to call the class Printer with the city name you want   
### It's very easy to use, after you started app.py wait for the scraper to get the first result, if it's accurate, press f10, you can save it with the beach name using 'CTRL-V', if it's not accurate, skip the result with f9, if you want to pause it, press f8, to unpause press f8 again.
