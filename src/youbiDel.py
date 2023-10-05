def youbiDel(naiyou):
    while True:
        if naiyou[0] == "(":
            if naiyou[1] == "月" or naiyou[1] == "火" or naiyou[1] == "水" or naiyou[1] == "木" or naiyou[1] == "金" or naiyou[1] == "土" or naiyou[1] == "日":
                i=0
                while i<len(naiyou):
                    if naiyou[i] == ")":
                        naiyou = naiyou[i+1:]
                        break
                    i+=1
        elif naiyou[0] == "月" or naiyou[0] == "火" or naiyou[0] == "水" or naiyou[0] == "木" or naiyou[0] == "金" or naiyou[0] == "土" or naiyou[0] == "日":
            if naiyou[1] == "曜":
                if naiyou[2] == "日":
                    naiyou = naiyou[3:]
                else:
                    naiyou = naiyou[2:]
            else:
                naiyou = naiyou[1:]
        elif naiyou[0] == "," or naiyou[0] == "." or naiyou[0] == "~":
            naiyou = naiyou[1:]
        else:
            return(naiyou)
    