import csv
'''
headers=['ID','UserName','Password','Age','Country']
rows=[(1001,"qiye","qiye_pass",24,"china"),
      (1002,"Mary","Mary_pass",20,"USA"),
      (1003,"Jack","Jack_pass",20,"USA")
      ]
with open('qiye.csv','w') as f:
    f_csv=csv.writer(f)
    f_csv.writerow(headers)
    f_csv.writerows(rows)                       
'''
'''
headers=['ID','UserName','Password','Age','Country']
rows=[{'ID':1001,'UserName':"Mary",'Password':"Mary_pass",'Age':20,'Country':"china"}]
with open('qiye2','w') as f:
    f_csv=csv.DictWriter(f,headers)
    f_csv.writeheader()
    f_csv.writerows(rows)
    '''
with open('qiye2') as f:
    csv_f=csv.reader(f)
    headers=next(csv_f)
    print(headers)
    for row in csv_f:
        print(row)
        print(row)
