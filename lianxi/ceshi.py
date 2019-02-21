import requests
import yaml

url='http://127.0.0.1:8080/api/single_interface_case/'
response=requests.get(url)
#print(response.json())

desired_caps = {
                'platformName': 'Android',
                'platformVersion': '7.0',
                'deviceName': 'A5RNW18316011440',
                'appPackage': 'com.tencent.mm',
                'appActivity': '.ui.LauncherUI',
                'automationName': 'Uiautomator2',
                'unicodeKeyboard': [True,"hh"],
                'resetKeyboard': True,
                'noReset': True,
                'chromeOptions': {'androidProcess': 'com.tencent.mm:tools'}
                }
with open('1.yaml','w',encoding='utf-8') as f:
     yaml.dump(desired_caps,f,default_flow_style=False)
     f.close()