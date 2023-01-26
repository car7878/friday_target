import requests
import json
import time
import requests
import base64
import datetime
pids = [7978334,8002380,8004948,7968158,8004958,7822745,7765297,7716167,7991913,7957797,7765295]
y = 0
disc = 0.0
url = 'https://aiapi.shopping.friday.tw/api/getqpage/'
headers2 = {'Accept': 'application/json','Accept-Encoding': 'gzip, deflate, br','Accept-Language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7,ko;q=0.6,zh-CN;q=0.5','Connection': 'keep-alive','Content-Length': '162','Content-Type': 'application/json','Host': 'aiapi.shopping.friday.tw','Origin': 'https://turn.shopping.friday.tw','Referer': 'https://turn.shopping.friday.tw/','sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','Sec-Fetch-Dest': 'empty','Sec-Fetch-Mode': 'cors','Sec-Fetch-Site': 'same-site','User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36','X-Requested-With': 'GA1.1.1453623390.1674006097'}
def lineNotifyMessage(token, msg):

    headers = {
        "Authorization": "Bearer " + token, 
        "Content-Type" : "application/x-www-form-urlencoded"
    }

    payload = {'message': msg }
    r = requests.post("https://notify-api.line.me/api/notify", headers = headers, params = payload)
    return r.status_code



if __name__ == "__main__":
    token = 'LLnWdt86iCuDfJBiEnlj7eKkD9VGYraAgfCF1S1WBOn'
    token2 = 'Ok5G5Lfy6wMWGCF5Ac64dYSh0ZqEoIrIpOIp7tibeIW'

    job_name = input("Job_name:")
    disc = input("請輸入折數:")
    target_value = input("target_value_input:")

    print(disc)
    x =1
    print(time.ctime(time.time()) + "\t")

    while True:
        try:
            target_value_request_url = "https://raw.githubusercontent.com/car7878/friday_target/main/target_value_" + target_value
            print(target_value_request_url)
            resp = requests.get(target_value_request_url)
            payload2 = {"target":"pseudoid","list_fun":"Q3sTT","list_args":"content","list_remote":"lots_m","list_cmpn":"friday00","list_click":0,"target_value":resp.text.replace("\n","")}
            print(payload2)
            r = requests.post(url,headers=headers2,data = json.dumps(payload2),timeout=5)
#            print(r.status_code)
            j= json.loads(r.text)
    #        print(j[0]['pids'])
    #        print(j[0]['flag_hs'])
    #        print("時間:" + datetime.datetime.fromtimestamp(json.loads(base64.b64decode(j[0]['flag_hs'].split(".")[1]+"===="))["exp"]).isoformat())
#            print(x)
            x=x+1
            if x % 10 == 0 :
                print(x)
                print(time.ctime(time.time()))
            if x % 100 == 0 :
                print(x)
                print("休息4分鐘")
                time.sleep(240)
                print(time.ctime(time.time()))
            for i in j[0]['pids']:
#                print(i['name'] +"\t" + "價格:" +str( i['price']) +"\t" + "折扣:" +str( i['discount']) +"\t" + "打幾折:" +str(i['discount'] / i['price']*10) +"\t" + "url:" + i['url'])
                    if i['discount'] / i['price'] > float(disc):
                        print(i['name'] +"\t" + "價格:" +str( i['price']) +"\t" + "折扣:" +str( i['discount']) +"\t" + "打幾折:" +str(i['discount'] / i['price']*10) +"\t" + "url:" + i['url'])
                        print(j[0]['flag_hs'])
                        print("Job_name:" + job_name +"時間:" + datetime.datetime.fromtimestamp(json.loads(base64.b64decode(j[0]['flag_hs'].split(".")[1]+"===="))["exp"]).isoformat())
                        message = "Job_name:" + job_name + "  HS:" + j[0]['flag_hs'] + "\t" + "時間:" + datetime.datetime.fromtimestamp(json.loads(base64.b64decode(j[0]['flag_hs'].split(".")[1]+"===="))["exp"]).isoformat() + "\t" +i['name'] +"\t" + "價格:" +str( i['price']) +"\t" + "折扣:" +str( i['discount']) +"\t" + "打幾折:" +str(i['discount'] / i['price']*10) +"\t" + "url:" + i['url']
                        lineNotifyMessage(token, message)
                        with open('friday.log', 'a', encoding='utf-8') as log_file:
                            log_file.write(j[0]['flag_hs']+"\n")
                            log_file.write("時間:" + datetime.datetime.fromtimestamp(json.loads(base64.b64decode(j[0]['flag_hs'].split(".")[1]+"===="))["exp"]).isoformat()+"\n")
                            log_file.write(i['name'] +"\t" + "價格:" +str( i['price']) +"\t" + "折扣:" +str( i['discount']) +"\t" + "打幾折:" +str(i['discount'] / i['price']*10) +"\t" + "url:" + i['url']+ "\n")
                        for z in pids:
                            if i['pid'] == z :
                                y = 1
                        if y != 1:
                            lineNotifyMessage(token2, message)
                            y = 0
            time.sleep(0.5)
        except:
            print("Error 休息10秒鐘")
            time.sleep(10)
            
