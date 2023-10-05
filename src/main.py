from . import zenhan
from . import hizukeni
from . import youbiDel
from . import registerCalendar

id = ""

def yoteiAuto(schedule):
    scheduleList = []
    yoteimList = []
    yoteidList = []
    naiyouList = []
    i = 0
    # 予定の追加
    scheduleList = schedule.splitlines()

    try:
        while i<len(scheduleList):
            yotei = scheduleList[i]
            yotei_han = zenhan.zenhan(yotei)
            if yotei != "":
                hizukem, hizuked, naiyou = hizukeni.hizukeni(yotei_han)
                if naiyou != "":
                    naiyou = youbiDel.youbiDel(naiyou)
                    yoteimList.append(hizukem)
                    yoteidList.append(hizuked)
                    naiyouList.append(naiyou)
         
                    print(hizukem)
                    print(hizuked)
                    print(naiyou)
            i+=1
    except:
        return("予定の取得中にエラーが発生しました。")

    #すべての量が同じことを確認
    if not(len(yoteimList) == len(yoteidList) and len(yoteimList) == len(naiyouList) and len(yoteidList) == len(naiyouList)):
        return("取得した予定が不正です。")

    #Google認証
    try:
        registerCalendar.credentialGoogle()
    except:
        return("Google APIの認証中にエラーが発生しました。")
    
    #カレンダーに登録
    try:
        i=0
        while i<len(yoteimList):
            res = registerCalendar.registerCalendar(yoteimList[i], yoteidList[i], naiyouList[i], id)
            if res == "credential error":
                return("Gmailアドレスが存在しないか、カレンダーの共有設定が不正です。")
            else:
                i+=1
    except:
        return("予定の登録中にエラーが発生しました。")


    return(len(yoteimList))