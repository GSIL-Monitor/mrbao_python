# coding:utf-8
import csv
header=['job_title','company_text','job_xinzhi','new_url']
row=[('测试工程师', '软通动力', '5K-7K', 'https://www.zhipin.com/job_detail/1417088295.html?ka=search_list_1'), ('测试工程师', '博彦科技', '10K-15K', 'https://www.zhipin.com/job_detail/1417084578.html?ka=search_list_2'), ('软件测试工程师', '维宏股份', '5K-7K', 'https://www.zhipin.com/job_detail/1417088525.html?ka=search_list_3'), ('蚂蚁金服 - 监控测试工程师（资深）', '蚂蚁金服', '15K-30K', 'https://www.zhipin.com/job_detail/1417074270.html?ka=search_list_4'), ('测试工程师', '迪英加科技', '10K-20K', 'https://www.zhipin.com/job_detail/1417086382.html?ka=search_list_5'), ('初，中级测试工程师（大柏树1.5W,1-3年经验）', '北风网', '10K-20K', 'https://www.zhipin.com/job_detail/1417079368.html?ka=search_list_6'), ('测试工程师', '小站教育', '12K-24K', 'https://www.zhipin.com/job_detail/1417053211.html?ka=search_list_7'), ('QA测试工程师', '微盟', '8K-10K', 'https://www.zhipin.com/job_detail/1417062195.html?ka=search_list_8'), ('实习测试工程师', '美团点评', '4K-6K', 'https://www.zhipin.com/job_detail/1417029179.html?ka=search_list_9'), ('资深测试工程师', '美团点评', '2K-3K', 'https://www.zhipin.com/job_detail/1417051904.html?ka=search_list_10'),]
with open('123.csv','w') as f:
    f_csv=csv.writer(f)
    f_csv.writerow(header)
    f_csv.writerows(row)