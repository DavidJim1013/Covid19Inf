import requests
import json
import re
import web

headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'
}

def get_cov_data_info():
    url=r'http://sa.sogou.com/new-weball/page/sgs/epidemic'
    rep=requests.get(url,headers=headers).content.decode('utf-8')
    json_data_str=re.findall('window.__INITIAL_STATE__ = (.*?)</script>',rep)[0]
    json_data=json.loads(json_data_str)
    domesticStats=json_data['data']['domesticStats']
    #累计确诊
    diagnosed=domesticStats['diagnosed']
    #累计治愈
    cured=domesticStats['cured']
    #现有疑似
    suspect=domesticStats['suspect']
    #累计死亡
    death=domesticStats['death']
    #现有确诊
    currentConfirmedCount=domesticStats['currentConfirmedCount']
    #无症状感染者
    noInfectCount=domesticStats['noInfectCount']
    #境外输入
    importedCount=domesticStats['importedCount']
    #现有重症
    seriousCount=domesticStats['seriousCount']

    domesticStats_data={
        "diagnosed":diagnosed,
        "cured":cured,
        "suspect":suspect,
        "death":death,
        "currentConfirmedCount":currentConfirmedCount,
        "noInfectCount":noInfectCount,
        "importedCount":importedCount,
        "seriousCount":seriousCount
    }

    domesticStats=[diagnosed,cured,suspect,death,currentConfirmedCount,noInfectCount,importedCount,seriousCount]
    return domesticStats_data

urls = (
    '/', 'index'
)

class index:
    def GET(self):
        domesticStats_data=get_cov_data_info()
        return domesticStats_data


if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
