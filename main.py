from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import csv
from threading import Thread


data = []


def get_data(messages:dict, login:bool):
    driver  = webdriver.Edge()
    driver.maximize_window()

    driver.get(
        "https://login.live.com/login.srf?wa=wsignin1.0&rpsnv=13&id=264960&wreply=https%3a%2f%2fwww.bing.com%2fsecure%2fPassport.aspx%3fedge_suppress_profile_switch%3d1%26requrl%3dhttps%253a%252f%252fwww.bing.com%252fsearch%253ftoWww%253d1%2526redig%253dCF6FAA3B24AB4DB69ADB641F4381D432%2526q%253dBing%252bAI%2526showconv%253d1%2526wlexpsignin%253d1%26sig%3d300479B8A0DF658D00BB6B57A1CD6457&wp=MBI_SSL&lc=1033&CSRFToken=1df1d208-abf2-4cf1-98c8-b17e091b4dd1&aadredir=1"
    )
    sleep(2)
    if login: 
        try:
            driver.find_element(By.XPATH, '//*[@id="iNext"]').click()
            sleep(2)
        except:
            pass
        try:
            driver.find_element(By.XPATH, '//*[@id="iLooksGood"]').click()
            sleep(2)
        except:
            pass
    else:
        mail = driver.find_element(By.XPATH, '//*[@id="i0116"]')
        mail.send_keys("")  # LOGIN FROM YOUR MICROSOFT
        mail.send_keys(Keys.ENTER)
        sleep(2)
        pasw = driver.find_element(By.XPATH, '//*[@id="i0118"]')
        pasw.send_keys("")  # PASSWORD FROM YOUR MICROSOFT
        pasw.send_keys(Keys.ENTER)
    ##### THAT'S A BUTTON FOR A MICRSOSOFT SECURITY CHECK
        sleep(5)
    try:
        driver.find_element(By.XPATH, '//*[@id="iLandingViewAction"]').click()
    except:
        pass
    sleep(5)
    try:
        driver.find_element(By.XPATH, '//*[@id="idSIButton9"]').click()
    except:
        pass
    try:
        driver.find_element(By.CLASS_NAME, 'joinWaitList').click()
        sleep(10)
    except:
        pass
    ##############################
    sleep(5)
    def interceptor(request):
        del request.headers['user-agent']  # Delete the header first
        request.headers['user-agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.48'
        del request.headers['useragentreductionoptout']  # Delete the header first
        request.headers['useragentreductionoptout'] = 'A7kgTC5xdZ2WIVGZEfb1hUoNuvjzOZX3VIV/BA6C18kQOOF50Q0D3oWoAm49k3BQImkujKILc7JmPysWk3CSjwUAAACMeyJvcmlnaW4iOiJodHRwczovL3d3dy5iaW5nLmNvbTo0NDMiLCJmZWF0dXJlIjoiU2VuZEZ1bGxVc2VyQWdlbnRBZnRlclJlZHVjdGlvbiIsImV4cGlyeSI6MTY4NDg4NjM5OSwiaXNTdWJkb21haW4iOnRydWUsImlzVGhpcmRQYXJ0eSI6dHJ1ZX0='
        del request.headers['sec-ch-ua-full-version-list']
        request.headers['sec-ch-ua-full-version-list'] = ''' "Chromium";v="112.0.5615.121", "Microsoft Edge";v="112.0.1722.48", "Not:A-Brand";v="99.0.0.0"  # Delete the header first'''
        del request.headers['cookie']
        request.headers['cookie'] = '_EDGE_V=1; SRCHD=AF=NOFORM; CortanaAppUID=DAF921105AF2CDB07515C22AE42B2FC7; ABDEF=V=13&ABDV=11&MRNB=1661174093119&MRB=0; SRCHS=PC=U531; RECSEARCH=SQs=[{"q":"x, ƹ","c":1,"ad":false},{"q":"ƹ","c":1,"ad":false},{"q":"як перевірити чи точка належить відрізку","c":1,"ad":false},{"q":"як дізнатись чи належить початок координат трикутнику з вершинами a(x1 , y1), b(x2 , y2), c(x3 , y3)","c":1,"ad":false},{"q":"ъ\\\\\\\\\\\\=","c":1,"ad":false},{"q":"notw","c":1,"ad":false},{"q":"яким оператором повертається значення, що обчислює функція?","c":1,"ad":false},{"q":"malloc c","c":1,"ad":false},{"q":"справка об использовании проводника в windows","c":1,"ad":false}]; BFBUSR=BAWAS=1&BAWFS=1; MUID=0DCD243A4CE064BC3435358448E06232; _tarLang=default=ru; _TTSS_IN=hist=WyJlbiIsImF1dG8tZGV0ZWN0Il0=; _TTSS_OUT=hist=WyJydSJd; ANIMIA=FRE=1; WLID=c1MPT3yKrX40LTwmaFGyz0IDd4bnQlFL6xQhM2M+qUZrhJMITkbsFwHu8sWwq3V9XXLMDSOhAworuTxYUIQ7G9O9ass+DwEInNz0+kgF1Yw=; BFB=AhADLzn8gA6uquuOq63VYbZHoOcBrSdzSeeKIdKRLnkE9rLgkb9EGb6umKUWRoMYtASzMRi6pg2oZTnFaxx46Ujiajuli8bhbb5rH0V2S3D_5DYwMjuGuFUFOIWGhN4eQmo9Q67dKrIbNoEA9H7faFw3BVXsFZXMunncEo_FPKS-ew; OIDR=ghAuRTChhC3eECiGe45D9n8aMw2Tby-dB6A-WNUlSM35VQ_KAsx5cb_k_hJpXZmMZ7MxI1mj8Fv-8h2PyH50usEGSI6EVTIKaZ4VTOxnli5gJBdfhg5Ukp0JOfLRFFcd4v8Hrv6qpjJ6tsz7jSvvpyjgzcuQ5ecncfGWadf5b6AgSPGQaUdVdbsEeXywc-Q1JG-Uccn3be70D2QdfhIQawq0p446lpJz3_eEMVw1o6CGkUtDy9iXHG9r_fmZGo_yhnvEgTpsumplqntosOfJIKiUzbdp1QUsIT7mc-20jwo4FKczaHI7yj_fsNC7Ze_MydH6sy_RzSCqQvZodcYeSgYML8HdZI5qI2JtOLFbownND4vQnDYwOGlxGzK6zAPAZkB0kqOdBRId9ubx1LIjIwGtucqAK2ling2amjvDwxalUZPFLN91OdQCg2t7BufJ57KM5ReDwk7jEa4wKjQBgULxQQPExPl0XF7sBiLOHr5ioTROPuYdSjxhzo2opyYa25CTNNzoT5OoMmm5p0L3rF414nsEExP8XNTkaRyJILeN3qwMb6MX9JtvAoCXKSpGlAAnkH2D6ahcXDORYPvkGoYeUvrLWl8zBOZsdPXLQUlKs8NE-XIssX6H-lJk2VeGycMkud4vcq36MDvV3fqfXFqH0YI1vpbRSJwmOYGGFtmzzcQzdgGOFPdXeUbe3_5KV_ACFrHDIHyfAF4H3uU1hq3FmaFR5Arvv98WxZW3v0DJogIs4AEa_EdXS0vn1sYTkoEAXCX2I6QX_AuQ482xF-dmV35sx6nQOKbsyBnoidGdsF5lKfT1eFah2RQ1bRjQP_v8iyLEAjgTLngqTG9q88OKfQ380hYfPiMYtacbBf8HFtVS1lh40qnyai4y6ZFrHVvVggTynuWdOBKwfIA3_wKri3MpiI8NCveBGm178SeJw_9Y5uhvkIpeoFvilISnUdeExnhr40M322u34J3dU0U1lElpTtr7iW6SG0LdWgk7CUcRQHjGXQxbZFdiw3nSuC-t4KfSJ_UlW8GjqE5j51cTkvkh_vsb3qamZxfqITtHAACDggDBx2wP-YMJQ3OhzSfsfCQF6H46J7vksMmaha0ndDJMR9ZJghECB2_as9W5oQ; Imported_MUID=2AAD9C2D8ABF6E96225C8EC18B526F45; SRCHUID=V=2&GUID=356D0C6CAB2642B09FA6C8FCA2FEBD09&dmnchg=1; MUIDB=0DCD243A4CE064BC3435358448E06232; CSRFCookie=d8607172-5040-4c0c-bf40-12e51091b90f; _EDGE_S=SID=23CEBB1169E968DE2476A9FD683B6938; ANON=A=E63A8AED4664247A23D0CD2CFFFFFFFF&E=1c30&W=1; NAP=V=1.9&E=1bd6&C=F1fXiIO77kdjU5x_6wyC0UlNofQm99sLYKSneXk_ukNvXohiJGxz5Q&W=1; PPLState=1; WLS=C=dfbef626e9223830&N=Vitaliy; _BINGNEWS=SW=1903&SH=947; MicrosoftApplicationsTelemetryDeviceId=c0b9d18a-3433-41ab-966c-86d84dc7e2fb; _HPVN=CS=eyJQbiI6eyJDbiI6MSwiU3QiOjAsIlFzIjowLCJQcm9kIjoiUCJ9LCJTYyI6eyJDbiI6MSwiU3QiOjAsIlFzIjowLCJQcm9kIjoiSCJ9LCJReiI6eyJDbiI6MSwiU3QiOjAsIlFzIjowLCJQcm9kIjoiVCJ9LCJBcCI6dHJ1ZSwiTXV0ZSI6dHJ1ZSwiTGFkIjoiMjAyMy0wNC0xMFQwMDowMDowMFoiLCJJb3RkIjowLCJHd2IiOjAsIkRmdCI6bnVsbCwiTXZzIjowLCJGbHQiOjAsIkltcCI6NH0=; SRCHUSR=DOB=20230407&T=1681932927000&POEX=W&TPC=1681206936000; ipv6=hit=1681936534577&t=4; _clck=1r4287w|1|faw|0; SUID=A; USRLOC=HS=1&ELOC=LAT=49.82019805908203|LON=23.978532791137695|N=Львов, Львовская область|ELT=5|&CLOC=LAT=49.812472062279056|LON=23.971360855115652|A=733.4464586120832|TS=230419195729|SRC=W; _SS=SID=04AAFE4CA6896AAC1C60ECA0A7646BA0&R=0&RB=0&GB=0&RG=0&RP=0&OCID=MY02AE; OID=AhD-IWZTArEKPFQTD3v9DCWHEWnP5s-aEgjGYAcTjjkWBSEz60o_jsVEW4IBgQO10jBk5FzXnot9ZqbwkKScDsQOeBWM-MC1Qz-LYDdIfBrftj46CVRw_ykkcysd03pGurOK52K3HfloF8PYv0uq3MzZ; OIDI=AhB7pbpHFCZKrzEgxV4s1C5x_cHZt_f1lCC0ExLONkKG1g; SRCHHPGUSR=BRW=XW&BRH=M&CW=1863&CH=977&SCW=1846&SCH=3170&DPR=1.0&UTC=180&SRCHLANG=ru&PV=15.0.0&PRVCW=1308&PRVCH=947&DM=1&HV=1681934247&EXLTT=30&THEME=1&WTS=63816495064; dsc=order=News; KievRPSSecAuth=FACSBBRaTOJILtFsMkpLVWSG6AN6C/svRwNmAAAEgAAACDRPBRkPy6xKUAS41tPM1kjXoieDcFuE15ilU1Yc/+K9EdpMbSTAY2UGyS3bLPkiT+snDWXBV+7nJwnECTIs9idnG27LBvqRmuwRXoujBbqY+dsleaag3q3oMNjcCw5xZl7phC0X7Gl8AqOIDx5JWbaIyZO9hgx4cSXRDtBQMMyeQkHIPyXcdJW7FkNvpK5T7R8qNYmrgFLopw0nNG375Q3tcn9Mk6W7+TbgCWsGaptF2uPb31EPPQnYSeuTmkS8AXtzy9e4Xk0P2HqCEIgWIEipjBLhQlbCwsNtQeJDz9rAKIZY/aDd8s/WesnHg+R3fgxnnFbu5Rsf+rb4TPmfufOhorAA7rFUxcNeXleOc9TWJXtrOwqzz1PwYLyu0ZrbfBajRFyo3ltC5XL83kbMcOKU0f228nJ+q8EZqR0VEYThDe/DvQoRVlxtPAbqqUxcwYeXjGkDA3BvTyF8rKOsT/Jp247W+ZFQtIg42NkExuGLg3C0GcV7ojBUBrXpDYgl5zKYzLdWTJzqj33C6qBX1saIUkEXExNacxMzLN/Zw6GnNYfB7zHJMRFwZ5N99s6khBnwlNqPfIFcMFH6QK9Rb11el3o6e8gUPEg7pJmcw9TyfT3jsUiFzFDsb/wzWDyK8k/NhwRcYa1HC/n2SWH0FKUUudJ+t21TF5XGjxHyO+3bxe/PuorvY2mUWjWBxiz2G2M17ri+0Dez0jqybxqsHjyjviz7MPf1RkJx7nwOGsMSLbp92gnSkT0mAfE4/wPKKJswcmEBjxv/L81mAuPeTOlq9UjWjQJBiRXPxV2k7MS6O3TlPRXz1djMXZmMD9+caQK9SsX4RBDPST/oqFg0lJo2kUoywCArpARJ6BgW6wV3Too6aRqRxP7hyJOCej45gDCIVNYPgXXbcozmsFONBT+IFm/CjPhzwaB3C0i6rjLjFrToQlzRbhkN8eSmtPWjyOS042l2ONLorXaLlNsDrEKv6WrBdf0/ApK6HrPY6okGVG/6pEShigLeg46p7M/Yt0badR7DpqV8s/DC4kY7hOItFdGCfnIfs48OkPaEpECDGZoTqJUPTZ2KIddGHXX3Iy/k7Pg/ZhM3WsLV1XwJE7P3qB3ghkJOL/a/nHZqZcMEIGO5R6dRJCTTtXOv6mX3LB3cYNVa9evfNvIgRHfQOghtpr24coAuq4cew53r2sG4iZuutuKh4PCROg4L5RHCwuN91qo/1wQF6uqMLiZcktu/MAhZTj7xdJA7ZXNnGq+EmYDfdFLH03ycUudwXV9EX+KyNCEiyROtoDubtfXK6NZHbZIKR8w++OCV2uGq8eryaFHkALrr6paR/JL9C8mgHb2nX67P8qc1B+czRWcL7wMMmeTBWNHjdIhdRSR6vi2Jq4lx42XRl80NqAx2frg3c1EvAD6F7s52uGaBMrdbxs5m0vV3utQgqCwDSCplEpoa6Te6yf5y6Vd9NEmdXdbtty494PxVZVE4QuEUAExYq6PB+yfHAfhTJF5ZHQrMlXV2; _U=1zz-Sdm50dHtc_0sbwe3V-FK025t1W-QScivL8PNEq1APfN5HXOoFf6kIhK0-xNfIG0_xHqa-ftALin5D0am99Zt6FFK84uSrjgz84PSQt3pp6KgRim1iwKih9nRuGbiZclt2i0tIUnIVfMOxN3b5I7pw2OhTC3S0BT97qzoVV7Z82fGEjb0Bo3V4dLUrNwJn8qhsa4en0vM0AQDQNRJ7XxInjndWYSBrg5ywEQtggG8; _RwBf=ilt=2&ihpd=0&ispd=2&rc=0&rb=0&gb=0&rg=0&pc=0&mtu=0&rbb=0.0&g=0&cid=&clo=0&v=2&l=2023-04-19T07:00:00.0000000Z&lft=0001-01-01T00:00:00.0000000&aof=0&o=0&p=bingcopilotwaitlist&c=MY00IA&t=9639&s=2023-04-07T20:11:00.1465037+00:00&ts=2023-04-19T19:57:29.4775710+00:00&rwred=0&wls=2&lka=0&lkt=0&TH=&mta=0&e=wFVEwXMKlNtQvAH8xKGitWvjES89TnadDNykzazRlObVW9PNWm9dOpNzf4jVMnPjkMB9zqjpvzdFEVnfaIXYhQ&A=E63A8AED4664247A23D0CD2CFFFFFFFF; _clsk=pppaoo|1681934253426|5|1|u.clarity.ms/collect'
        del request.headers['x-client-data']
        request.headers['x-client-data'] = 'eyIxIjoiMCIsIjEwIjoiIiwiMiI6IjAiLCIzIjoiMCIsIjQiOiItMjM2NDYyNDk0ODkyODAzMjQ1MCIsIjUiOiJcInRLMXZIVTZGbjZmL21ESDdyajUyVkRpQWlsYnJtYUZGbWEzcXAvekJaVTA9XCIiLCI2Ijoic3RhYmxlIiwiNyI6IjY4NzE5NDc2NzM2MSIsIjkiOiJkZXNrdG9wIn0='


    # Set the interceptor on the driver
    driver.request_interceptor = interceptor

    for message in messages:
        driver.get(
            "https://www.bing.com/search?form=MY0291&OCID=MY0291&q=Bing+AI&showconv=1"
        )
        sleep(5)
        

        shadow_host = driver.find_element(By.CLASS_NAME, "cib-serp-main")
        shadow_root = shadow_host.shadow_root

        new_host = shadow_root.find_element(By.ID, "cib-action-bar-main")
        new_root = new_host.shadow_root

        chat_host = new_root.find_element(By.CSS_SELECTOR, "div > div.main-container > div > div.input-row > cib-text-input")
        chat_root = chat_host.shadow_root
        chat = chat_root.find_element(By.CLASS_NAME, "text-area")
        chat.send_keys(
            f"Grab me a testimonial from {message}. It can be the first case study or testimonial you find on their site."
        )
        chat.send_keys(Keys.ENTER)
        sleep(40)  # DELAY TIME

        shadow_host = driver.find_element(By.CLASS_NAME, "cib-serp-main")
        shadow_root = shadow_host.shadow_root
        new_host = shadow_root.find_element(By.ID, "cib-conversation-main")
        new_root = new_host.shadow_root
        try:
            mes_host = new_root.find_elements(
                By.CSS_SELECTOR, "#cib-chat-main > cib-chat-turn"
            )[-1]
            mes_root = mes_host.shadow_root
        except:
            sleep(5)
            try:
                mes_host = new_root.find_elements(
                    By.CSS_SELECTOR, "#cib-chat-main > cib-chat-turn"
                )[-1]
                mes_root = mes_host.shadow_root
            except:
                continue
        answer = mes_root.find_element(
            By.CLASS_NAME, "response-message-group"
        ).text.strip()
        print(answer)
        data.append([message, answer])


def save_data(data):
    header = ["URl", "Answer"]
    df = pd.DataFrame(data=data, columns=header)
    df.to_csv("1.csv", encoding="utf-8", index=False)  # FILENAME


def add_data():
    messages = []
    with open("testimonials.csv", "r", encoding="utf-8") as f:  # PATH TO CSV FILE(TO READ)
        reader = csv.reader(f, delimiter=",")
        for i, row in enumerate(reader):
            if i >= 1:
                messages.append(row[0])

    return messages


def main():

    # links = add_data()
    links= ['google.com']
    get_data(links, True)
    save_data(data=data)


if __name__ == "__main__":
    main()