# -*- coding: utf-8 -*-
"""
Created on Sat Sep 11 18:27:58 2021

@author: Ameer Abdullah
"""


from selenium import webdriver
import pandas as pd
from webdriver_manager.firefox import GeckoDriverManager
import time
from selenium.webdriver.support.ui import Select


course_title = []
course_organization = []
course_URL =[]
course_Certificate_type = []
course_rating = []
course_difficulty = []
course_students_enrolled = []
course_image_URL = []
course_image_name=[]


#driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()





for i in range(1,5):
    driver.get('https://www.coursera.org/search?page='+str(i)+'&index=prod_all_launched_products_term_optimization_aa_test&entityTypeDescription=Degrees')
    time.sleep(10)
    
    for j in range(1,11):
        if (i==4 and j==3):
            break
        #print((i-1)*10+j)
        
        #title
        name = driver.find_elements_by_xpath('//*[@id="main"]/div/div/div[1]/div[2]/div/div/div/div/div/ul/li[' +str(j)+']/div/div/div/div/div/div[2]/div[1]/h2')
        name = name[0]
        course = name.text
        course_title.append(course)
        
        
        #organization
        name = driver.find_elements_by_xpath('//*[@id="main"]/div/div/div[1]/div[2]/div/div/div/div/div/ul/li['+str(j)+']/div/div/div/div/div/div[2]/div[2]/span')
        name = name[0]
        course = name.text
        course_organization.append(course)

        
print(course_title)
print(course_organization)
#print(course_rating)
#print(course_difficulty)
#print(course_students_enrolled)


coursera_df = pd.DataFrame({'course_title': course_title,
                    # 'course_URL':course_URL,
                   'course_organization': course_organization,
                   # 'course_Certificate_type': course_Certificate_type,
                   # 'course_rating':course_rating,
                   #  'course_difficulty':course_difficulty,
                   #  'course_students_enrolled':course_students_enrolled,
                     # 'course_icon':course_image_URL,
                   # 'image_name':course_image_name
                    })

# #writing into a .csv file
coursera_df.to_csv('Degrees.csv')
