import os
import sendmessage
from datetime import datetime
from apscheduler.schedulers.blocking import BlockingScheduler



def scraping():
    print(datetime.strftime(datetime.now(), "suspect_%Y-%m-%d_%H:%M:%S"))
    sendMessage = sendmessage.SendMessage()
    suzy =[{'location':'통진읍','description':'김포 - 집'},{'location':'영등포구','description':'여의도 - 회사'}]
    tak = [{'location':'강동구','description':'암사동 - 집'},{'location':'신촌로','description':'합정역 - 회사'}]
    sendMessage.getPMInfo(suzy)
    sendMessage.getPMInfo(tak)


if __name__ == '__main__':
    scheduler = BlockingScheduler()

    # job을 등록
    scheduler.add_job(scraping,'cron',hour ='07,11,15,17',timezone='Asia/Seoul')  # 60초마다 실행
    try:
        scheduler.start()
    except(KeyboardInterrupt, SystemExit):
        print("End")
        pass

