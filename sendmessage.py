import requests
import json
import logging
from bs4 import BeautifulSoup

logging.basicConfig(level=logging.DEBUG)

class SendMessage:

    def __init__(self):
        self.telegramApi = 'https://api.telegram.org/bot330472065:AAEfrxS78hh_fLsEWdiUQgfapjbwsRfU6sA/sendMessage'
        self.telegramChatId= '62443661'

    def sendMessage(self,msg,token,chatid):
        telegramUrl = 'https://api.telegram.org/bot'+token+'/sendMessage'
        params = {'chat_id':chatid,'text':msg}
        result = requests.get(telegramUrl,params=params)
        resultCode = result.status_code
        resultJson = result.json()
        logging.debug(resultCode)
        if(result.raise_for_status()):
            self.telegramChatId = resultJson['result']['chat']['id']

    def getPMInfo(self,locations,token,chatid):
        for location in locations:

            result = requests.get('http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getMsrstnAcctoRltmMesureDnsty?stationName='+location['location']+'&dataTerm=month&pageNo=1&numOfRows=10&ServiceKey=9XewlhJmpN8FgPILBXQ4BliMa1WW%2FhsJ5b8dEcMtZ0Ka%2Fhz1JpBb4yfx62NuFr0fs0HNas7ZWxjeOqW8CWn2sw%3D%3D&ver=1.3&_returnType=json')

            if(result.raise_for_status()):
                logging.error('API SERVER BAD RESPONSE')
            else:
                resultJson = result.json()
                resultInfo = resultJson['list'][0]
                dataTime = resultInfo['dataTime']
                pm10Value = resultInfo['pm10Value']
                pm10Grade1h = resultInfo['pm10Grade1h']
                pm10GradeKorean = '좋음'
                if pm10Grade1h =='1':
                    pm10GradeKorean = '좋음'
                elif pm10Grade1h == '2':
                    pm10GradeKorean = '보통'
                elif pm10Grade1h == '3':
                    pm10GradeKorean = '나쁨'
                elif pm10Grade1h == '4':
                    pm10GradeKorean = '매우나쁨'
                else:
                    pm10GradeKorean = '데이터없음'
                message = '당신의 {0} 의 미세먼지는 {1} 관측소 기준 {2} 시간의 미세먼지 농도는 {3} 이며, 등급은 {4} 입니다.'.format(location['description'],location['location'],dataTime,pm10Value,pm10GradeKorean)
                self.sendMessage(message,token,chatid)

    def getPMInfoMessage(self,location):
        result = requests.get('http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getMsrstnAcctoRltmMesureDnsty?stationName='+location+'&dataTerm=month&pageNo=1&numOfRows=10&ServiceKey=9XewlhJmpN8FgPILBXQ4BliMa1WW%2FhsJ5b8dEcMtZ0Ka%2Fhz1JpBb4yfx62NuFr0fs0HNas7ZWxjeOqW8CWn2sw%3D%3D&ver=1.3&_returnType=json')

        if(result.raise_for_status()):
            logging.error('API SERVER BAD RESPONSE')
        else:
            resultJson = result.json()
            resultInfo = resultJson['list'][0]
            dataTime = resultInfo['dataTime']
            pm10Value = resultInfo['pm10Value']
            pm10Grade1h = resultInfo['pm10Grade1h']
            pm10GradeKorean = '좋음'
            if pm10Grade1h =='1':
                pm10GradeKorean = '좋음'
            elif pm10Grade1h == '2':
                pm10GradeKorean = '보통'
            elif pm10Grade1h == '3':
                pm10GradeKorean = '나쁨'
            elif pm10Grade1h == '4':
                pm10GradeKorean = '매우나쁨'
            else:
                pm10GradeKorean = '데이터없음'
            message = '{0} 관측소 기준 {1} 시간의 미세먼지 농도는 {2} 이며, 등급은 {3} 입니다.'.format(location,dataTime,pm10Value,pm10GradeKorean)
            return message