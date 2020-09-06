from selenium import webdriver
import os
import time

def main():
    driver = webdriver.Chrome(os.getcwd() + "//chromedriver")

    driver.get("https://petition.president.gov.ua/petition/100754")

    driver.find_element_by_xpath('//*[@id="pet-tab"]/ul/li[3]/a').click()

    theEnd = int(driver.find_element_by_xpath('//*[@id="pet-tab-3"]/div/div[3]/div/ul/li[7]/a').text) + 2

    i = 0
    f = open('peoples', 'a')
    while i < theEnd:
        time.sleep(1)
        peoples = driver.find_elements_by_class_name("table_row")
        
        for name in peoples:
            f.write(name.text + '\n')
        
        allBtn = driver.find_elements_by_class_name('pag_link')
        allBtn[len(allBtn) - 1].click()
        i += 1
    f.close()   
    

if __name__ == "__main__":
    main()