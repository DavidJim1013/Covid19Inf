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
    globalStats=json_data['data']['globalStatis']
    #累计确诊
    diagnosed=str(domesticStats['diagnosed'])
    #累计治愈
    cured=str(domesticStats['cured'])
    #现有疑似
    suspect=str(domesticStats['suspect'])
    #累计死亡
    death=str(domesticStats['death'])
    #现有确诊
    currentConfirmedCount=str(domesticStats['currentConfirmedCount'])
    #无症状感染者
    noInfectCount=str(domesticStats['noInfectCount'])
    #境外输入
    importedCount=str(domesticStats['importedCount'])
    #现有重症
    seriousCount=str(domesticStats['seriousCount'])
    #更新时间
    times=str(domesticStats['times'])
    #全球现有确诊
    nowConfirm=str(globalStats['nowConfirm'])
    #全球累计确诊
    confirm=str(globalStats['confirm'])
    #全球累计治愈
    heal=str(globalStats['heal'])
    #全球累计死亡
    dead=str(globalStats['dead'])

    domesticStats_data={
        "diagnosed":diagnosed,
        "cured":cured,
        "suspect":suspect,
        "death":death,
        "currentConfirmedCount":currentConfirmedCount,
        "noInfectCount":noInfectCount,
        "importedCount":importedCount,
        "seriousCount":seriousCount,
        "globalnowconfirm":nowConfirm,
        "globalconfirm":confirm,
        "globalheal":heal,
        "dead":dead,
        "times":times
    }
    jsondata = json.dumps(domesticStats_data)

    domesticStats=[diagnosed,cured,suspect,death,currentConfirmedCount,noInfectCount,importedCount,seriousCount,times]
    return jsondata

urls = (
    '/', 'index'
)

class index:
    def GET(self):
        web.header("Access-Control-Allow-Origin", "*") 
        domesticStats_data=get_cov_data_info()
        return domesticStats_data


if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
