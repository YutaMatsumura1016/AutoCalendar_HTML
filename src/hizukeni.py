def hizukeni(yotei_han):
    yoteiList = []
    hizukeListm = []
    hizuke = ""
    hizukeListd = []
    naiyouList = []
    hizukem = ""
    hizuked = ""
    naiyou = ""

    i = 0
    t = 0
    while i<len(yotei_han):
        yoteiList.append(yotei_han[i])
        i+=1

    while t<len(yoteiList):
        #B月は入っていて、日はまだ(日を1桁入れるところまで)
        if len(hizukeListm)>0 and len(hizukeListm)<=2 and hizukeListd == []:
            # print("B")
            #B1今回が/
            if yoteiList[t] == "/" or yoteiList[t] == "月":
                hizuke = "/"
            #B2前回が数字
            elif yoteiList[t-1].isdigit():
                #B21今回も数字
                if yoteiList[t].isdigit():
                    hizukeListm.append(yoteiList[t])
                #B22今回は数字ではない
                else:
                    hizukeListm = []
                    hizuke = ""  
            #B3前回が/
            elif hizuke == "/":
                #B31今回は数字
                if yoteiList[t].isdigit():
                    hizukeListd.append(yoteiList[t])
                #B32今回は数字ではない
                else:
                    hizukeListm = []
                    hizuke = ""
        #F日に,が入っていて、月の,が1個以下。または日の,が2個以上
        elif ("," in hizukeListd and hizukeListm.count(",")<2) or hizukeListd.count(",")>1:
            # print("F")
            #F1今回が数字
            if yoteiList[t].isdigit():
                #F11次も数字
                if yoteiList[t+1].isdigit():
                    hizukeListd.append(yoteiList[t])
                #F12次は数字ではない
                else:
                    hizukeListd.append(yoteiList[t])
                    #F121次が区切り文字ではない
                    if not (yoteiList[t+1] == "." or yoteiList[t+1] == "," or yoteiList[t+1] == "~"):
                        naiyouList = yoteiList[t+1:]

            #F2今回が区切り
            elif yoteiList[t] == "." or yoteiList[t] == "," or yoteiList[t] == "~":
                #F21次の桁が数字ではない
                if not yoteiList[t+1].isdigit():
                    naiyouList = yoteiList[t+1:]
                    break
                #F22次の桁が数字
                #次かその次に月がある
                if yoteiList[t+2] == "/" or yoteiList[t+2] == "月" or yoteiList[t+3] == "/" or yoteiList[t+3] == "月":
                    hizukeListm.append(",")
                #F23ない
                else:
                    hizukeListd.append(",")
                
        #E月に,が入っている
        elif "," in hizukeListm:
            # print("E")
            #E1今回が数字
            if yoteiList[t].isdigit():
                hizukeListm.append(yoteiList[t])
            #E2今回が月
            elif yoteiList[t] == "/" or yoteiList[t] == "月":
                hizukeListd.append(",")
            #E3今回は文字(例外)
            else:
                naiyouList = yoteiList[t+1:]
        #C日が1桁入っている
        elif len(hizukeListd)==1:
            # print("C")
            #C1今回の桁も数字
            if yoteiList[t].isdigit():
                hizukeListd.append(yoteiList[t])
            #C2今回の桁は区切り
            elif yoteiList[t] == "." or yoteiList[t] == "," or yoteiList[t] == "~":
                #C21次の桁が数字ではない
                if not yoteiList[t+1].isdigit():
                    naiyouList = yoteiList[t:]
                    break
                #次の桁が数字
                #C22次かその次に月がある
                elif yoteiList[t+2] == "/" or yoteiList[t+2] == "月" or yoteiList[t+3] == "/" or yoteiList[t+3] == "月":
                    hizukeListm.append(",")
                #C23ない
                else:
                    hizukeListd.append(",")
            #C3今回の桁は文字
            else:
                naiyouList = yoteiList[t:]
                break
        #D日付が2桁入っている
        elif len(hizukeListd)==2:
            # print("D")
            #D1今回の桁が区切りでない
            if not (yoteiList[t] == "." or yoteiList[t] == "," or yoteiList[t] == "~"):
                naiyouList = yoteiList[t:]
                break
            #D2今回の桁が区切り
            elif yoteiList[t] == "." or yoteiList[t] == "," or yoteiList[t] == "~":
                #D21次の桁が数字ではない
                if not yoteiList[t+1].isdigit():
                    naiyouList = yoteiList[t+1:]
                    break
                #D22次の桁が数字
                #次かその次に月がある
                if yoteiList[t+2] == "/" or yoteiList[t+2] == "月" or yoteiList[t+3] == "/" or yoteiList[t+3] == "月":
                    hizukeListm.append(",")
                #D23ない
                else:
                    hizukeListd.append(",")

                    
        #A何も入っていない
        elif yoteiList[t].isdigit():
            # print("A")
            hizukeListm.append(yoteiList[t])
        
        t+=1

    #月の数を合わせる
    c=0
    d=0 #月の,の数
    e=0
    f=0 #日の,の数
    m=""
    while c<len(hizukeListm):
        if hizukeListm[c] == ",":
            d+=1
        c+=1
    while e<len(hizukeListd):
        if hizukeListd[e] == ",":
            f+=1
        e+=1
    if d<f:
        t=0
        while t<len(hizukeListm):
            m=m+hizukeListm[t]
            t+=1
        i=0
        while i<f:
            hizukeListm.append(",")
            hizukeListm.append(m)
            i+=1

    #文字列化
    i=0
    while i<len(hizukeListm):
        hizukem = hizukem + hizukeListm[i]
        i+=1
    t=0
    while t<len(hizukeListd):
        hizuked = hizuked + hizukeListd[t]
        t+=1
    #先頭空白削除
    if naiyouList != []:
        if naiyouList[0] == " ":
            naiyouList.pop(0)
        w=0
        while w<len(naiyouList):
            naiyou = naiyou + naiyouList[w]
            w+=1

    return hizukem, hizuked, naiyou
    