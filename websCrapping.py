
# coding: utf-8

# In[1]:

from bs4 import BeautifulSoup
from collections import defaultdict
import csv
from datetime import datetime
import os
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import time
import schedule
import sched
from selenium.webdriver.common.keys import Keys
import webbrowser
from selenium.webdriver.firefox.webdriver import FirefoxProfile


Capital = 4900

# In[2]:

save_folder = 'FirstMetroReciepts'


# In[3]:

if not os.path.isdir(save_folder):
    os.mkdir(save_folder)


# In[4]:

def login(username,password):
    inputs = WebDriverWait(driver,10).until(lambda driver:
            driver.find_elements_by_class_name('divLoginInputText'))
    inputs[0].send_keys(username)
    inputs[1].send_keys(password)
    driver.find_element_by_id('LoginButton').click()
    try:
        driver.switch_to_frame('main')
    except:
        pass
    WebDriverWait(driver,20).until(lambda driver:
        driver.find_element_by_link_text('QUOTES')).click()



# In[5]:

def set_code(code):
    try:
        driver.switch_to_frame('main')
    except:
        pass
    '''
    try:
        driver.find_element_by_link_text('QUOTES').click()
    except:
        pass
    '''
    inbox = WebDriverWait(driver,10).until(lambda driver : 
            driver.find_element_by_id('secCode'))
    inbox.clear()
    inbox.send_keys(code)
    driver.find_element_by_id('btnGoSI').click()
    
# In[6]:

def get_keys():
    keys = driver.find_element_by_tag_name('tr')
    return [a.text for a in keys.find_elements_by_tag_name('th')[:-1]]


# In[7]:

def generate_levels_dicts():
    header = get_keys()
    for row in driver.find_elements_by_class_name('siBnAPart'):
        cells = [x.text for x in row.find_elements_by_tag_name('td')]
        yield dict(zip(header,cells))


# In[8]:

def get_top_bid(code):
    set_code(code)
    bid_price_css = '#bidprice1'
    time.sleep(1)
    bid = driver.find_element_by_css_selector(bid_price_css)
    return bid.text.replace(',','')

# In[9]:

def buy_stock(order):
    print('Buying No.{}'.format(order['No']))
    driver.find_element_by_id('lnkSIDbuy').click()
    try:
        volume = WebDriverWait(driver,10).until(lambda driver :
            driver.find_element_by_name('volume'))
    except:
        return False



# In[10]:


# In[11]:

def go_to_bidpage():
    driver.get(base_url)
    time.sleep(1)
    try:
        driver.switch_to_frame('main')
    except:
        pass
    nxt = driver.find_elements_by_link_text('QUOTES')
    if nxt:
        nxt[0].click()
        try:
            nxt[0].click()
        except:
            pass


# In[12]:

def update_csv(csv_file):
    with open(csv_file,'wb') as outfile:
        writer = csv.writer(outfile,delimiter=',')
        writer.writerow(header)
        for order in orders:
            outrow = [order[h] for h in header]
            writer.writerow(outrow)


# In[13]:
'''
with open('fm_username_password.txt','rb') as infile:
    username,password = infile.readline().split(',')
'''

username = 'usr_name'

password = 'pawwsd'

# Add the path to your Firefox profile here. 
# Note: make sure to use forward slashes, as Microsoft defaults to the backslash.
#keprofile = FirefoxProfile('C:/Users/Jerome/AppData/Roaming/Mozilla/Firefox/Profiles/vd6mkrcs.Default User')
#driver = webdriver.Firefox(profile)


# In[14]:

driver = webdriver.Firefox()


# In[15]:

base_url = 'base_url'


# In[16]:

driver.get(base_url)


# In[17]:

login(username,password)


# In[18]:

time.sleep(1)
go_to_bidpage()


# In[19]:

orders = list()


# In[20]:

csv_file = 'OrderORG.csv'


# In[21]:

with open(csv_file,'rb') as infile:
    reader = csv.reader(infile,delimiter=',')
    header = reader.next()
    for row in reader:
        orders.append(dict(zip(header,row)))

# In[22]:

start = time.time()

# In[23]:

  
# In[ ]:

while(1):
#for i in range(1):
    now = time.time()
    # get runtime in seconds
    runtime = now - start
    # If program runs for 3 hours, quit. 10800 seconds in 3 hours, so...
    if runtime > 10800:
        break

    for order in orders:
        order['Current Market Price'] = get_top_bid(order['StockCode'])
        print("{}:{}".format(
        order['StockCode'],order['Current Market Price']))
        update_csv(csv_file)    
        if order['Buy Price'] and not order['Portfolio - Sell Quantity']:
            if float(order['Current Market Price']) > float(order['Buy Price']):
                if buy_stock(order):
                    print("[+] Successfully Purchased No.{}:{}".format(
                            order['No'],order['StockCode']))
                else:
                    print("[-] error buying No.{}:{}".format(
                            order['No'],order['StockCode']))
                #time.sleep(1)
                go_to_bidpage()



  

        
# In[ 37]:

driver.close()


# In[ 37]:



