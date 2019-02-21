# coding:utf-8
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
from urllib.parse import urljoin
import re
import csv

url='https://so.csdn.net/so/search/s.do?p=2&q=http'
response=requests.get(url)

print(response.text)