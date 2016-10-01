# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest, time, re, getpass

fhand = open('first.txt', 'r')
fhand2 = open('second.txt', 'w')


class Test7(unittest.TestCase):
    def setUp(self):

        self.driver = webdriver.Chrome()
        #self.base_url = raw_input("URL: ")
        self.accept_next_alert = True

    def test_7(self):
        driver = self.driver
        for line in fhand:
            driver.get(line)

            lastHeight = driver.execute_script("return document.body.scrollHeight")

            #in every discussion searching for links
            list_links = driver.find_elements_by_class_name('bp_text')
            count = 1
            for i in list_links:

                link = driver.find_elements_by_class_name('mem_link')
                for l in link:

                    print count, " ", l.get_attribute('href')
                    count +=1


                    fhand2.write(l.get_attribute('href'))
                    fhand2.write("\n")





if __name__ == "__main__":
    unittest.main()