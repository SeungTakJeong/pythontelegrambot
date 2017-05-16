import os
import sendmessage
from datetime import datetime
from apscheduler.schedulers.blocking import BlockingScheduler



def scraping():
    print(datetime.strftime(datetime.now(), "suspect_%Y-%m-%d_%H:%M:%S"))
    sendMessage = sendmessage.SendMessage()
    suzy =[{'location':'통진읍','description':'김포 - 집'},{'location':'영등포구','description':'여의도 - 회사'}]
    suzyToken = '304118278:AAH3uUnl_FC2tJj434zuYtBXfaGmMsuv1Rc'
    suzyChatId = '332946608'
    tak = [{'location':'강동구','description':'암사동 - 집'},{'location':'신촌로','description':'합정역 - 회사'}]
    takToken = '330472065:AAEfrxS78hh_fLsEWdiUQgfapjbwsRfU6sA'
    takChatId = '62443661'
    sendMessage.getPMInfo(suzy,suzyToken,suzyChatId)
    sendMessage.getPMInfo(tak,takToken,takChatId)


if __name__ == '__main__':
    scheduler = BlockingScheduler()

    # job을 등록
    scheduler.add_job(scraping,'cron',hour ='07,11,15,17',timezone='Asia/Seoul')  # 7,11,15,17시마다 실행
    try:
        scheduler.start()
    except(KeyboardInterrupt, SystemExit):
        print("End")
        pass

