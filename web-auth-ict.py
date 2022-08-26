#!/usr/bin/env python
# -*-coding:utf-8-*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os

os.environ["PATH"] += os.pathsep + os.path.dirname(os.path.realpath(__file__))
driver = webdriver.PhantomJS("./phantomjs-2.1.1-linux-x86_64/bin/phantomjs")
driver.get('https://gw.ict.ac.cn/srun_portal_pc?ac_id=1&theme=pro')
name = driver.find_element_by_id("username")
name.send_keys('blockchain_test_1')
password = driver.find_element_by_id('password')
password.send_keys('ictblockchain706')
password.send_keys(Keys.RETURN)
login =  driver.find_element_by_id( "login-account")
login.click()
time.sleep(1)
driver.quit()