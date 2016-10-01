# -*- coding: utf-8 -*-

#Enter the link to the list of discussions
#in the group and file will be created with all links in this discussions


from selenium import webdriver
import unittest, time, re, getpass

#creating the first file to write all found links
fhand = open('first.txt', 'w')
print "-".center(10, '=')



class Test6(unittest.TestCase):
    def setUp(self):
        self.base_url = raw_input("URL: ")
        self.driver = webdriver.Chrome()
        self.accept_next_alert = True

    def test_6(self):
        driver = self.driver
        driver.get(self.base_url)

        #trying to find the bottom of the page
        lastHeight = driver.execute_script("return document.body.scrollHeight")
        while True:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(1)
            newHeight = driver.execute_script("return document.body.scrollHeight")
            if newHeight == lastHeight:
                break
            lastHeight = newHeight

        #searching for discussions links    
        list_links = driver.find_elements_by_class_name('blst_title')
        count = 1
        for i in list_links:

            print count, " ", i.get_attribute('href')
            count +=1
            fhand.write(i.get_attribute('href'))
            fhand.write("\n")

if __name__ == "__main__":
    unittest.main()