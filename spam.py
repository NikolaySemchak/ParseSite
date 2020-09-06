from selenium import webdriver
import os

def main():
    driver = webdriver.Chrome(os.getcwd() + "//chromedriver")

    driver.get("https://petition.president.gov.ua/petition/100754")

    driver.find_element_by_xpath('//*[@id="pet-tab"]/ul/li[3]/a').click()

    theEnd = int(driver.find_element_by_xpath('//*[@id="pet-tab-3"]/div/div[3]/div/ul/li[7]/a').text) + 2
    print (theEnd)
    # while True:
    #     peoples = driver.find_elements_by_class_name("table_row")
    
    #     f = open('peoples', 'w')
        
    #     for name in peoples:
    #         f.write(name.text + '\n')
        
    #     pagLinks = driver.find_elements_by_class_name('pag_link')
    #     for i in pagLinks:
    #         if i.get_attribute('class') == 'pag_link active':
                
    

if __name__ == "__main__":
    main()