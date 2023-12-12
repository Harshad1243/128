from bs4 import BeautifulSoup
import time
import pandas as pd
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By

START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"

# Webdriver
browser = webdriver.Chrome("D:/Setup/chromedriver_win32/chromedriver.exe")
browser.get(START_URL)

scarped_data = []

def scrape():    
    for ul_tag in soup.find_all("ul",attrs={"class","brown dwarfs"}):
        li_tags = ul_tag.find_all("li")
        temp_list = []
        for index, li_tag in enumerate(li_tags):
            if index ==0:
                temp_list.append(li_tag.find_all("a")[0].contents[0])
            else:
                try:
                    temp_list.append(li_tag.contents[0])
                except:
                    temp_list.apend('')

        hyperlink_li_tag = li_tags[0]

        temp_list.append("https://en.wikipedia.org/"+hyperlink_li_tag.find_all("a",href=True)[0]['href'])
        scarped_data.append(temp_list)

    browser.find_element(By.XPATH, value='//*[@did="primary_cloumn"]/footer/div/div/div/nav/span[2]/a').click()

    print(f"Page{i} scraping completed")

    scrape()
    headers = ['Star_name','Distance','Mass','Radius','Luminosity']
    star_df_1_df_1 = pd.DataFrame(scarped_data,columns=headers)
    star_df_1_df_1.to_csv('updated_scraped_csv',index=True,index_label="id")

    def scrape_more_data(hyperlink):     
        try:
            page = requests.get(hyperlink)
            soup = BeautifulSoup(page.content,"html.parser")
            temp_list = []
            for tr_tag in soup.find_all("tr",attrs={"class":"fact_row"}):
                td_tags = tr_tag.find_all("td")
                for td_tag in td_tags:
                    try:
                        temp_list.append(td_tag.find_all("div",attrs={"class":"value"})[0].contents[0])
                    except:
                        temp_list.append("")
            new_star_data.append(temp_list)
        except:
            time.sleep(1)
            scrape_more_data(hyperlink)
    planet_df_1 = pd.read_csv("updated_scraped_data.csv")
    for index,row in planet_df_1.iterrows():
        print(row['hyperlink'])
        scrape_more_data(row['hyperlink'])
        print(f"Data Scraping at hyperlink{index+1} completed")
    print(new_star_data[0.10])

    scrapped_data = []
    for row in new_star_data:
        replaced = []
        for el in row:
            el = el.replace("\n","")
            replaced.append(el)
        scrapped_data.append(replaced)
    print(scrapped_data)

    
    soup = BeautifulSoup(browser.page_source, "html.parser")


    #VERY IMP: The class "wikitable" and < tr> data is at the time of creation of this code. 
    # This may be updated in future as the page is maintained by Wikipedia. 
    # Understand the page structure as discussed in the class & perform Web Scraping from scratch.

    bright_star_table = soup.find("table",attrs={"class","wikitable"})

    table_body = bright_star_table.find("tbody")

    table_rows = table_body.find_all("tr")

    for row in table_rows:
        table_cols = row.find_all("td")
        print(table_cols)

        temp_list = []
    
    for col_data in table_cols:
        print(col_data.text)

        data = col_data.text.strip()
        print(data)

        temp_list.append(data)

    scarped_data.append(temp_list)

    stars_data = []

    for i in range(0,len(scarped_data)):
        
        Star_names = scarped_data[i][1]
        Distance = scarped_data[i][3]
        Mass = scarped_data[i][5]
        Radius = scarped_data[i][6]
        Lum = scarped_data[i][7]

        required_data = [Star_names,Distance,Mass,Radius,Lum]
        stars_data.append(required_data)

        headers = ['Star_name','Distance','Mass','Radius','Luminosity']

        star_df_1 = pd.DataFrame(stars_data,columns=headers)

        star_df_1.to_csv("scraped_data.csv",index=True,index_label="id")


    



