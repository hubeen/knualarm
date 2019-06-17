from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from knuapp.models import dreem_singwan
from knuapp.models import staff_singwan
from knuapp.models import staff_yesan
from knuapp.models import staff_choen
from knuapp.models import Account
from knuapp.models import Announ_kongju
from knuapp.models import Announ_brain
from knuapp.models import Announ_sabum
from knuapp.models import Announ_insa
#from knuapp.models import Announ_natural
from knuapp.models import Announ_indu
from knuapp.models import Announ_cnh
from knuapp.models import Announ_art
from knuapp.models import Announ_control
from knuapp.models import Announ_cse
from knuapp.models import Announ_mech
from knuapp.models import Announ_civil
from knuapp.models import Announ_archi
from knuapp.models import Announ_archeng
from knuapp.models import Announ_ame
from knuapp.models import Announ_ie
from knuapp.models import Announ_optical
from knuapp.models import Announ_earth
from knuapp.models import Announ_chinese
from knuapp.models import Announ_eng
from knuapp.models import Announ_france
from knuapp.models import Announ_german
from knuapp.models import Announ_history
from knuapp.models import Announ_geography
from knuapp.models import Announ_economics
from knuapp.models import Announ_intrade
from knuapp.models import Announ_business
from knuapp.models import Announ_tourism
from knuapp.models import Announ_tourismenglish
from knuapp.models import Announ_public
from knuapp.models import Announ_law
from knuapp.models import Announ_socialwelfare
from knuapp.models import Announ_cm
from knuapp.models import Announ_pr
from knuapp.models import Announ_hort
from knuapp.models import Announ_ars
from knuapp.models import Announ_rce
from knuapp.models import Announ_bme
from knuapp.models import Announ_forest
from knuapp.models import Announ_la
from knuapp.models import Announ_fan
from knuapp.models import Announ_food
from knuapp.models import Announ_clas
from knuapp.models import Announ_dhm
from knuapp.models import Announ_emt
from knuapp.models import Announ_dmrhim
from knuapp.models import Announ_fdesign
from knuapp.models import Announ_dance



import json 
import certifi
import urllib3
import urllib
import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
import time
from time import gmtime, strftime
import datetime
import re
import threading
from multiprocessing import Process, Queue
from PIL import Image
urllib3.disable_warnings()

#메세지
welcome = {'type': 'buttons', 'buttons': ["서비스", "내정보", "!도움!"]}
main = {'message': {'text': '메인으로 돌아갑니다.\n'},  'keyboard': {'type': 'buttons', 'buttons': ['서비스', "내정보", "!도움!"]} }
sorry = {'message': {'text': '죄송합니다.\n이해하지 못했습니다.\n다시 시도해주세요.'}, 'keyboard': {'type': 'buttons', 'buttons':['메인', "!도움!"]}}
helps = {'message': {'text':'안녕하세요.\n컴퓨터공학부 소프트웨어전공 17학번 문승현입니다.\n이것은 공주대학교 유틸봇입니다.\n업데이트 공지는 홈에서 이루어집니다.\n많은 친구추가와 관심부탁드립니다.\n개발자에게 여자소개시켜주세요.\n버그&아이디어 제보: mhubeen@gmail.com\n감사합니다.'}, "keyboard": { "type": "buttons", "buttons": ["뒤로가기"]}}

service_list = {'message': {'text': '[공주대학교 유틸봇]\n\n현재 구현된 서비스들의 목록입니다.\n이용하실 서비스를 선택해주세요!\n'}, 'keyboard': {'type': 'buttons', 'buttons':['학식보기', '공지사항', '버스시간' , '뒤로가기']}}

haksik = {'message': {'text': '어디 캠퍼스의 학식을 보고 싶으신가요?\n'},  'keyboard': {'type': 'buttons', 'buttons': ['천안캠퍼스', "신관캠퍼스", "예산캠퍼스", "뒤로가기"]} }
call_admin = {'message': {'text': '[ERROR]\n\n알 수 없는 에러가 나타났다!\n\n사용자는 개발자에게 문의를 해주세요!'}, 'keyboard': {'type': 'buttons', 'buttons':['메인', "!도움!"]}}
notfriend = {'message': {'text': '[안내]\n\n공주대학교 봇 서비스를 이용하시려면 먼저 친구추가를 해주세요!!!\n* 만약 친구추가가 되어있어도 안내가 뜬다면 차단하였다가 다시 추가해주세요.'},'keyboard': {'type': 'buttons', 'buttons':['친구추가']}}
knucoin_main = {'message': {'text': 'KNUCOIN 서비스에 오신것을 환영합니다.\nKNUCOIN은 하루에 0.1개씩 받을 수 있습니다.\n코인으로 이용할 수  있는 서비스는 이후에 점차 늘려갈 예정입니다.'},'keyboard': {'type': 'buttons', 'buttons':['내코인', "코인 받기", '뒤로가기']}}
mypage = {'message': {'text': '[내정보] \n\n현재는 KNUCOIN 조회만 가능합니다.\n'},'keyboard': {'type': 'buttons', 'buttons':['KNUCOIN', '뒤로가기']}}


bus_noc = {'message': {'text': '[버스 시간]\n\n공주대학교에서 지원해주는 순환버스와 등교버스의 시간을 볼 수 있는 서비스입니다.\n'}, 'keyboard': {'type': 'buttons', 'buttons':['등교버스', '순환버스', '뒤로가기']}}
bus_deung = {'message': {'text': '[등교 버스]\n\n공주대학교에서 지원해주는 등교버스의 시간을 볼 수 있는 서비스입니다.\n어떤 지역에서 출발하는 버스 시간을 보시겠습니까?'}, 'keyboard': {'type': 'buttons', 'buttons':['유성', '청주', '천안', '대전', '뒤로가기']}}
bus_sun = {'message': {'text': '[순환 버스]\n\n공주대학교에서 지원해주는 순환버스의 시간을 볼 수 있는 서비스입니다.\n어떤 캠퍼스의 버스 시간을 보시겠습니까?'}, 'keyboard': {'type': 'buttons', 'buttons':['천안캠퍼스', '공주캠퍼스', '예산캠퍼스', '뒤로가기']}}


notics = {'message': {'text': '공주대학교 공지사항을 쉽게 볼 수 있는 서비스입니다.\n\n최근에 올라온 공지사항을 보여드리며 링크를 직접 들어가셔서 보시면 됩니다.\n많은 이용 바랍니다.\n'},'keyboard': {'type': 'buttons', 'buttons':['학생소식', '공과대학','사범대학', '인문사회과학대학', '산업과학대학', '간호보건대학', '예술대학',  '뒤로가기']}}
notics_value = {'message': {'text': ''},'keyboard': {'type': 'buttons', 'buttons':['메인', '뒤로가기']}}
notics_brain = {'message': {'text': '[공과대학]\n\n공과대학의 공지사항과 공과대학에 소속되있는 학부 및 학과의 공지사항을 조회하실 수 있습니다.\n공지사항을 보시고 싶은 곳을 선택해주세요.\n'},'keyboard': {'type': 'buttons', 'buttons':['공과대학공지', '컴퓨터공학부', '제어계측공학전공', '기계자동차공학부', '건설환경공학부', '건축학부', '건축공학부', '신소재공학부', '산업시스템공학과', '광공학과', '뒤로가기']}}
notics_sabum = {'message': {'text': '[사범대학]\n\n사범대학의 공지사항과 사범대학에 소속되있는 학부 및 학과의 공지사항을 조회하실 수 있습니다.\n공지사항을 보시고 싶은 곳을 선택해주세요.\n'},'keyboard': {'type': 'buttons', 'buttons':['사범대학공지', '지구과학교육과', '뒤로가기']}}
notics_insa = {'message': {'text': '[인문사회과학대학]\n\n인문사회과학대학의 공지사항과 인문사회과학대학에 소속되있는 학부 및 학과의 공지사항을 조회하실 수 있습니다.\n공지사항을 보시고 싶은 곳을 선택해주세요.\n'},'keyboard': {'type': 'buttons', 'buttons':['인문사회과학대학공지', '중어중문학과', '영어영문학과', '불어불문학과', '독어독문학과', '사학과', '지리학과', '경제학전공', '국제통상학전공', '경영학과', '관광경영학전공', '관광영어통역학전공', '행정학과', '법학과', '사회복지학과' , '뒤로가기']}}
notics_indu = {'message': {'text': '[산업과학대학]\n\n산업과학대학의  공지사항과 산업과학대학에 소속되있는 학부 및 학과의 공지사항을 조회하실 수 있습니다\n공지사항을 보시고 싶은 곳을 선택해주세요.\n'},'keyboard': {'type': 'buttons', 'buttons':['산업과학대학공지', '산업유통학과', '식물자원학과', '원예학과', '동물자원학과', '지역건설공학전공', '생물산업기계공학', '산림자원학과', '조경학과', '식품영양학전공', '식품공학과', '특수동물학과','뒤로가기']}}
notics_cnh = {'message': {'text': '[간호보건대학]\n\n간호보건대학의 공지사항과 간호보건대학에 소속되있는 학부 및 학과의 공지사항을 조회하실 수 있습니다\n공지사항을 보시고 싶은 곳을 선택해주세요.\n'}, 'keyboard': {'type': 'buttons', 'buttons':['간호보건대학공지','보건행정학과', '응급구조학과', '의료정보학과', '뒤로가기']}}
notics_art = {'message': {'text': '[예술대학]\n\n예술대학의 공지사항과 예술대학에 소속되있는 학부 및 학과의 공지사항을 조회하실 수 있습니다\n공지사항을 보시고 싶은 곳을 선택해주세요.\n'}, 'keyboard': {'type': 'buttons', 'buttons':['예술대학공지','조형디자인학부', '무용학과', '뒤로가기']}}



#학식 페이지
cheonan = {'message': {"text": "[공주대학교 천안캠퍼스]\n\n* 평일\n- 조식: 07:40 ~ 09:00 \n- 중식: 11:30 ~ 13:30\n- 석식: 17:40 ~ 19:00\n\n* 주말 및 공휴일\n- 조식:  08:00 ~ 09:00\n - 중식: 12:00 ~ 13:00\n - 석식: 18:00 ~ 19:00\n\n어디 식당의 식단을 보시겠습니까?"},
    'keyboard': {'type': 'buttons', 'buttons': ['생활관 식당', "학생 식당", "직원 식당","메인", "뒤로가기"]}
}
singwan = {
    'message': {'text': '[공주대학교 신관캠퍼스]\n\n* 평일\n- 조식: 07:30 ~ 08:30\n- 중식: 11:30 ~ 13:30\n- 석식: 17:30 ~ 19:00\n\n* 주말 및 공휴일\n- 조식: 07:30 ~ 08:30\n- 중식: 12:00 ~ 13:00\n- 석식: 18:00 ~ 19:00\n\n어디 식당의 식단을 보시겠습니까?'},
    'keyboard': {'type': 'buttons', 'buttons': ['생활관 식당', "학생 식당", "직원 식당","메인", "뒤로가기"]}
}

yesan = { 
    'message': {'text': '[공주대학교 예산캠퍼스]\n\n* 평일\n- 조식: 08:00 ~ 09:00\n- 중식: 11:40 ~ 13:30\n- 석식: 17:40 ~ 19:00\n\n* 주말 및 공휴일\n- 조식: 08:00 ~ 09:00\n- 중식: 12:00 ~ 13:00\n- 석식: 18:00 ~ 19:00\n\n어디 식당의 식단을 보시겠습니까?'},
    'keyboard': {'type': 'buttons', 'buttons': ["학생 식당", "직원 식당", "메인", "뒤로가기"]}
}

singwan_dormi = {'message': {'text': '[공주대학교 신관캠퍼스 기숙사]\n\n어디 기숙사의 식단을 보시겠습니까?'},  'keyboard': {'type': 'buttons', 'buttons': ["은행사/비전", "드림하우스", "메인"]} }

alert = {'message': {'text': "현재 구현이 되지 않은 상태입니다. 죄송합니다. 빠른 시간안에 개발을 마치도록 노력하겠습니다."}, 'keyboard': {'type': 'buttons', 'buttons': ["메인"]}}


week = ['월', '화', '수', '목', '금', '토', '일']

# DB선언
dreem = dreem_singwan
staff_ch = staff_choen
staff_ye = staff_yesan
staff_si = staff_singwan
Account = Account
Announs_kongju = Announ_kongju
Announs_brain = Announ_brain
Announs_sabum = Announ_sabum
Announs_insa = Announ_insa
#Announs_natural = Announ_natural
Announs_indu = Announ_indu
Announs_cnh = Announ_cnh
Announs_art = Announ_art
Announs_control = Announ_control
Announs_cse = Announ_cse
Announs_mech = Announ_mech
Announs_civil = Announ_civil
Announs_archi = Announ_archi
Announs_archeng = Announ_archeng
Announs_ame = Announ_ame
Announs_ie = Announ_ie
Announs_optical = Announ_optical
Announs_earth = Announ_earth
Announs_chinese = Announ_chinese
Announs_eng = Announ_eng
Announs_france = Announ_france
Announs_german = Announ_german
Announs_history = Announ_history
Announs_geography = Announ_geography
Announs_economics = Announ_economics
Announs_intrade = Announ_intrade
Announs_business = Announ_business
Announs_tourism = Announ_tourism
Announs_tourismenglish = Announ_tourismenglish
Announs_public = Announ_public
Announs_law = Announ_law
Announs_socialwelfare = Announ_socialwelfare
Announs_cm =Announ_cm
Announs_pr =Announ_pr
Announs_hort =Announ_hort
Announs_ars =Announ_ars
Announs_rce =Announ_rce
Announs_bme =Announ_bme
Announs_forest =Announ_forest
Announs_la =Announ_la
Announs_fan =Announ_fan
Announs_food =Announ_food
Announs_clas =Announ_clas
Announs_dhm = Announ_dhm
Announs_emt = Announ_emt
Announs_dmrhim =Announ_dmrhim
Announs_fdesign = Announ_fdesign
Announs_dance = Announ_dance


# 큐 선언
dreem_q = Queue()
staff_ch_q = Queue()
staff_ye_q = Queue()
staff_si_q = Queue()
Account_q = Queue()
Announs_kongju_q = Queue()
Announs_brain_q = Queue()
Announs_sabum_q = Queue()
Announs_insa_q = Queue()
#Announs_natural_q = Queue()
Announs_indu_q = Queue()
Announs_cnh_q = Queue()
Announs_art_q = Queue()
Announs_control_q = Queue()
Announs_cse_q = Queue()
Announs_mech_q = Queue()
Announs_civil_q = Queue()
Announs_archi_q = Queue()
Announs_archeng_q = Queue()
Announs_ame_q = Queue()
Announs_ie_q = Queue()
Announs_optical_q = Queue()
Announs_earth_q = Queue()
Announs_chinese_q = Queue()
Announs_eng_q = Queue()
Announs_france_q = Queue()
Announs_german_q = Queue()
Announs_history_q = Queue()
Announs_geography_q = Queue()
Announs_economics_q = Queue()
Announs_intrade_q = Queue()
Announs_business_q = Queue()
Announs_tourism_q = Queue()
Announs_tourismenglish_q = Queue()
Announs_public_q = Queue()
Announs_law_q = Queue()
Announs_socialwelfare_q = Queue()
Announs_cm_q =Queue()
Announs_pr_q =Queue()
Announs_hort_q =Queue()
Announs_ars_q =Queue()
Announs_rce_q =Queue()
Announs_bme_q =Queue()
Announs_forest_q =Queue()
Announs_la_q =Queue()
Announs_fan_q =Queue()
Announs_food_q = Queue()
Announs_clas_q = Queue()
Announs_dhm_q =  Queue()
Announs_emt_q =  Queue()
Announs_dmrhim_q = Queue()
Announs_fdesign_q =  Queue()
Announs_dance_q =  Queue()


def db_get(self, days):
    try:
        result = self.objects.filter(day=days)[0].content
        return result
    except:
        return "X"

def db_add_friend(_ids):
    try:
        Account.objects.get(ids=_ids).idx
    except:
        Account(ids=_ids).save()

def db_not_friend(_ids):
    try:
        Account.objects.get(ids=_ids).idx
    except:
        return "X"

def db_get_idx(_ids):
    return Account.objects.get(ids=_ids).idx

def db_update_idx(_ids, _idx):
	try:
		Account.objects.filter(ids=_ids).update(idx=_idx)
	except:
		return "X"
def db_check(self, days):
    try:
        result = self.objects.filter(day=days)[0]
        return result
    except:
        return "X"

def db_insert(self,contents):
	try:
		string = strftime("%y.%m.%d", time.localtime())
		self(day=string, content=contents).save()
	except:
		return "X"

def db_get_Lasted(_ids):
    return Account.objects.get(ids=_ids).lasted

def get_point(_ids):
    return Account.objects.get(ids=_ids).point

def give_point(_ids):
    now = datetime.datetime.now()
    s_Lasted = now.strftime("%y-%m-%d")
    u_Lasted = db_get_Lasted(_ids)
    user_time = datetime.datetime.strptime(u_Lasted, '%y-%m-%d')
    serv_time = datetime.datetime.strptime(s_Lasted, '%y-%m-%d')
    val = serv_time - user_time
    point = Account.objects.get(ids=_ids).point
    gives = (0.1*val.days)
    point += gives
    Account.objects.filter(ids=_ids).update(point=point)
    Account.objects.filter(ids=_ids).update(lasted=s_Lasted)
    if(val.days == 0):
        return "X"
    else:
        return gives

def ViewImage(request, param):
	image_data = open("/home/hubeen/Prjct/knualram/knuapp/bus/" + param + ".png", "rb").read()
	return HttpResponse(image_data, content_type="image/png")

def image_lnk(name):
	image_data = im = Image.open("/home/hubeen/Prjct/knualram/knuapp/bus/" + name + ".png")
	sz = image_data.size
	lnk = "http://hubeen.kr:8000/bus/" + urllib.parse.quote_plus(name)
	return sz, lnk

def get_kongju_Announ(q): #학생소식
    url = {}
    http = urllib3.PoolManager()
    r = http.request('GET', 'http://www.kongju.ac.kr/lounge/board.jsp?board=student_news&page=0')
    sc =  r.data.decode('cp949', 'ignore')
    cd = BeautifulSoup(sc, "html.parser")
    tb = cd.find("table", class_="content_main_table02").find_all("a", href=True)
    for i, cnt in zip(tb, range(len(tb))):
        if(i['title'] != ""):
            url[cnt] = [i['title'], "http://www.kongju.ac.kr/lounge/"+i['href']]

    q.put(json.dumps(url))

def get_brain_Announ(q): #공과대학
    url = {}
    http = urllib3.PoolManager()
    r = http.request('GET', 'http://brain.kongju.ac.kr/brain/cop/bbs/selectBoardList.do?bbsId=BBSMSTR_000000000001')
    sc =  r.data.decode('utf-8')
    cd = BeautifulSoup(sc, "html.parser")
    tb = cd.find("div", class_="courses").find_all("a", href=True)
    for i, cnt in zip(tb, range(len(tb))):
        if(i.text != ""):
            tmp =  i['onclick'].split("fn_egov_inqire_notice(")[1].split(");")[0].replace("'","").replace(" ", "")
            tmp = tmp.split(',')
            url_tmp = "http://brain.kongju.ac.kr/brain/cop/bbs/selectBoardArticle.do?bbsId=" + tmp[1] +"&nttId=" + tmp[0]
            url[cnt] = [i.text , url_tmp]

    q.put(json.dumps(url))

def get_sabum_Announ(q):#사범대학
    url = {}
    http = urllib3.PoolManager()
    r = http.request('GET', 'http://sabum.kongju.ac.kr/custo/list.asp?bbs_code=7')
    sc =  r.data.decode('cp949', 'ignore')
    cd = BeautifulSoup(sc, "html.parser")
    tb = cd.find("table", {"id":"bbs_list_tbl"}).find_all("a", href=True)
    for i, cnt in zip(tb, range(len(tb))):
        if(i.text != ""):
            tmp = i['onclick'].split("viewGo(")[1].split(",")[0]
            url_tmp = "http://sabum.kongju.ac.kr/custo/view.asp?idx="+ tmp +"&page=1&bbs_code=7"
            url[cnt] = [i.text , url_tmp]

    q.put(json.dumps(url))

def get_insa_Announ(q): #인문사회과학대학
    url = {}
    http = urllib3.PoolManager()
    r = http.request('GET', 'https://insa.kongju.ac.kr/main/board/list.action?q=518da08fa3d7eab65226f7de6f82ae4f1be5aadc235d7f9e817ad3dea247a499')
    sc =  r.data.decode('utf-8')
    cd = BeautifulSoup(sc, "html.parser")
    tb = cd.find("table", class_="body-list-board").find_all("a", href=True)
    for i, cnt in zip(tb, range(len(tb))):
        if(i.text != ""):
            url[cnt] = [i.text, "https://insa.kongju.ac.kr" + i['href']]
    q.put(json.dumps(url))

def get_natural_Announ(q): #자연과학대학
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    url = {}
    http = urllib3.PoolManager()
    r = http.request('GET', 'http://natural.kongju.ac.kr/news', headers={'User-Agent':'Mozilla/5.0'})
    sc = r.data.decode('utf-8')
    cd = BeautifulSoup(sc, "html.parser")
    tb = cd.find("tbody").find_all("a", href=True)
    for i, cnt in zip(tb, range(len(tb))):
        if(i.text != ""):
            url[cnt] = [i.text, i['href']]
    q.put(json.dumps(url))

def get_indu_Announ(q): #산업과학대학
    url = {}
    http = urllib3.PoolManager()
    r = http.request('GET', 'http://indu.kongju.ac.kr/board.do?paramBean.key=65&paramBean.mainGroupKey=1&boardBean.boardMngKey=1')
    sc = r.data.decode('utf-8')
    cd = BeautifulSoup(sc, "html.parser")
    tb = cd.find_all("span")
    for i, cnt in zip(tb, range(len(tb))):
        if(i.text != ""):
            tmp = i['onclick'].split(', ')[1].split(')')[0]
            url_tmp = "http://indu.kongju.ac.kr/board.do?org.apache.struts.taglib.html.TOKEN=17e8cdfe30d15523c996ee4028c725f3&boardBean.boardKey=" + tmp + "&boardBean.boardMngKey=1&paramBean.key=65&paramBean.homepageKey=0&paramBean.mainGroupKey=1&paramBean.page=0&action=view&boardBean.passwd=&paramBean.searchType=subject&paramBean.searchWord="
            url[cnt] = [i.text, url_tmp]
    q.put(json.dumps(url))

def get_cnh_Announ(q): #간호보건대학
    url = {}
    http = urllib3.PoolManager()
    r = http.request('GET', 'http://cnh.kongju.ac.kr/sub03/service_01_list.asp')
    sc = r.data.decode('cp949', 'ignore')
    cd = BeautifulSoup(sc, "html.parser")
    tb = cd.find("div", class_="cont_body").find_all("a", href=True)
    for i, cnt in zip(tb, range(len(tb))):
        if(i.text != ""):
            url[cnt] = [i.text, "http://cnh.kongju.ac.kr/sub03/" + i['href']]
    q.put(json.dumps(url))

def get_art_Announ(q): #예술대학
    url = {}
    http = urllib3.PoolManager()
    r = http.request('GET', 'http://art.kongju.ac.kr/sub03/sub01_01.jsp?menuNo=3&subNo=1')
    sc = r.data.decode('utf-8')
    cd = BeautifulSoup(sc, "html.parser")
    tb = cd.find("div", class_="board_list").find_all("a", href=True)
    for i, cnt in zip(tb, range(len(tb))):
        if(i.text != ""):
            url[cnt] = [ i.text, "http://art.kongju.ac.kr/sub03" +i['href'].replace(".","")]

    q.put(json.dumps(url))

def get_control_Announ(q): # 제어계측공학전공
    url = {}
    http = urllib3.PoolManager()
    r = http.request('GET', 'http://control.kongju.ac.kr/Service/board/BoardList.aspx?categ=g1')
    sc = r.data.decode('utf-8')
    cd = BeautifulSoup(sc, "html.parser")
    tb = cd.find_all("tr")
    for i, cnt in zip(tb, range(len(tb))):
        tmp = i.find("a", href=True)
        if(tmp != None):
            if(tmp.text != ""):
                url[cnt] = [tmp.text.strip(), "http://control.kongju.ac.kr/Service/board/BoardItem.aspx?categ=g1&page=1&bidx=" + tmp['onclick'].split("goItem('")[1].split("')")[0]]
    q.put(json.dumps(url))

def get_cse_Announ(q): # 컴퓨터공학부
    url = {}
    http = urllib3.PoolManager()
    r = http.request('GET', 'http://cse.kongju.ac.kr/community/notice.asp')
    sc = r.data.decode('utf-8')
    cd = BeautifulSoup(sc, "html.parser")
    tb = cd.find("table", class_="lmcGeneralList").find_all("a", href=True)
    for i, cnt in zip(tb, range(len(tb))):
        if(i.text != ""):
            url[cnt] = [i.text.strip(), "http://cse.kongju.ac.kr" + i['href']]
    q.put(json.dumps(url))

def get_mech_Announ(q): #기계자동차공학부
    url = {}
    http = urllib3.PoolManager()
    r = http.request('GET', 'http://mech.kongju.ac.kr/community/community01_notice.asp?lmCode=notice')
    sc = r.data.decode('utf-8')
    cd = BeautifulSoup(sc, "html.parser")
    tb = cd.find("table", class_="lmcGeneralList").find_all("a", href=True)
    for i, cnt in zip(tb, range(len(tb))):
        if(i.text != ""):
            url[cnt] = [i.text.strip(), "http://mech.kongju.ac.kr" + i['href']]

    q.put(json.dumps(url))


def get_civil_Announ(q): #건설환경공학부
    url = {}
    http = urllib3.PoolManager()
    r = http.request('GET', 'http://civil.kongju.ac.kr/community/community01_notice.asp')
    sc = r.data.decode('utf-8')
    cd = BeautifulSoup(sc, "html.parser")
    tb = cd.find("table", class_="lmcGeneralList").find_all("a", href=True)
    for i, cnt in zip(tb, range(len(tb))):
        if(i.text != ""):
            url[cnt] = [i.text.strip(), "http://civil.kongju.ac.kr" + i['href']]

    q.put(json.dumps(url))

def get_archi_Announ(q): #건축학부
    url = {}
    http = urllib3.PoolManager()
    r = http.request('GET', 'http://archi.kongju.ac.kr/notice/list_hi.asp')
    sc = r.data
    cd = BeautifulSoup(sc, "html.parser")
    tb = cd.find("section", {"id":"content"}).find_all("a", href=True)
    for i, cnt in zip(tb, range(len(tb))):
        tmp_href = i['href']
        if(tmp_href.find('download') > 0):
            if(i.text != ""):
                url[cnt] = [i.text.strip(), "http://archi.kongju.ac.kr/notice/view_hi.asp?idx="+ tmp_href.split("view_send('")[1].split("')")[0] +"&search=&find=&gotopage=1&keyword="]
    q.put(json.dumps(url))

def get_archeng_Announ(q): #건축공학부
    url = {}
    http = urllib3.PoolManager()
    r = http.request('GET', 'http://archeng.kongju.ac.kr/notice/list_hi.asp')
    sc = r.data
    cd = BeautifulSoup(sc, "html.parser")
    tb = cd.find("table", class_="b_txt").find_all("a", href=True)
    for i, cnt in zip(tb, range(len(tb))):
        tmp_href = i['href']
        if(tmp_href.find('download') > 0):
            if(i.text != ""):
                url[cnt] = [i.text.strip(), "http://archeng.kongju.ac.kr/notice/view_hi.asp?idx=" + tmp_href.split("view_send('")[1].split("')")[0] + "&search=&find=&gotopage=1&keyword="]

    q.put(json.dumps(url))

def get_ame_Announ(q): #신소재공학부
    url = {}
    http = urllib3.PoolManager()
    r = http.request('GET','http://ame.kongju.ac.kr/community/notice.asp')
    sc = r.data
    cd = BeautifulSoup(sc, "html.parser")
    tb = cd.find("table", class_="lmcGeneralList").find_all("a", href=True)
    for i, cnt in zip(tb, range(len(tb))):
        if(i.text != ""):
            url[cnt] = [i.text.strip(), "http://ame.kongju.ac.kr" + i['href']]
    q.put(json.dumps(url))

def get_ie_Announ(q): #산업시스템공학과
    url = {}
    http = urllib3.PoolManager()
    r = http.request('GET','http://ie.kongju.ac.kr/index.php?mid=board_lhSN77')
    sc = r.data
    cd = BeautifulSoup(sc, "html.parser")
    tb = cd.find("table").find_all("a", href=True)
    for i, cnt in zip(tb, range(len(tb))):
        tmp_href = i['href']
        if(tmp_href.find('document_srl') > 0):
            if(i.text != ""):
                url[cnt] = [i.text.strip(), "http://ie.kongju.ac.kr/" + tmp_href]

    q.put(json.dumps(url))

def get_optical_Announ(q): #광공학과
    url = {}
    http = urllib3.PoolManager()
    r = http.request('GET','http://optical.kongju.ac.kr/sub5_4.php')
    sc = r.data
    cd = BeautifulSoup(sc, "html.parser")
    tb = cd.find("table", class_="ezsboard_td").find_all("a", class_="ezsboard", href=True)
    for cnt in  range(1, len(tb), 3):
        url[cnt] = [tb[cnt].text.strip(), "http://optical.kongju.ac.kr" + tb[cnt]['href']]

    q.put(json.dumps(url))


def get_earth_Announ(q): #지구과학교육과
    url = {}
    http = urllib3.PoolManager()
    r = http.request('GET', 'http://earth.kongju.ac.kr/modules/bbs/index.php?code=bbs_notice&xid=1')
    sc = r.data
    cd = BeautifulSoup(sc, "html.parser")
    tb = cd.find("table", {'summary' : '게시판 리스트'}).find_all("a", href=True)
    for i, cnt in zip(tb, range(len(tb))):
        url[cnt] = [i.text.strip(), "http://earth.kongju.ac.kr/modules/bbs/" + i['href']]

    q.put(json.dumps(url))

def get_chinese_Announ(q): #중어중문학과
    url = {}
    http = urllib3.PoolManager(
        cert_reqs='CERT_REQUIRED',
        ca_certs=certifi.where())
    r = http.request('GET', "https://chinese.kongju.ac.kr/main/board/list.action?q=687b8a3da22c72e2b2c4dbb5ccd9fec6f04bbfbd0ab55e8c75702d55310b360a")
    sc = r.data.decode('utf-8')
    cd = BeautifulSoup(sc, "html.parser")
    tb = cd.find("table", class_="body-list-board").find_all("a", class_="ajax", href=True)
    for i, cnt in zip(tb, range(len(tb))):
        url[cnt] = [i.text.strip(), "https://chinese.kongju.ac.kr" + i['href']]
    q.put(json.dumps(url))

def get_eng_Announ(q): #영어영문학과
    url = {}
    http = urllib3.PoolManager(
        cert_reqs='CERT_REQUIRED',
        ca_certs=certifi.where())
    r = http.request('GET', "https://eng.kongju.ac.kr/main/board/list.action?q=b52b1cc0bce6b3dadae85bd05fcff8f9920bef22a31f7988402af1e831f1f4e2")
    sc = r.data.decode('utf-8')
    cd = BeautifulSoup(sc, "html.parser")
    tb = cd.find("table", class_="body-list-board").find_all("a", class_="ajax", href=True)
    for i, cnt in zip(tb, range(len(tb))):
        url[cnt] = [i.text.strip(), "https://eng.kongju.ac.kr" + i['href']]
    q.put(json.dumps(url))

def get_france_Announ(q): #불어불문학과
    url = {}
    http = urllib3.PoolManager(
        cert_reqs='CERT_REQUIRED',
        ca_certs=certifi.where())
    r = http.request('GET', "https://france.kongju.ac.kr/main/board/list.action?q=ce5e552b4e7cf87d82656b30ef82d54a0dc42f9881d3ffff7681ed818518119b")
    sc = r.data.decode('utf-8')
    cd = BeautifulSoup(sc, "html.parser")
    tb = cd.find("table", class_="body-list-board").find_all("a", class_="ajax", href=True)
    for i, cnt in zip(tb, range(len(tb))):
        url[cnt] = [i.text.strip(), "https://france.kongju.ac.kr" + i['href']]
    q.put(json.dumps(url))

def get_german_Announ(q): #독어독문학과
    url = {}
    http = urllib3.PoolManager(
        cert_reqs='CERT_REQUIRED',
        ca_certs=certifi.where())
    r = http.request('GET', 'https://german.kongju.ac.kr/main/board/list.action?q=b5f4f8d9282662cb73c5239efaff36951b3f102131ff65b93b4f67dbe9ade2f8')
    sc = r.data.decode('utf-8')
    cd = BeautifulSoup(sc, "html.parser")
    tb = cd.find("table", class_="body-list-board").find_all("a", class_="ajax", href=True)
    for i, cnt in zip(tb, range(len(tb))):
        url[cnt] = [i.text.strip(), "https://german.kongju.ac.kr" + i['href']]
    q.put(json.dumps(url))

def get_history_Announ(q): # 사학과
    url = {}
    http = urllib3.PoolManager(
        cert_reqs='CERT_REQUIRED',
        ca_certs=certifi.where())
    r = http.request('GET', 'https://history.kongju.ac.kr/main/board/list.action?q=35ce2fb7844998cef838806f4c03f619d2cef4419f8d25662dc9889b3a25288a')
    sc = r.data.decode('utf-8')
    cd = BeautifulSoup(sc, "html.parser")
    tb = cd.find("table", class_="body-list-board").find_all("a", class_="ajax", href=True)
    for i, cnt in zip(tb, range(len(tb))):
        url[cnt] = [i.text.strip(), "https://history.kongju.ac.kr" + i['href']]
    q.put(json.dumps(url))

def get_geography_Announ(q): # 지리학과
    url = {}
    http = urllib3.PoolManager(
        cert_reqs='CERT_REQUIRED',
        ca_certs=certifi.where())
    r = http.request('GET', 'https://geography.kongju.ac.kr/main/board/list.action?q=cdb3681a44e37ae275be41fb471cc683554785794af396abeea292c6de7836dc')
    sc = r.data.decode('utf-8')
    cd = BeautifulSoup(sc, "html.parser")
    tb = cd.find("table", class_="body-list-board").find_all("a", class_="ajax", href=True)
    for i, cnt in zip(tb, range(len(tb))):
        url[cnt] = [i.text.strip(), "https://geography.kongju.ac.kr" + i['href']]
    q.put(json.dumps(url))

def get_economics_Announ(q): # 경제학전공
    url = {}
    http = urllib3.PoolManager(
        cert_reqs='CERT_REQUIRED',
        ca_certs=certifi.where())
    r = http.request('GET', 'https://economics.kongju.ac.kr/main/board/list.action?q=17604b01febc0b8ed3ce6d35048949367b383680c2e3ae0d1aa6762a14dba7b8')
    sc = r.data.decode('utf-8')
    cd = BeautifulSoup(sc, "html.parser")
    tb = cd.find("table", class_="body-list-board").find_all("a", class_="ajax", href=True)
    for i, cnt in zip(tb, range(len(tb))):
        url[cnt] = [i.text.strip(), "https://economics.kongju.ac.kr" + i['href']]
    q.put(json.dumps(url))

def get_intrade_Announ(q): # 국제통상학전공
    url = {}
    http = urllib3.PoolManager(
        cert_reqs='CERT_REQUIRED',
        ca_certs=certifi.where())
    r = http.request('GET', 'https://in-trade.kongju.ac.kr/main/board/list.action?q=7da1388c52154ee93dc9fd442967a6592f8482dee1b5002e0c3d09b4990a61a7')
    sc = r.data.decode('utf-8')
    cd = BeautifulSoup(sc, "html.parser")
    tb = cd.find("table", class_="body-list-board").find_all("a", class_="ajax", href=True)
    for i, cnt in zip(tb, range(len(tb))):
        url[cnt] = [i.text.strip(), "https://in-trade.kongju.ac.kr" + i['href']]
    q.put(json.dumps(url))

def get_business_Announ(q): #경영학과
    url = {}
    http = urllib3.PoolManager(
        cert_reqs='CERT_REQUIRED',
        ca_certs=certifi.where())
    r = http.request('GET', 'https://business.kongju.ac.kr/main/board/list.php?q=ac42a8ee5de8e31953f26465634a292ffef153f1e615403e98c3363d772be26d')
    sc = r.data.decode('utf-8')
    cd = BeautifulSoup(sc, "html.parser")
    tb = cd.find("table", class_="body-list-board").find_all("a", class_="ajax", href=True)
    for i, cnt in zip(tb, range(len(tb))):
        url[cnt] = [i.text.strip(), "https://business.kongju.ac.kr" + i['href']]
    q.put(json.dumps(url))

def get_tourism_Announ(q): #관광경영학전공
    url = {}
    http = urllib3.PoolManager(
        cert_reqs='CERT_REQUIRED',
        ca_certs=certifi.where())
    r = http.request('GET', 'https://tourism.kongju.ac.kr/main/board/list.action?mid=45&tblname=20170220115514')
    sc = r.data.decode('utf-8')
    cd = BeautifulSoup(sc, "html.parser")
    tb = cd.find("table", class_="body-list-board").find_all("a", class_="ajax", href=True)
    for i, cnt in zip(tb, range(len(tb))):
        url[cnt] = [i.text.strip(), "https://tourism.kongju.ac.kr" + i['href']]
    q.put(json.dumps(url))

def get_tourismenglish_Announ(q):#관광영어통역학전공
    url = {}
    http = urllib3.PoolManager(
        cert_reqs='CERT_REQUIRED',
        ca_certs=certifi.where())
    r = http.request('GET', 'https://tourismenglish.kongju.ac.kr/main/board/list.action?q=be6bd668202f04f7f855ce3d8ba84c2cecd64e0535ace7732482621bc7bff738')
    sc = r.data.decode('utf-8')
    cd = BeautifulSoup(sc, "html.parser")
    tb = cd.find("table", class_="body-list-board").find_all("a", class_="ajax", href=True)
    for i, cnt in zip(tb, range(len(tb))):
        url[cnt] = [i.text.strip(), "https://tourismenglish.kongju.ac.kr" + i['href']]
    q.put(json.dumps(url))

def get_public_Announ(q): #행정학과
    url = {}
    http = urllib3.PoolManager(
        cert_reqs='CERT_REQUIRED',
        ca_certs=certifi.where())
    r = http.request('GET', 'https://public.kongju.ac.kr/main/board/list.action?q=bfed3d4ebb5a0d13ff86489010dd05f3fa81ea0ac9f2569c386ce847a9b06ad7')
    sc = r.data.decode('utf-8')
    cd = BeautifulSoup(sc, "html.parser")
    tb = cd.find("table", class_="body-list-board").find_all("a", class_="ajax", href=True)
    for i, cnt in zip(tb, range(len(tb))):
        url[cnt] = [i.text.strip(), "https://public.kongju.ac.kr" + i['href']]
    q.put(json.dumps(url))

def get_law_Announ(q): #법학과
    url = {}
    http = urllib3.PoolManager(
        cert_reqs='CERT_REQUIRED',
        ca_certs=certifi.where())
    r = http.request('GET', 'https://law.kongju.ac.kr/main/board/list.action?q=664a797ffe90e82d44b0dc03b3574813feb258cf32bf82e6532f6d323cb59b92')
    sc = r.data.decode('utf-8')
    cd = BeautifulSoup(sc, "html.parser")
    tb = cd.find("table", class_="body-list-board").find_all("a", class_="ajax", href=True)
    for i, cnt in zip(tb, range(len(tb))):
        url[cnt] = [i.text.strip(), "https://law.kongju.ac.kr" + i['href']]
    q.put(json.dumps(url))

def get_socialwelfare_Announ(q): #사회복지학과
    url = {}
    http = urllib3.PoolManager(
        cert_reqs='CERT_REQUIRED',
        ca_certs=certifi.where())
    r = http.request('GET', 'https://socialwelfare.kongju.ac.kr/main/board/list.action?q=b01c5dc5232539702f7ca5952435274febe3ce4f9fc4c36bff1f4f43ec8b3e9d')
    sc = r.data.decode('utf-8')
    cd = BeautifulSoup(sc, "html.parser")
    tb = cd.find("table", class_="body-list-board").find_all("a", class_="ajax", href=True)
    for i, cnt in zip(tb, range(len(tb))):
        url[cnt] = [i.text.strip(), "https://socialwelfare.kongju.ac.kr" + i['href']]
    q.put(json.dumps(url))

def get_cm_Announ(q): #산업유통학과
    url = {}
    http = urllib3.PoolManager()
    r = http.request('GET', 'http://cm.kongju.ac.kr/community/community01_notice.asp')
    sc = r.data.decode('utf-8')
    cd = BeautifulSoup(sc, "html.parser")
    tb = cd.find("table", class_="lmcGeneralList").find_all("a", href=True)
    for i,cnt in zip(tb, range(len(tb))):
        url[cnt] = [i.text.strip(), "http://cm.kongju.ac.kr" + i['href']]
    q.put(json.dumps(url))

def get_pr_Announ(q): #식물자원학과
    url = {}
    http = urllib3.PoolManager()
    r = http.request('GET', 'http://pr.kongju.ac.kr/board.do?paramBean.key=72&paramBean.mainGroupKey=1&boardBean.boardMngKey=7')
    sc = r.data.decode('utf-8')
    cd = BeautifulSoup(sc, "html.parser")
    tb = cd.find("table", {"border": "0"}).find_all("span", {"style": "cursor:hand"})
    for i, cnt in zip(tb, range(len(tb))):
        url[cnt] = [i.text.strip(), "http://pr.kongju.ac.kr/board.do?org.apache.struts.taglib.html.TOKEN=2698c3c591319fbf2365b0c9e54599e9&boardBean.boardKey="+ i['onclick'].split("'view', ")[1].split(")")[0] +"&boardBean.boardMngKey=7&paramBean.key=72&paramBean.homepageKey=0&paramBean.mainGroupKey=1&paramBean.page=0&action=view&boardBean.passwd=&paramBean.searchType=subject&paramBean.searchWord="]

    q.put(json.dumps(url))

def get_hort_Announ(q): #원예학과
    url = {}
    http = urllib3.PoolManager()
    r = http.request('GET', 'http://hort.kongju.ac.kr/board.do?paramBean.key=27&paramBean.mainGroupKey=1&boardBean.boardMngKey=2')
    sc = r.data.decode('utf-8')
    cd = BeautifulSoup(sc, "html.parser")
    tb = cd.find("table", {"border": "0"}).find_all("span", {"style": "cursor:hand"})
    for i, cnt in zip(tb, range(len(tb))):
        url[cnt] = [i.text.strip(), "http://hort.kongju.ac.kr/board.do?org.apache.struts.taglib.html.TOKEN=d114482681b2cc3ec83d140a3d20db41&boardBean.boardKey="+ i['onclick'].split("'view', ")[1].split(")")[0] +"&boardBean.boardMngKey=2&paramBean.key=27&paramBean.homepageKey=0&paramBean.mainGroupKey=1&paramBean.page=0&action=view&boardBean.passwd=&paramBean.searchType=subject&paramBean.searchWord="]

    q.put(json.dumps(url))

def get_ars_Announ(q): #동물자원학과
    url = {}
    http = urllib3.PoolManager()
    r = http.request('GET', 'http://ars.kongju.ac.kr/board.do?paramBean.key=60&paramBean.mainGroupKey=1&boardBean.boardMngKey=7')
    sc = r.data.decode('utf-8')
    cd = BeautifulSoup(sc, "html.parser")
    tb = cd.find("table", {"border": "0"}).find_all("span", {"style": "cursor:hand"})
    for i, cnt in zip(tb, range(len(tb))):
        url[cnt] = [i.text.strip(), "http://ars.kongju.ac.kr/board.do?org.apache.struts.taglib.html.TOKEN=30dca517940168fc5ea5c4c5ae7c951d&boardBean.boardKey=" + i['onclick'].split("'view', ")[1].split(")")[0] +"&boardBean.boardMngKey=7&paramBean.key=60&paramBean.homepageKey=0&paramBean.mainGroupKey=1&paramBean.page=0&action=view&boardBean.passwd=&paramBean.searchType=subject&paramBean.searchWord="]

    q.put(json.dumps(url))

def get_rce_Announ(q): #지역건설공학전공
    url = {}
    http = urllib3.PoolManager()
    r = http.request('GET','http://rce.kongju.ac.kr/board.do?paramBean.key=23&paramBean.mainGroupKey=1&boardBean.boardMngKey=1')
    sc = r.data.decode('utf-8')
    cd = BeautifulSoup(sc, "html.parser")
    tb = cd.find("table", {"border": "0"}).find_all("span", {"style": "cursor:hand"})
    for i, cnt in zip(tb, range(len(tb))):
        url[cnt] = [i.text.strip(), "http://rce.kongju.ac.kr/board.do?org.apache.struts.taglib.html.TOKEN=d68e4b5ab64e325f8595a32fa0296348&boardBean.boardKey="+ i['onclick'].split("'view', ")[1].split(")")[0] +"&boardBean.boardMngKey=1&paramBean.key=23&paramBean.homepageKey=0&paramBean.mainGroupKey=1&paramBean.page=0&action=view&boardBean.passwd=&paramBean.searchType=subject&paramBean.searchWord="]

    q.put(json.dumps(url))

def get_bme_Announ(q): #생물산업기계공학
    url = {}
    http = urllib3.PoolManager()
    r = http.request('GET','http://bme.kongju.ac.kr/board.do?paramBean.key=39&paramBean.mainGroupKey=1&boardBean.boardMngKey=2')
    sc = r.data.decode('utf-8')
    cd = BeautifulSoup(sc, "html.parser")
    tb = cd.find("table", {"border": "0"}).find_all("span", {"style": "cursor:hand"})
    for i, cnt in zip(tb, range(len(tb))):
        url[cnt] = [i.text.strip(), "http://bme.kongju.ac.kr/board.do?org.apache.struts.taglib.html.TOKEN=9da872dcf4f59491bab4142c6137e762&boardBean.boardKey=" + i['onclick'].split("'view', ")[1].split(")")[0] + "&boardBean.boardMngKey=2&paramBean.key=39&paramBean.homepageKey=0&paramBean.mainGroupKey=1&paramBean.page=0&action=view&boardBean.passwd=&paramBean.searchType=subject&paramBean.searchWord="]
    q.put(json.dumps(url))


def get_forest_Announ(q): #산림자원학과
    url = {}
    http = urllib3.PoolManager()
    r = http.request('GET','http://forest.kongju.ac.kr/board.do?paramBean.key=24&paramBean.mainGroupKey=1&boardBean.boardMngKey=2')
    sc = r.data.decode('utf-8')
    cd = BeautifulSoup(sc, "html.parser")
    tb = cd.find("table", {"border": "0"}).find_all("span", {"style": "cursor:hand"})
    for i, cnt in zip(tb, range(len(tb))):
        url[cnt] = [i.text.strip(), "http://forest.kongju.ac.kr/board.do?org.apache.struts.taglib.html.TOKEN=bf37108ef93d8a434107f9310f7044e4&boardBean.boardKey=" + i['onclick'].split("'view', ")[1].split(")")[0] + "&boardBean.boardMngKey=2&paramBean.key=24&paramBean.homepageKey=0&paramBean.mainGroupKey=1&paramBean.page=0&action=view&boardBean.passwd=&paramBean.searchType=subject&paramBean.searchWord="]
    q.put(json.dumps(url))

def get_la_Announ(q): #조경학과
    url = {}
    http = urllib3.PoolManager()
    r = http.request('GET','http://la.kongju.ac.kr/board.do?paramBean.key=24&paramBean.mainGroupKey=1&boardBean.boardMngKey=1')
    sc = r.data.decode('utf-8')
    cd = BeautifulSoup(sc, "html.parser")
    tb = cd.find("table", {"border": "0"}).find_all("span", {"style": "cursor:hand"})
    for i, cnt in zip(tb, range(len(tb))):
        url[cnt] = [i.text.strip(), "http://la.kongju.ac.kr/board.do?org.apache.struts.taglib.html.TOKEN=45f014e76e9cf1412317a207e5f6e94b&boardBean.boardKey=" + i['onclick'].split("'view', ")[1].split(")")[0] + "&boardBean.boardMngKey=1&paramBean.key=24&paramBean.homepageKey=0&paramBean.mainGroupKey=1&paramBean.page=0&action=view&boardBean.passwd=&paramBean.searchType=subject&paramBean.searchWord="]
    q.put(json.dumps(url))

def get_fan_Announ(q): #식품영양학전공
    url = {}
    http = urllib3.PoolManager()
    r = http.request('GET','http://fan.kongju.ac.kr/board.do?paramBean.key=30&paramBean.mainGroupKey=1&boardBean.boardMngKey=1')
    sc = r.data.decode('utf-8')
    cd = BeautifulSoup(sc, "html.parser")
    tb = cd.find("table", {"border": "0"}).find_all("span", {"style": "cursor:hand"})
    for i, cnt in zip(tb, range(len(tb))):
        url[cnt] = [i.text.strip(), "http://fan.kongju.ac.kr/board.do?org.apache.struts.taglib.html.TOKEN=b8f0d0c0d12339ef2256f2926ad0cf80&boardBean.boardKey=" + i['onclick'].split("'view', ")[1].split(")")[0] + "&boardBean.boardMngKey=1&paramBean.key=30&paramBean.homepageKey=0&paramBean.mainGroupKey=1&paramBean.page=0&action=view&boardBean.passwd=&paramBean.searchType=subject&paramBean.searchWord="]
    q.put(json.dumps(url))


def get_food_Announ(q): #식품공학과
    url = {}
    http = urllib3.PoolManager()
    r = http.request('GET','http://food.kongju.ac.kr/board.do?paramBean.key=38&paramBean.mainGroupKey=1&boardBean.boardMngKey=1')
    sc = r.data.decode('utf-8')
    cd = BeautifulSoup(sc, "html.parser")
    tb = cd.find("table", {"border": "0"}).find_all("span", {"style": "cursor:hand"})
    for i, cnt in zip(tb, range(len(tb))):
        url[cnt] = [i.text.strip(), "http://food.kongju.ac.kr/board.do?org.apache.struts.taglib.html.TOKEN=fb909ac26255dbbbf2c20ea188305594&boardBean.boardKey=" + i['onclick'].split("'view', ")[1].split(")")[0] + "&boardBean.boardMngKey=1&paramBean.key=38&paramBean.homepageKey=0&paramBean.mainGroupKey=1&paramBean.page=0&action=view&boardBean.passwd=&paramBean.searchType=subject&paramBean.searchWord="]

    q.put(json.dumps(url))


def get_clas_Announ(q): #특수동물학과
    url = {}
    http = urllib3.PoolManager()
    r = http.request('GET','http://clas.kongju.ac.kr/board.do?paramBean.key=111&paramBean.mainGroupKey=1&boardBean.boardMngKey=2')
    sc = r.data.decode('utf-8')
    cd = BeautifulSoup(sc, "html.parser")
    tb = cd.find("table", {"border": "0"}).find_all("span", {"style": "cursor:hand"})
    for i, cnt in zip(tb, range(len(tb))):
        url[cnt] = [i.text.strip(), "http://clas.kongju.ac.kr/board.do?org.apache.struts.taglib.html.TOKEN=129efa47b84629e19bbdedeef8297c17&boardBean.boardKey=" + i['onclick'].split("'view', ")[1].split(")")[0] + "&boardBean.boardMngKey=2&paramBean.key=111&paramBean.homepageKey=0&paramBean.mainGroupKey=1&paramBean.page=0&action=view&boardBean.passwd=&paramBean.searchType=subject&paramBean.searchWord="]
    q.put(json.dumps(url))

def get_dhm_Announ(q): #보건행정학과
    url = {}
    http = urllib3.PoolManager()
    r = http.request('GET','http://www.dhm.or.kr/web/bbs/board.php?bo_table=m3_01')
    sc = r.data.decode('utf-8')
    cd = BeautifulSoup(sc, "html.parser")
    tb = cd.find("div", class_="tbl_head01 tbl_wrap").find_all("a", href=True)
    for i, cnt in zip(tb, range(len(tb))):
        if(i['href'].find("wr_id") > 0):
            url[cnt] = [i.text.strip(), i['href']]
    q.put(json.dumps(url))

def get_emt_Announ(q): # 응급구조학과
    url = {}
    http = urllib3.PoolManager()
    r = http.request('GET','http://emt.kongju.ac.kr:8080/board/sub01.jsp')
    sc = r.data.decode('utf-8')
    cd = BeautifulSoup(sc, "html.parser")
    tb = cd.find("table", class_="chart3").find_all("a", href=True)
    for i, cnt in zip(tb, range(len(tb))):
        url[cnt] = [i.text.strip(), "http://emt.kongju.ac.kr:8080/board" + i['href'].replace("./", "/")]
    q.put(json.dumps(url))

def get_dmrhim_Announ(q): #의료정보학과
    url = {}
    http = urllib3.PoolManager()
    r = http.request('GET','http://www.dmrhim.com/bbs/bbs.php?table=m0401')
    sc = r.data
    cd = BeautifulSoup(sc, "html.parser")
    tb = cd.find_all("a", attrs={'href': "#."})

    for i, cnt in zip(tb, range(len(tb))):
        on = i['onclick'].replace("'", "")
        url[cnt] = [i.text.strip(), "http://www.dmrhim.com/bbs/bbs.php?table=" + on.split(",")[3] +  "&query=view&uid=" + on.split(",")[0].split("e(")[1] + "&p=1"]
    q.put(json.dumps(url))

def get_fdesign_Announ(q): # 조형디자인학부
	url = {}
	http = urllib3.PoolManager()
	r = http.request('GET','http://f-design.kongju.ac.kr:8080/board/sub01.jsp')
	sc = r.data.decode("utf-8")
	cd = BeautifulSoup(sc, "html.parser")
	tb = cd.find_all("a", class_="listTxt")
	for i, cnt in zip(tb, range(len(tb))):
		url[cnt] = [i.text.replace(u'\xa0', u' ').strip(), "http://f-design.kongju.ac.kr:8080/board" + i['href'].replace("./", "/")]
	
	q.put(json.dumps(url))

def get_dance_Announ(q): #무용학과
    url = {}
    http = urllib3.PoolManager(
        cert_reqs='CERT_REQUIRED',
        ca_certs=certifi.where())
    r = http.request('GET', "https://dance.kongju.ac.kr/main/board/list.php?tblname=20120712095453")
    sc = r.data#.decode('utf-8')
    cd = BeautifulSoup(sc, "html.parser")
    tb = cd.find_all("a", class_="ajax", href=True)
    for i, cnt in zip(tb, range(len(tb))):
        if(i['href'].find("&id=") > 0 ):
            url[cnt] = [i.text.strip(), "https://dance.kongju.ac.kr/main/board/" + i['href']]
    q.put(json.dumps(url))

# 학식
def get_staff_si(q):
    try:
        http = urllib3.PoolManager()
        r = http.request('GET', 'http://www.kongju.ac.kr/service/food_view_w.jsp?code=C001&idx=1')
        sc =  r.data.decode('cp949', 'ignore')
        cd = BeautifulSoup(sc, "html.parser")
        today = cd.find("td", class_="toady")
        for br in today.find_all("br"):
            br.replace_with("\n")
        if(today.getText() == ""):
            today = "\n[중식]\n오늘은 운영하지 않습니다."
        else:
            today = "\n[중식]\n" + today.getText()
    except:
        today = "\n[중식]\n오늘은 운영하지 않습니다."

    q.put(today)

def get_staff_ch(q):
    try:
        http = urllib3.PoolManager()
        r = http.request('GET', 'http://www.kongju.ac.kr/service/food_view_w.jsp?code=C002&idx=1')
        sc =  r.data.decode('cp949', 'ignore')
        cd = BeautifulSoup(sc, "html.parser")
        today = cd.find("td", class_="toady")
        for br in today.find_all("br"):
            br.replace_with("\n")
        if(today.getText() == ""):
            today = "\n[중식]\n오늘은 운영하지 않습니다."
        else:
            today = "\n[중식]\n" + today.getText()
    except:
        today = "\n[중식]\n오늘은 운영하지 않습니다."

    q.put(today)

def get_staff_ye(q):
    try:
        http = urllib3.PoolManager()
        r = http.request('GET', 'http://www.kongju.ac.kr/service/food_view_w.jsp?code=C003&idx=1')
        sc = r.data.decode('cp949', 'ignore')
        cd = BeautifulSoup(sc, "html.parser")
        today = cd.find("td", class_="toady")
        for br in today.find_all("br"):
            br.replace_with("\n")

        if(today.getText() == ""):
            today = "\n[중식]\n오늘은 운영하지 않습니다."
        else:
            today = "\n[중식]\n" + today.getText()
    except:
        today = "\n[중식]\n오늘은 운영하지 않습니다."

    q.put(today)

def get_dreem(q):
    now = time.localtime()
    bobname = ["\n[조식]\n", "\n[중식]\n", "\n[석식]\n"]
    clear = []
    http = urllib3.PoolManager(
        cert_reqs='CERT_REQUIRED',
        ca_certs=certifi.where()
    )
    r = http.request('GET', 'https://dormi.kongju.ac.kr/main/contents/food.php?mid=40&k=2')
    """
    morning = cd.find('div', attrs={'id': 'breakfast'}).find("div")
    morning = morning.getText().replace("(", "").replace(" ", "").split(",")
    lunch = cd.find('div', attrs={'id': 'lunch'}).find("div")
    lunch = lunch.getText().replace("(", "").replace(" ", "").split(",")
    dinner = cd.find('div', attrs={'id': 'diner'}).find("div")
    dinner = dinner.getText().replace("(", "").replace(" ", "").split(",")
    bobs = [morning, lunch, dinner]
    for i in bobs:
        clear.append(i)
        ret = "[드림 하우스]\n"
        
    for i in range(3):
        ret += bobname[i]
        for b in clear[i]:
            ret += b + "\n"
    return ret
    """



@csrf_exempt
def friend_add(request):
    if(request.method == 'POST'):
        ids = json.loads((request.body).decode('utf-8'))
        db_add_friend(ids['user_key'])
    return JsonResponse(call_admin)



def keyboard(request):
	return JsonResponse(welcome)

def announToTitle(v):
	ret = []
	js = json.loads(v)
	for i in js:
		ret.append(js[i][0].strip())
	return ret

def announToURL(self, strs):
	now = strftime("%y.%m.%d", time.localtime())
	dic = db_get(self,now)
	js = json.loads(dic)
	for i in js:
		if(js[i][0].strip() == strs):
			return js[i][1]
	return "X"

def db_all_insert():
	now = strftime("%y.%m.%d", time.localtime())
	staff_ch_ck = db_check(staff_ch, now)
	staff_ye_ck = db_check(staff_ye, now)
	staff_si_ck = db_check(staff_si, now)
	Announ_kongju_ck = db_check(Announs_kongju, now)	
	Announ_sabum_ck = db_check(Announs_sabum, now)
	Announ_insa_ck = db_check(Announs_insa, now)
    #Announ_natural_ck = db_check(Announs_natural, now)
	Announ_brain_ck = db_check(Announs_brain,now)
	Announ_indu_ck = db_check(Announs_indu, now)	
	Announ_cnh_ck = db_check(Announs_cnh, now)
	Announ_art_ck = db_check(Announs_art, now)
	Announ_control_ck = db_check(Announs_control, now)
	Announ_cse_ck = db_check(Announs_cse, now)
	Announ_mech_ck = db_check(Announs_mech, now)
	Announ_civil_ck = db_check(Announs_civil, now)
	Announ_archi_ck = db_check(Announs_archi, now)
	Announ_archeng_ck = db_check(Announs_archeng, now)
	Announ_ame_ck = db_check(Announs_ame, now)
	Announ_ie_ck = db_check(Announs_ie, now)
	Announ_optical_ck = db_check(Announs_optical, now)
	Announ_earth_ck = db_check(Announs_earth, now)
	Announ_chinese_ck = db_check(Announs_chinese, now)
	Announ_eng_ck = db_check(Announs_eng, now)
	Announ_france_ck = db_check(Announs_france, now)
	Announ_german_ck = db_check(Announs_german, now)
	Announ_history_ck = db_check(Announs_history, now)
	Announ_geography_ck = db_check(Announs_geography, now)
	Announ_economics_ck = db_check(Announs_economics, now)
	Announ_intrade_ck = db_check(Announs_intrade, now)
	Announ_business_ck = db_check(Announs_business, now)
	Announ_tourism_ck = db_check(Announs_tourism, now)
	Announ_tourismenglish_ck = db_check(Announs_tourismenglish, now)
	Announ_public_ck = db_check(Announs_public, now)
	Announ_law_ck = db_check(Announs_law, now)
	Announ_socialwelfare_ck = db_check(Announs_socialwelfare, now)
	Announ_cm_ck = db_check(Announs_cm, now)
	Announ_pr_ck =db_check(Announs_pr, now)
	Announ_hort_ck = db_check(Announs_hort, now)
	Announ_ars_ck =db_check(Announs_ars, now)
	Announ_rce_ck =db_check(Announs_rce, now)
	Announ_bme_ck =db_check(Announs_bme, now)
	Announ_forest_ck =db_check(Announs_forest, now)
	Announ_la_ck =db_check(Announs_la, now)
	Announ_fan_ck =db_check(Announs_fan, now)
	Announ_food_ck =db_check(Announs_food, now)
	Announ_clas_ck =db_check(Announs_clas, now)
	Announ_dhm_ck = db_check(Announs_dhm, now)
	Announ_emt_ck = db_check(Announs_emt, now)
	Announ_dmrhim_ck = db_check(Announs_dmrhim,now)
	Announ_fdesign_ck = db_check(Announs_fdesign, now)
	Announ_dance_ck = db_check(Announs_dance, now)	
	global dreem_q 
	global staff_ch_q 
	global staff_ye_q 
	global staff_si_q 
	global Account_q 
	global Announs_kongju_q 
	global Announs_brain_q 
	global Announs_sabum_q 
	global Announs_insa_q 
	#global Announs_natural_q 
	global Announs_indu_q 
	global Announs_cnh_q 
	global Announs_art_q 
	global Announs_control_q 
	global Announs_cse_q 
	global Announs_mech_q 
	global Announs_civil_q 
	global Announs_archi_q 
	global Announs_archeng_q 
	global Announs_ame_q 
	global Announs_ie_q 
	global Announs_optical_q 
	global Announs_earth_q 
	global Announs_chinese_q 
	global Announs_eng_q 
	global Announs_france_q 
	global Announs_german_q 
	global Announs_history_q 
	global Announs_geography_q 
	global Announs_economics_q 
	global Announs_intrade_q 
	global Announs_business_q 
	global Announs_tourism_q 
	global Announs_tourismenglish_q 
	global Announs_public_q 
	global Announs_law_q 
	global Announs_socialwelfare_q 
	global Announs_cm_q 
	global Announs_pr_q 
	global Announs_hort_q 
	global Announs_ars_q 
	global Announs_rce_q 
	global Announs_bme_q 
	global Announs_forest_q 
	global Announs_la_q 
	global Announs_fan_q 
	global Announs_food_q 
	global Announs_clas_q 
	global Announs_dhm_q
	global Announs_emt_q
	global Announs_dmrhim_q 
	global Announs_fdesign_q
	global Announs_dance_q

	proc = []
	if (Announ_kongju_ck == "X"):
		proc.append(threading.Thread(target=db_insert, args=(Announs_kongju, Announs_kongju_q.get(), )))	
	if (Announ_sabum_ck == "X"):
		proc.append(threading.Thread(target=db_insert, args=(Announs_sabum,Announs_sabum_q.get(), )))
	if (Announ_insa_ck == "X"):
		proc.append(threading.Thread(target=db_insert, args=(Announs_insa,Announs_insa_q.get(), )))
	if (Announ_brain_ck == "X"):
		proc.append(threading.Thread(target=db_insert, args=(Announs_brain ,Announs_brain_q.get(), )))
	if (Announ_indu_ck == "X"):
		proc.append(threading.Thread(target=db_insert, args=(Announs_indu ,Announs_indu_q.get(), )))
	if (Announ_cnh_ck == "X"):	
		proc.append(threading.Thread(target=db_insert, args=(Announs_cnh ,Announs_cnh_q.get(), )))
	if (Announ_art_ck == "X"):
		proc.append(threading.Thread(target=db_insert, args=(Announs_art ,Announs_art_q.get(), )))
	if (Announ_control_ck == "X"):
		proc.append(threading.Thread(target=db_insert, args=(Announs_control ,Announs_control_q.get(), )))
	if (Announ_cse_ck == "X"):
		proc.append(threading.Thread(target=db_insert, args=(Announs_cse ,Announs_cse_q.get(), )))
	if (Announ_mech_ck == "X"):
		proc.append(threading.Thread(target=db_insert, args=(Announs_mech ,Announs_mech_q.get(), )))
	if (Announ_civil_ck == "X"):
		proc.append(threading.Thread(target=db_insert, args=(Announs_civil ,Announs_civil_q.get(), )))
	if (Announ_archi_ck == "X"):
		proc.append(threading.Thread(target=db_insert, args=(Announs_archi ,Announs_archi_q.get(), )))
	if (Announ_archeng_ck == "X"):
		proc.append(threading.Thread(target=db_insert, args=(Announs_archeng ,Announs_archeng_q.get(), )))
	if (Announ_ame_ck == "X"):
		proc.append(threading.Thread(target=db_insert, args=(Announs_ame ,Announs_ame_q.get(), )))
	if (Announ_ie_ck == "X"):
		proc.append(threading.Thread(target=db_insert, args=(Announs_ie ,Announs_ie_q.get(), )))
	if (Announ_optical_ck == "X"):
		proc.append(threading.Thread(target=db_insert, args=(Announs_optical ,Announs_optical_q.get(), )))
	if (Announ_earth_ck == "X"):
		proc.append(threading.Thread(target=db_insert, args=(Announs_earth ,Announs_earth_q.get(), )))
	if (Announ_chinese_ck == "X"):	
		proc.append(threading.Thread(target=db_insert, args=(Announs_chinese ,Announs_chinese_q.get(), )))
	if (Announ_eng_ck == "X"):
		proc.append(threading.Thread(target=db_insert, args=(Announs_eng ,Announs_eng_q.get(), )))
	if (Announ_france_ck == "X"):
		proc.append(threading.Thread(target=db_insert, args=(Announs_france ,Announs_france_q.get(), )))
	if (Announ_german_ck == "X"):
		proc.append(threading.Thread(target=db_insert, args=(Announs_german ,Announs_german_q.get(), )))
	if (Announ_history_ck == "X"):
		proc.append(threading.Thread(target=db_insert, args=(Announs_history ,Announs_history_q.get(), )))
	if (Announ_geography_ck == "X"):
		proc.append(threading.Thread(target=db_insert, args=(Announs_geography ,Announs_geography_q.get(), )))
	if (Announ_economics_ck == "X"):
		proc.append(threading.Thread(target=db_insert, args=(Announs_economics ,Announs_economics_q.get(), )))
	if (Announ_intrade_ck == "X"):
		proc.append(threading.Thread(target=db_insert, args=(Announs_intrade ,Announs_intrade_q.get(), )))
	if (Announ_business_ck == "X"):
		proc.append(threading.Thread(target=db_insert, args=(Announs_business ,Announs_business_q.get(), )))
	if (Announ_tourism_ck == "X"):
		proc.append(threading.Thread(target=db_insert, args=(Announs_tourism ,Announs_tourism_q.get(), )))
	if (Announ_tourismenglish_ck == "X"):
		proc.append(threading.Thread(target=db_insert, args=(Announs_tourismenglish ,Announs_tourismenglish_q.get(), )))
	if (Announ_public_ck == "X"):
		proc.append(threading.Thread(target=db_insert, args=(Announs_public ,Announs_public_q.get(), )))
	if (Announ_law_ck == "X"):
		proc.append(threading.Thread(target=db_insert, args=(Announs_law ,Announs_law_q.get(), )))
	if (Announ_socialwelfare_ck == "X"):
		proc.append(threading.Thread(target=db_insert, args=(Announs_socialwelfare ,Announs_socialwelfare_q.get(), )))
	if (Announ_cm_ck == "X"):
		proc.append(threading.Thread(target=db_insert, args=(Announs_cm ,Announs_cm_q.get(), )))
	if (Announ_pr_ck == "X"):
		proc.append(threading.Thread(target=db_insert, args=(Announs_pr ,Announs_pr_q.get(), )))
	if (Announ_hort_ck == "X"):
		proc.append(threading.Thread(target=db_insert, args=(Announs_hort ,Announs_hort_q.get(), )))
	if (Announ_ars_ck == "X"):
		proc.append(threading.Thread(target=db_insert, args=(Announs_ars ,Announs_ars_q.get(), )))
	if (Announ_rce_ck == "X"):
		proc.append(threading.Thread(target=db_insert, args=(Announs_rce ,Announs_rce_q.get(), )))
	if (Announ_bme_ck == "X"):
		proc.append(threading.Thread(target=db_insert, args=(Announs_bme ,Announs_bme_q.get(), )))
	if (Announ_forest_ck == "X"):
		proc.append(threading.Thread(target=db_insert, args=(Announs_forest ,Announs_forest_q.get(), )))
	if (Announ_la_ck == "X"):
		proc.append(threading.Thread(target=db_insert, args=(Announs_la ,Announs_la_q.get(), )))
	if (Announ_fan_ck == "X"):
		proc.append(threading.Thread(target=db_insert, args=(Announs_fan ,Announs_fan_q.get(), )))
	if (Announ_food_ck == "X"):
		proc.append(threading.Thread(target=db_insert, args=(Announs_food ,Announs_food_q.get(), )))
	if (Announ_clas_ck == "X"):
		proc.append(threading.Thread(target=db_insert, args=(Announs_clas ,Announs_clas_q.get(), )))
	if (Announ_dhm_ck == "X"):
		proc.append(threading.Thread(target=db_insert, args=(Announs_dhm ,Announs_dhm_q.get(), )))
	if (Announ_emt_ck == "X"):
		proc.append(threading.Thread(target=db_insert, args=(Announs_emt ,Announs_emt_q.get(), )))
	if (Announ_dmrhim_ck == "X"):
		proc.append(threading.Thread(target=db_insert, args=(Announs_dmrhim ,Announs_dmrhim_q.get(), )))
	if (Announ_fdesign_ck == "X"):
		proc.append(threading.Thread(target=db_insert, args=(Announs_fdesign ,Announs_fdesign_q.get(), )))
	if (Announ_dance_ck == "X"):
		proc.append(threading.Thread(target=db_insert, args=(Announs_dance ,Announs_dance_q.get(), )))
	if (staff_ye_ck == "X"):
		proc.append(threading.Thread(target=db_insert, args=(staff_ye ,staff_ye_q.get(), )))
	if (staff_ch_ck == "X"):
		proc.append(threading.Thread(target=db_insert, args=(staff_ch ,staff_ch_q.get(), )))
	if (staff_si_ck == "X"):
		proc.append(threading.Thread(target=db_insert, args=(staff_si ,staff_si_q.get(), )))

	for p in proc:
		p.daemon = False
		p.start()


def db_all_get():
	global dreem_q 
	global staff_ch_q 
	global staff_ye_q 
	global staff_si_q 
	global Account_q 
	global Announs_kongju_q 
	global Announs_brain_q 
	global Announs_sabum_q 
	global Announs_insa_q 
	#global Announs_natural_q 
	global Announs_indu_q 
	global Announs_cnh_q 
	global Announs_art_q 
	global Announs_control_q 
	global Announs_cse_q 
	global Announs_mech_q 
	global Announs_civil_q 
	global Announs_archi_q 
	global Announs_archeng_q 
	global Announs_ame_q 
	global Announs_ie_q 
	global Announs_optical_q 
	global Announs_earth_q 
	global Announs_chinese_q 
	global Announs_eng_q 
	global Announs_france_q 
	global Announs_german_q 
	global Announs_history_q 
	global Announs_geography_q 
	global Announs_economics_q 
	global Announs_intrade_q 
	global Announs_business_q 
	global Announs_tourism_q 
	global Announs_tourismenglish_q 
	global Announs_public_q 
	global Announs_law_q 
	global Announs_socialwelfare_q 
	global Announs_cm_q 
	global Announs_pr_q 
	global Announs_hort_q 
	global Announs_ars_q 
	global Announs_rce_q 
	global Announs_bme_q 
	global Announs_forest_q 
	global Announs_la_q 
	global Announs_fan_q 
	global Announs_food_q 
	global Announs_clas_q 
	global Announs_dhm_q
	global Announs_emt_q
	global Announs_dmrhim_q 
	global Announs_fdesign_q
	global Announs_dance_q

	proc = []
	
	now = strftime("%y.%m.%d", time.localtime())
	staff_ch_ck = db_check(staff_ch, now)
	staff_ye_ck = db_check(staff_ye, now)
	staff_si_ck = db_check(staff_si, now)
	Announ_kongju_ck = db_check(Announs_kongju, now)	
	Announ_sabum_ck = db_check(Announs_sabum, now)
	Announ_insa_ck = db_check(Announs_insa, now)
    #Announ_natural_ck = db_check(Announs_natural, now)
	Announ_brain_ck = db_check(Announs_brain,now)
	Announ_indu_ck = db_check(Announs_indu, now)	
	Announ_cnh_ck = db_check(Announs_cnh, now)
	Announ_art_ck = db_check(Announs_art, now)
	Announ_control_ck = db_check(Announs_control, now)
	Announ_cse_ck = db_check(Announs_cse, now)
	Announ_mech_ck = db_check(Announs_mech, now)
	Announ_civil_ck = db_check(Announs_civil, now)
	Announ_archi_ck = db_check(Announs_archi, now)
	Announ_archeng_ck = db_check(Announs_archeng, now)
	Announ_ame_ck = db_check(Announs_ame, now)
	Announ_ie_ck = db_check(Announs_ie, now)
	Announ_optical_ck = db_check(Announs_optical, now)
	Announ_earth_ck = db_check(Announs_earth, now)
	Announ_chinese_ck = db_check(Announs_chinese, now)
	Announ_eng_ck = db_check(Announs_eng, now)
	Announ_france_ck = db_check(Announs_france, now)
	Announ_german_ck = db_check(Announs_german, now)
	Announ_history_ck = db_check(Announs_history, now)
	Announ_geography_ck = db_check(Announs_geography, now)
	Announ_economics_ck = db_check(Announs_economics, now)
	Announ_intrade_ck = db_check(Announs_intrade, now)
	Announ_business_ck = db_check(Announs_business, now)
	Announ_tourism_ck = db_check(Announs_tourism, now)
	Announ_tourismenglish_ck = db_check(Announs_tourismenglish, now)
	Announ_public_ck = db_check(Announs_public, now)
	Announ_law_ck = db_check(Announs_law, now)
	Announ_socialwelfare_ck = db_check(Announs_socialwelfare, now)
	Announ_cm_ck = db_check(Announs_cm, now)
	Announ_pr_ck =db_check(Announs_pr, now)
	Announ_hort_ck = db_check(Announs_hort, now)
	Announ_ars_ck =db_check(Announs_ars, now)
	Announ_rce_ck =db_check(Announs_rce, now)
	Announ_bme_ck =db_check(Announs_bme, now)
	Announ_forest_ck =db_check(Announs_forest, now)
	Announ_la_ck =db_check(Announs_la, now)
	Announ_fan_ck =db_check(Announs_fan, now)
	Announ_food_ck =db_check(Announs_food, now)
	Announ_clas_ck =db_check(Announs_clas, now)
	Announ_dhm_ck = db_check(Announs_dhm, now)
	Announ_emt_ck = db_check(Announs_emt, now)
	Announ_dmrhim_ck = db_check(Announs_dmrhim,now)
	Announ_fdesign_ck = db_check(Announs_fdesign, now)
	Announ_dance_ck = db_check(Announs_dance, now)	

	proc = []
	if (Announ_kongju_ck == "X"):
		proc.append(threading.Thread(target=get_kongju_Announ, args=(Announs_kongju_q, )))
	if (Announ_sabum_ck == "X"):
		proc.append(threading.Thread(target=get_sabum_Announ, args=(Announs_sabum_q, )))
	if (Announ_insa_ck == "X"):
		proc.append(threading.Thread(target=get_insa_Announ, args=(Announs_insa_q, )))
	if (Announ_brain_ck == "X"):
		proc.append(threading.Thread(target=get_brain_Announ, args=(Announs_brain_q, )))
	if (Announ_indu_ck == "X"):
		proc.append(threading.Thread(target=get_indu_Announ, args=(Announs_indu_q, )))
	if (Announ_cnh_ck == "X"):	
		proc.append(threading.Thread(target=get_cnh_Announ, args=(Announs_cnh_q, )))
	if (Announ_art_ck == "X"):
		proc.append(threading.Thread(target=get_art_Announ, args=(Announs_art_q, )))
	if (Announ_control_ck == "X"):
		proc.append(threading.Thread(target=get_control_Announ, args=(Announs_control_q, )))
	if (Announ_cse_ck == "X"):
		proc.append(threading.Thread(target=get_cse_Announ, args=(Announs_cse_q, )))
	if (Announ_mech_ck == "X"):
		proc.append(threading.Thread(target=get_mech_Announ, args=(Announs_mech_q, )))
	if (Announ_civil_ck == "X"):
		proc.append(threading.Thread(target=get_civil_Announ, args=(Announs_civil_q, )))
	if (Announ_archi_ck == "X"):
		proc.append(threading.Thread(target=get_archi_Announ, args=(Announs_archi_q, )))
	if (Announ_archeng_ck == "X"):
		proc.append(threading.Thread(target=get_archeng_Announ, args=(Announs_archeng_q, )))
	if (Announ_ame_ck == "X"):
		proc.append(threading.Thread(target=get_ame_Announ, args=(Announs_ame_q, )))
	if (Announ_ie_ck == "X"):
		proc.append(threading.Thread(target=get_ie_Announ, args=(Announs_ie_q, )))
	if (Announ_optical_ck == "X"):
		proc.append(threading.Thread(target=get_optical_Announ, args=(Announs_optical_q, )))
	if (Announ_earth_ck == "X"):
		proc.append(threading.Thread(target=get_earth_Announ, args=(Announs_earth_q, )))
	if (Announ_chinese_ck == "X"):	
		proc.append(threading.Thread(target=get_chinese_Announ, args=(Announs_chinese_q, )))
	if (Announ_eng_ck == "X"):
		proc.append(threading.Thread(target=get_eng_Announ, args=(Announs_eng_q, )))
	if (Announ_france_ck == "X"):
		proc.append(threading.Thread(target=get_france_Announ, args=(Announs_france_q, )))
	if (Announ_german_ck == "X"):
		proc.append(threading.Thread(target=get_german_Announ, args=(Announs_german_q, )))
	if (Announ_history_ck == "X"):
		proc.append(threading.Thread(target=get_history_Announ, args=(Announs_history_q, )))
	if (Announ_geography_ck == "X"):
		proc.append(threading.Thread(target=get_geography_Announ, args=(Announs_geography_q, )))
	if (Announ_economics_ck == "X"):
		proc.append(threading.Thread(target=get_economics_Announ, args=(Announs_economics_q, )))
	if (Announ_intrade_ck == "X"):
		proc.append(threading.Thread(target=get_intrade_Announ, args=(Announs_intrade_q, )))
	if (Announ_business_ck == "X"):
		proc.append(threading.Thread(target=get_business_Announ, args=(Announs_business_q, )))
	if (Announ_tourism_ck == "X"):
		proc.append(threading.Thread(target=get_tourism_Announ, args=(Announs_tourism_q, )))
	if (Announ_tourismenglish_ck == "X"):
		proc.append(threading.Thread(target=get_tourismenglish_Announ, args=(Announs_tourismenglish_q, )))
	if (Announ_public_ck == "X"):
		proc.append(threading.Thread(target=get_public_Announ, args=(Announs_public_q, )))
	if (Announ_law_ck == "X"):
		proc.append(threading.Thread(target=get_law_Announ, args=(Announs_law_q, )))
	if (Announ_socialwelfare_ck == "X"):
		proc.append(threading.Thread(target=get_socialwelfare_Announ, args=(Announs_socialwelfare_q, )))
	if (Announ_cm_ck == "X"):
		proc.append(threading.Thread(target=get_cm_Announ, args=(Announs_cm_q, )))
	if (Announ_pr_ck == "X"):
		proc.append(threading.Thread(target=get_pr_Announ, args=(Announs_pr_q, )))
	if (Announ_hort_ck == "X"):
		proc.append(threading.Thread(target=get_hort_Announ, args=(Announs_hort_q, )))
	if (Announ_ars_ck == "X"):
		proc.append(threading.Thread(target=get_ars_Announ, args=(Announs_ars_q, )))
	if (Announ_rce_ck == "X"):
		proc.append(threading.Thread(target=get_rce_Announ, args=(Announs_rce_q, )))
	if (Announ_bme_ck == "X"):
		proc.append(threading.Thread(target=get_bme_Announ, args=(Announs_bme_q, )))
	if (Announ_forest_ck == "X"):
		proc.append(threading.Thread(target=get_forest_Announ, args=(Announs_forest_q, )))
	if (Announ_la_ck == "X"):
		proc.append(threading.Thread(target=get_la_Announ, args=(Announs_la_q, )))
	if (Announ_fan_ck == "X"):
		proc.append(threading.Thread(target=get_fan_Announ, args=(Announs_fan_q, )))
	if (Announ_food_ck == "X"):
		proc.append(threading.Thread(target=get_food_Announ, args=(Announs_food_q, )))
	if (Announ_clas_ck == "X"):
		proc.append(threading.Thread(target=get_clas_Announ, args=(Announs_clas_q, )))
	if (Announ_dhm_ck == "X"):
		proc.append(threading.Thread(target=get_dhm_Announ, args=(Announs_dhm_q, )))
	if (Announ_emt_ck == "X"):
		proc.append(threading.Thread(target=get_emt_Announ, args=(Announs_emt_q, )))
	if (Announ_dmrhim_ck == "X"):
		proc.append(threading.Thread(target=get_dmrhim_Announ, args=(Announs_dmrhim_q, )))
	if (Announ_fdesign_ck == "X"):
		proc.append(threading.Thread(target=get_fdesign_Announ, args=(Announs_fdesign_q, )))
	if (Announ_dance_ck == "X"):
		proc.append(threading.Thread(target=get_dance_Announ, args=(Announs_dance_q, )))
	if (staff_ye_ck == "X"):
		proc.append(threading.Thread(target=get_staff_ye, args=(staff_ye_q, )))
	if (staff_ch_ck == "X"):
		proc.append(threading.Thread(target=get_staff_ch, args=(staff_ch_q, )))
	if (staff_si_ck == "X"):
		proc.append(threading.Thread(target=get_staff_si, args=(staff_si_q, )))

	for p in proc:
		p.daemon = False
		p.start()


@csrf_exempt 
def message(request):   
	db_all_get()
	db_all_insert()
	announ_kongju_view = {'message': {'text': '[학생소식]\n\n학생소식을 선택하셨습니다.\n학생소식에 올라온 공지사항을 보여드리겠습니다.'},'keyboard': {'type': 'buttons', 'buttons':[]}}
	announ_brain_view = {'message': {'text': '[공과대학]\n\n공과대학을 선택하셨습니다.\n공과대학에 올라온 공지사항을 보여드리겠습니다.'},'keyboard': {'type': 'buttons',     'buttons':[]}}
	announ_sabum_view = {'message': {'text': '[사범대학]\n\n사범대학을 선택하셨습니다.\n사범대학에 올라온 공지사항을 보여드리겠습니다.'},'keyboard': {'type': 'buttons',     'buttons':[]}}
	announ_insa_view = {'message': {'text': '[인문사회과학대학]\n\n인문사회과학대학을 선택하셨습니다.\n인문사회과학대학에 올라온 공지사항을 보여드리겠습니다.'},'keyboard': {'type': 'buttons',     'buttons':[]}}
	announ_natural_view = {'message': {'text': '[자연과학대학]\n\n자연과학대학을 선택하셨습니다.\n자연과학대학에 올라온 공지사항을 보여드리겠습니다.'},'keyboard': {'type': 'buttons',     'buttons':[]}}
	announ_indu_view = {'message': {'text': '[산업과학대학]\n\n산업과학대학을 선택하셨습니다.\n산업과학대학에 올라온 공지사항을 보여드리겠습니다.'},'keyboard': {'type': 'buttons',     'buttons':[]}}
	announ_cnh_view = {'message': {'text': '[간호보건대학]\n\n간호보건대학을 선택하셨습니다.\n간호보건대학에 올라온 공지사항을 보여드리겠습니다.'},'keyboard': {'type': 'buttons',     'buttons':[]}}
	announ_art_view = {'message': {'text': '[예술대학]\n\n예술대학을 선택하셨습니다.\n예술대학에 올라온 공지사항을 보여드리겠습니다.'},'keyboard': {'type': 'buttons',     'buttons':[]}}
	announ_control_view = {'message': {'text': '[제어계측공학전공]\n\n을 선택하셨습니다.\n제어계측공학전공에 올라온 공지사항을 보여드리겠습니다.'},'keyboard': {'type': 'buttons',         'buttons':[]}}
	announ_cse_view = {'message': {'text': '[컴퓨터공학부]\n\n을 선택하셨습니다.\n컴퓨터공학부에 올라온 공지사항을 보여드리겠습니다.'},'keyboard': {'type': 'buttons',         'buttons':[]}}
	announ_mech_view = {'message': {'text': '[기계자동차공학부]\n\n을 선택하셨습니다.\기계자동차공학부n에 올라온 공지사항을 보여드리겠습니다.'},'keyboard': {'type': 'buttons',         'buttons':[]}}
	announ_civil_view = {'message': {'text': '[건설환경공학부]\n\n을 선택하셨습니다.\n건설환경공학부에 올라온 공지사항을 보여드리겠습니다.'},'keyboard': {'type': 'buttons',         'buttons':[]}}
	announ_archi_view = {'message': {'text': '[건축학부]\n\n을 선택하셨습니다.\n건축학부에 올라온 공지사항을 보여드리겠습니다.'},'keyboard': {'type': 'buttons',         'buttons':[]}}
	announ_archeng_view = {'message': {'text': '[건축공학부]\n\n을 선택하셨습니다.\n건축공학부에 올라온 공지사항을 보여드리겠습니다.'},'keyboard': {'type': 'buttons',         'buttons':[]}}
	announ_ame_view = {'message': {'text': '[신소재공학부]\n\n을 선택하셨습니다.\n신소재공학부에 올라온 공지사항을 보여드리겠습니다.'},'keyboard': {'type': 'buttons',         'buttons':[]}}
	announ_ie_view = {'message': {'text': '[산업시스템공학과]\n\n을 선택하셨습니다.\n산업시스템공학과에 올라온 공지사항을 보여드리겠습니다.'},'keyboard': {'type': 'buttons',         'buttons':[]}}
	announ_optical_view = {'message': {'text': '[광공학과]\n\n을 선택하셨습니다.\n광공학과에 올라온 공지사항을 보여드리겠습니다.'},'keyboard': {'type': 'buttons',         'buttons':[]}}

	announ_earth_view = {'message': {'text': '[지구과학교육과]\n\n을 선택하셨습니다.\n지구과학교육과에 올라온 공지사항을 보여드리겠습니다.'},'keyboard': {'type': 'buttons',              'buttons':[]}}



	announ_chinese_view = {'message': {'text': '[중어중문학과]\n\n을 선택하셨습니다.\n중어중문학과에 올라온 공지사항을 보여드리겠습니다.'},'keyboard': {'type': 'buttons',              'buttons':[]}}
	announ_eng_view = {'message': {'text': '[영어영문학과]\n\n을 선택하셨습니다.\n영어영문학과에 올라온 공지사항을 보여드리겠습니다.'},'keyboard': {'type': 'buttons',              'buttons':[]}}
	announ_france_view = {'message': {'text': '[불어불문학과]\n\n을 선택하셨습니다.\n불어불문학과에 올라온 공지사항을 보여드리겠습니다.'},'keyboard': {'type': 'buttons',              'buttons':[]}}
	announ_german_view = {'message': {'text': '[독어독문학과]\n\n을 선택하셨습니다.\n독어독문학과에 올라온 공지사항을 보여드리겠습니다.'},'keyboard': {'type': 'buttons',              'buttons':[]}}
	announ_history_view = {'message': {'text': '[사학과]\n\n을 선택하셨습니다.\n사학과에 올라온 공지사항을 보여드리겠습니다.'},'keyboard': {'type': 'buttons',              'buttons':[]}}
	announ_geography_view = {'message': {'text': '[지리학과]\n\n을 선택하셨습니다.\n지리학과에 올라온 공지사항을 보여드리겠습니다.'},'keyboard': {'type': 'buttons',              'buttons':[]}}
	announ_economics_view = {'message': {'text': '[경제학전공]\n\n을 선택하셨습니다.\n경제학전공에 올라온 공지사항을 보여드리겠습니다.'},'keyboard': {'type': 'buttons',              'buttons':[]}}
	announ_intrade_view = {'message': {'text': '[국제통상학전공]\n\n을 선택하셨습니다.\n국제통상학전공에 올라온 공지사항을 보여드리겠습니다.'},'keyboard': {'type': 'buttons',              'buttons':[]}}
	announ_business_view = {'message': {'text': '[경영학과]\n\n을 선택하셨습니다.\n경영학과에 올라온 공지사항을 보여드리겠습니다.'},'keyboard': {'type': 'buttons',              'buttons':[]}}
	announ_tourism_view = {'message': {'text': '[관광경영학전공]\n\n을 선택하셨습니다.\n관광경영학전공에 올라온 공지사항을 보여드리겠습니다.'},'keyboard': {'type': 'buttons',              'buttons':[]}}
	announ_tourismenglish_view = {'message': {'text': '[관광영어통역학전공]\n\n을 선택하셨습니다.\n관광영어통역학전공에 올라온 공지사항을 보여드리겠습니다.'},'keyboard': {'type': 'buttons',              'buttons':[]}}
	announ_public_view = {'message': {'text': '[행정학과]\n\n을 선택하셨습니다.\n행정학과에 올라온 공지사항을 보여드리겠습니다.'},'keyboard': {'type': 'buttons',              'buttons':[]}}
	announ_law_view = {'message': {'text': '[법학과]\n\n을 선택하셨습니다.\n법학과에 올라온 공지사항을 보여드리겠습니다.'},'keyboard': {'type': 'buttons',              'buttons':[]}}
	announ_socialwelfare_view = {'message': {'text': '[사회복지학과]\n\n을 선택하셨습니다.\n사회복지학과에 올라온 공지사항을 보여드리겠습니다.'},'keyboard': {'type': 'buttons',              'buttons':[]}}




	announ_cm_view = {'message': {'text': '[산업유통학과]\n\n산업유통학과을 선택하셨습니다.\n에 올라온 공지사항을 보여드리겠습니다.'},'keyboard': {'type': 'buttons',              'buttons':[]}}
	announ_pr_view = {'message': {'text': '[식물자원학과]\n\n식물자원학과을 선택하셨습니다.\n에 올라온 공지사항을 보여드리겠습니다.'},'keyboard': {'type': 'buttons',              'buttons':[]}}
	announ_hort_view = {'message': {'text': '[원예학과]\n\n원예학과을 선택하셨습니다.\n에 올라온 공지사항을 보여드리겠습니다.'},'keyboard': {'type': 'buttons',              'buttons':[]}}
	announ_ars_view = {'message': {'text': '[동물자원학과]\n\n동물자원학과을 선택하셨습니다.\n에 올라온 공지사항을 보여드리겠습니다.'},'keyboard': {'type': 'buttons',              'buttons':[]}}
	announ_rce_view = {'message': {'text': '[지역건설공학전공]\n\n지역건설공학전공을 선택하셨습니다.\n에 올라온 공지사항을 보여드리겠습니다.'},'keyboard': {'type': 'buttons',              'buttons':[]}}
	announ_bme_view = {'message': {'text': '[생물산업기계공학]\n\n생물산업기계공학을 선택하셨습니다.\n에 올라온 공지사항을 보여드리겠습니다.'},'keyboard': {'type': 'buttons',              'buttons':[]}}
	announ_forest_view = {'message': {'text': '[산림자원학과]\n\n산림자원학과을 선택하셨습니다.\n에 올라온 공지사항을 보여드리겠습니다.'},'keyboard': {'type': 'buttons',              'buttons':[]}}
	announ_la_view = {'message': {'text': '[조경학과]\n\n조경학과을 선택하셨습니다.\n에 올라온 공지사항을 보여드리겠습니다.'},'keyboard': {'type': 'buttons',              'buttons':[]}}
	announ_fan_view = {'message': {'text': '[식품영양학전공]\n\n식품영양학전공을 선택하셨습니다.\n에 올라온 공지사항을 보여드리겠습니다.'},'keyboard': {'type': 'buttons',              'buttons':[]}}
	announ_food_view = {'message': {'text': '[식품공학과]\n\n식품공학과을 선택하셨습니다.\n에 올라온 공지사항을 보여드리겠습니다.'},'keyboard': {'type': 'buttons',              'buttons':[]}}
	announ_clas_view = {'message': {'text': '[특수동물학과]\n\n특수동물학과을 선택하셨습니다.\n에 올라온 공지사항을 보여드리겠습니다.'},'keyboard': {'type': 'buttons',              'buttons':[]}}

	
	announ_dhm_view = {'message': {'text': '[보건행정학과]\n\n보건행정학과을 선택하셨습니다.\n에 올라온 공지사항을 보여드리겠습니다.'},'keyboard': {'type': 'buttons',              'buttons':[]}}
	announ_emt_view = {'message': {'text': '[응급구조학과]\n\n응급구조학과을 선택하셨습니다.\n에 올라온 공지사항을 보여드리겠습니다.'},'keyboard': {'type': 'buttons',              'buttons':[]}}
	announ_dmrhim_view = {'message': {'text': '[의료정보학과]\n\n의료정보학과을 선택하셨습니다.\n에 올라온 공지사항을 보여드리겠습니다.'},'keyboard': {'type': 'buttons',              'buttons':[]}}
	announ_fdesign_view = {'message': {'text': '[조형디자인학부]\n\n조형디자인학부을 선택하셨습니다.\n에 올라온 공지사항을 보여드리겠습니다.'},'keyboard': {'type': 'buttons',              'buttons':[]}}
	announ_dance_view = {'message': {'text': '[무용학과]\n\n무용학과을 선택하셨습니다.\n에 올라온 공지사항을 보여드리겠습니다.'},'keyboard': {'type': 'buttons',              'buttons':[]}}


	bus_val = {"message": {"text": "[버스시간]\n\n조회하신 버스 시간입니다\n\n","photo": {"url": "https://photo.src","width": 640,"height": 480},"message_button": {"label": "개발자 후원하기","url": "http://hubeen.kr/donate"}},"keyboard": {"type": "buttons","buttons": ["뒤로가기"]}}

	knucoin_de = {'message': {'text': '[KNUCOIN]\n\n현재 소지하고 있는 갯수는 아래와 같습니다.\n\nKNUCOIN : '},'keyboard': {'type': 'buttons', 'buttons':['메인', '뒤로가기']}}
	knucoin_gi = {'message': {'text': '[KNUCOIN]\n\n코인은 하루에 0.1knc를 지급합니다.\n\n개발자 도와주기 : hubeen.kr/donate의 광고를 눌러주세요!\n\n'},'keyboard': {'type': 'buttons', 'buttons':['메인','뒤로가기']}}
	bob = {'message': {'text': ""}, 'keyboard': {'type': 'buttons', 'buttons': ["메인", "뒤로가기"]}}
	now = strftime("%y.%m.%d", time.localtime())
	message = ((request.body).decode('utf-8'))
	ret_json = json.loads(message)
	strs = ret_json['content']	
	ids = ret_json['user_key']
	types = ret_json['type']

	if(strs == "친구추가"):
		if(db_not_friend(ids) == "X"):
			return JsonResponse(notfriend)	
		else:
			db_update_idx(ids, 0)
			return JsonResponse(main)

	if (strs == "!도움!"):
		db_update_idx(ids, 1)	
		return JsonResponse(helps)

#뒤로가기
	if (strs == "뒤로가기"):
		if(db_not_friend(ids) != "X"):
			if(db_get_idx(ids) == 1):
				db_update_idx(ids, 0)
				return JsonResponse(main)
			if(db_get_idx(ids) == 2):
				db_update_idx(ids, 0)
				return JsonResponse(main)
			if(db_get_idx(ids) == 3):
				db_update_idx(ids, 2)
				return JsonResponse(service_list)
			if(db_get_idx(ids) == 4):
				db_update_idx(ids, 3)
				return JsonResponse(haksik)
			if(db_get_idx(ids) == 5):
				db_update_idx(ids, 4)
				return JsonResponse(cheonan)
			if(db_get_idx(ids) == 6):
				db_update_idx(ids, 4)
				return JsonResponse(cheonan)
			if(db_get_idx(ids) == 7):
				db_update_idx(ids, 4)
				return JsonResponse(cheonan)
			if(db_get_idx(ids) == 8):
				db_update_idx(ids, 3)
				return JsonResponse(haksik)
			if(db_get_idx(ids) == 9):
				db_update_idx(ids, 8)
				return JsonResponse(singwan)
			if(db_get_idx(ids) == 10):
				db_update_idx(ids, 8)
				return JsonResponse(singwan)
			if(db_get_idx(ids) == 11):
				db_update_idx(ids, 8)
				return JsonResponse(singwan)
			if(db_get_idx(ids) == 12):
				db_update_idx(ids, 11)
				return JsonResponse(singwan_dormi)
			if(db_get_idx(ids) == 13):
				db_update_idx(ids, 11)
				return JsonResponse(singwan_dormi)
			if(db_get_idx(ids) == 14):
				db_update_idx(ids, 3)
				return JsonResponse(haksik)
			if(db_get_idx(ids) == 15):
				db_update_idx(ids, 14)
				return JsonResponse(yesan)
			if(db_get_idx(ids) == 16):
				db_update_idx(ids, 14)
				return JsonResponse(yesan)
			if(db_get_idx(ids) == 17):
				db_update_idx(ids, 2)
				return JsonResponse(service_list)
			if(db_get_idx(ids) == 18):
				db_update_idx(ids, 17)
				return JsonResponse(notics)
			if(db_get_idx(ids) == 19):
				db_update_idx(ids, 17)
				return JsonResponse(notics)
			if(db_get_idx(ids) == 20):
				db_update_idx(ids, 19)
				return JsonResponse(notics_brain)
			if(db_get_idx(ids) == 21):
				db_update_idx(ids, 19)
				return JsonResponse(notics_brain)
			if(db_get_idx(ids) == 22):
				db_update_idx(ids, 19)
				return JsonResponse(notics_brain)
			if(db_get_idx(ids) == 23):
				db_update_idx(ids, 19)
				return JsonResponse(notics_brain)
			if(db_get_idx(ids) == 24):
				db_update_idx(ids, 19)
				return JsonResponse(notics_brain)
			if(db_get_idx(ids) == 25):
				db_update_idx(ids, 19)
				return JsonResponse(notics_brain)
			if(db_get_idx(ids) == 26):
				db_update_idx(ids, 19)
				return JsonResponse(notics_brain)
			if(db_get_idx(ids) == 27):
				db_update_idx(ids, 19)
				return JsonResponse(notics_brain)
			if(db_get_idx(ids) == 28):
				db_update_idx(ids, 19)
				return JsonResponse(notics_brain)
			if(db_get_idx(ids) == 29):
				db_update_idx(ids, 19)
				return JsonResponse(notics_brain)
			if(db_get_idx(ids) == 30):
				db_update_idx(ids, 19)
				return JsonResponse(notics)
			if(db_get_idx(ids) == 31):
				db_update_idx(ids, 30)
				return JsonResponse(notics_sabum)	
			if(db_get_idx(ids) == 32):
				db_update_idx(ids, 30)
				return JsonResponse(notics_sabum)
			if(db_get_idx(ids) == 33):
				db_update_idx(ids, 17)
				return JsonResponse(notics)
			if(db_get_idx(ids) == 34):
				db_update_idx(ids, 33)
				return JsonResponse(notics_insa)
			if(db_get_idx(ids) == 35):
				db_update_idx(ids, 33)
				return JsonResponse(notics_insa)
			if(db_get_idx(ids) == 36):
				db_update_idx(ids, 33)
				return JsonResponse(notics_insa)
			if(db_get_idx(ids) == 37):
				db_update_idx(ids, 33)
				return JsonResponse(notics_insa)
			if(db_get_idx(ids) == 38):
				db_update_idx(ids, 33)
				return JsonResponse(notics_insa)
			if(db_get_idx(ids) == 39):
				db_update_idx(ids, 33)
				return JsonResponse(notics_insa)
			if(db_get_idx(ids) == 40):
				db_update_idx(ids, 33)
				return JsonResponse(notics_insa)
			if(db_get_idx(ids) == 41):
				db_update_idx(ids, 33)
				return JsonResponse(notics_insa)
			if(db_get_idx(ids) == 42):
				db_update_idx(ids, 33)
				return JsonResponse(notics_insa)
			if(db_get_idx(ids) == 43):
				db_update_idx(ids, 33)
				return JsonResponse(notics_insa)
			if(db_get_idx(ids) == 44):
				db_update_idx(ids, 33)
				return JsonResponse(notics_insa)
			if(db_get_idx(ids) == 45):
				db_update_idx(ids, 33)
				return JsonResponse(notics_insa)
			if(db_get_idx(ids) == 46):
				db_update_idx(ids, 33)
				return JsonResponse(notics_insa)
			if(db_get_idx(ids) == 47):
				db_update_idx(ids, 33)
				return JsonResponse(notics_insa)
			if(db_get_idx(ids) == 48):
				db_update_idx(ids, 33)
				return JsonResponse(notics_insa)
			if(db_get_idx(ids) == 49):
				db_update_idx(ids, 33)
				return JsonResponse(notics_insa)
			if(db_get_idx(ids) == 50):
				db_update_idx(ids, 17)
				return JsonResponse(notics)
			if(db_get_idx(ids) == 51):
				db_update_idx(ids, 50)
				return JsonResponse(notics_indu)
			if(db_get_idx(ids) == 52):
				db_update_idx(ids, 50)
				return JsonResponse(notics_indu)
			if(db_get_idx(ids) == 53):
				db_update_idx(ids, 50)
				return JsonResponse(notics_indu)
			if(db_get_idx(ids) == 54):
				db_update_idx(ids, 50)
				return JsonResponse(notics_indu)
			if(db_get_idx(ids) == 55):
				db_update_idx(ids, 50)
				return JsonResponse(notics_indu)
			if(db_get_idx(ids) == 56):
				db_update_idx(ids, 50)
				return JsonResponse(notics_indu)
			if(db_get_idx(ids) == 57):
				db_update_idx(ids, 50)
				return JsonResponse(notics_indu)
			if(db_get_idx(ids) == 58):
				db_update_idx(ids, 50)
				return JsonResponse(notics_indu)
			if(db_get_idx(ids) == 59):
				db_update_idx(ids, 50)
				return JsonResponse(notics_indu)
			if(db_get_idx(ids) == 60):
				db_update_idx(ids, 50)
				return JsonResponse(notics_indu)
			if(db_get_idx(ids) == 61):
				db_update_idx(ids, 50)
				return JsonResponse(notics_indu)
			if(db_get_idx(ids) == 62):
				db_update_idx(ids, 50)
				return JsonResponse(notics_indu)
			if(db_get_idx(ids) == 63):
				db_update_idx(ids, 17)
				return JsonResponse(notics)
			if(db_get_idx(ids) == 64):
				db_update_idx(ids, 63)
				return JsonResponse(notics_cnh)
			if(db_get_idx(ids) == 65):
				db_update_idx(ids, 63)
				return JsonResponse(notics_cnh)
			if(db_get_idx(ids) == 66):
				db_update_idx(ids, 63)
				return JsonResponse(notics_cnh)
			if(db_get_idx(ids) == 67):
				db_update_idx(ids, 63)
				return JsonResponse(notics_cnh)
			if(db_get_idx(ids) == 68):
				db_update_idx(ids, 17)
				return JsonResponse(notics)
			if(db_get_idx(ids) == 69):
				db_update_idx(ids, 68)
				return JsonResponse(notics_art)
			if(db_get_idx(ids) == 70):
				db_update_idx(ids, 68)
				return JsonResponse(notics_art)
			if(db_get_idx(ids) == 71):
				db_update_idx(ids, 68)
				return JsonResponse(notics_art)	
			if(db_get_idx(ids) == 72):
				db_update_idx(ids, 2)
				return JsonResponse(service_list)
			if(db_get_idx(ids) == 73):
				db_update_idx(ids, 72)
				return JsonResponse(bus_noc)
			if(db_get_idx(ids) == 74):
				db_update_idx(ids, 73)
				return JsonResponse(bus_deung)
			if(db_get_idx(ids) == 75):
				db_update_idx(ids, 73)
				return JsonResponse(bus_deung)
			if(db_get_idx(ids) == 76):
				db_update_idx(ids, 73)
				return JsonResponse(bus_deung)
			if(db_get_idx(ids) == 77):
				db_update_idx(ids, 73)
				return JsonResponse(bus_deung)
			if(db_get_idx(ids) == 78):
				db_update_idx(ids, 72)
				return JsonResponse(bus_noc)														
			if(db_get_idx(ids) == 79):
				db_update_idx(ids, 78)
				return JsonResponse(bus_sun)
			if(db_get_idx(ids) == 80):
				db_update_idx(ids, 78)
				return JsonResponse(bus_sun)
			if(db_get_idx(ids) == 81):
				db_update_idx(ids, 78)
				return JsonResponse(bus_sun)
			if(db_get_idx(ids) == 82):
				db_update_idx(ids, 2)
				return JsonResponse(service_list)
			if(db_get_idx(ids) == 83):
				db_update_idx(ids, 82)
				return JsonResponse(mypage)
			if(db_get_idx(ids) == 84):
				db_update_idx(ids, 83)
				return JsonResponse(knucoin_main)
			if(db_get_idx(ids) == 85):
				db_update_idx(ids, 83)
				return JsonResponse(knucoin_main)		
		else:
			return JsonResponse(notfriend)	

	if(strs == "메인"):
		if(db_not_friend(ids) != 'X'):
			db_update_idx(ids, 0)
			return JsonResponse(main)	
		else:
			return JsonResponse(notfriend)

	elif(strs == "서비스"):
		if(db_not_friend(ids) != 'X'):
			db_update_idx(ids, 2)
			return JsonResponse(service_list)
		else:		
			return JsonResponse(notfriend)
	

	#학식 코드 시작!

	elif(strs == "학식보기"):
		if(db_not_friend(ids) != 'X'):
			db_update_idx(ids, 3)
			return JsonResponse(haksik)
		else:
			return JsonResponse(notfriend)
	elif(db_get_idx(ids) == 3):
		if(strs == "천안캠퍼스"):
			if(db_not_friend(ids) != 'X'):
				db_update_idx(ids, 4)
				return JsonResponse(cheonan)
			else:
				return JsonResponse(notfriend)
		if(strs == "신관캠퍼스"):
			if(db_not_friend(ids) != 'X'):
				db_update_idx(ids, 8)
				return JsonResponse(singwan)
			else:
				return JsonResponse(notfriend)
		if(strs == "예산캠퍼스"):
			if(db_not_friend(ids) != 'X'):
				db_update_idx(ids, 14)
				return JsonResponse(yesan)
			else:
				return JsonResponse(notfriend)

	elif(strs == "학생 식당"):
		if(db_get_idx(ids) == 4):
			db_update_idx(ids,5)
			return JsonResponse(alert)
		elif(db_get_idx(ids) == 8):
			db_update_idx(ids,9)
			return JsonResponse(alert)
		elif(db_get_idx(ids) == 14):
			db_update_idx(ids,15)
			return JsonResponse(alert)

	elif(strs == "직원 식당"):
		if(db_get_idx(ids) == 4):
			db_update_idx(ids,6)
			bob['message']['text'] = db_get(staff_ch, now)	
			return JsonResponse(bob)
		elif(db_get_idx(ids) == 8):
			db_update_idx(ids,10)
			bob['message']['text'] = db_get(staff_si, now)	
			return JsonResponse(bob)
		elif(db_get_idx(ids) == 14):
			db_update_idx(ids,16)
			bob['message']['text'] = db_get(staff_ye, now)	
			return JsonResponse(bob)
		else:
			return JsonResponse(call_admin)

	elif(strs == "생활관 식당"):
		if(db_get_idx(ids) == 4):
			return JsonResponse(alert)
			# 천안캠퍼스 생활관식당 
		elif(db_get_idx(ids) == 8):
			db_update_idx(ids,11)
			return JsonResponse(singwan_dormi)
		else:
			return JsonResponse(call_admin)
	elif(strs == "은행사/비전"):
		db_update_idx(ids, 12)
		return JsonResponse(alert)

	elif(strs == "드림하우스"):
		db_update_idx(ids, 13)
		return JsonResponse(alert)

	# 학식 끝!

	# 공지 코드 시작

	elif(strs == "공지사항"):
		if(db_not_friend(ids) != 'X'):
			db_update_idx(ids, 17)
			return JsonResponse(notics)
		else:
			return JsonResponse(notfriend)
	elif(strs == "학생소식"):
		if(db_not_friend(ids) != 'X'):
			if(db_get_idx(ids) == 17):
				db_update_idx(ids, 18)
				dic = db_get(Announs_kongju,now)
				title = announToTitle(dic)
				title.append("뒤로가기")
				announ_kongju_view['keyboard']['buttons'] = title
				return JsonResponse(announ_kongju_view)
		else:
			return JsonResponse(notfriend)

	# 공과 대학 부분

	elif(strs == "공과대학"):
		if(db_not_friend(ids) != 'X'):
			if(db_get_idx(ids) == 17):
				db_update_idx(ids, 19)
				return JsonResponse(notics_brain)
		else:
			return JsonResponse(notfriend)

	elif(db_get_idx(ids) == 19):
		if(strs == "공과대학공지"):
			db_update_idx(ids, 20)
			dic = db_get(Announs_brain , now)
			title = announToTitle(dic)
			title.append("뒤로가기")
			announ_brain_view['keyboard']['buttons'] = title
			return JsonResponse(announ_brain_view)
		if(strs == "컴퓨터공학부"):
			db_update_idx(ids, 21)
			dic = db_get(Announs_cse , now)
			title = announToTitle(dic)
			title.append("뒤로가기")
			announ_cse_view['keyboard']['buttons'] = title
			return JsonResponse(announ_cse_view)
		if(strs == "제어계측공학전공"):
			db_update_idx(ids, 22)
			dic = db_get(Announs_control , now)
			title = announToTitle(dic)
			title.append("뒤로가기")
			announ_control_view['keyboard']['buttons'] = title
			return JsonResponse(announ_control_view)
		if(strs == "기계자동차공학부"):
			db_update_idx(ids, 23)
			dic = db_get(Announs_mech , now)
			title = announToTitle(dic)
			title.append("뒤로가기")
			announ_mech_view['keyboard']['buttons'] = title
			return JsonResponse(announ_mech_view)
		if(strs == "건설환경공학부"):
			db_update_idx(ids, 24)
			dic = db_get(Announs_civil , now)
			title = announToTitle(dic)
			title.append("뒤로가기")
			announ_civil_view['keyboard']['buttons'] = title
			return JsonResponse(announ_civil_view)
		if(strs == "건축학부"):
			db_update_idx(ids, 25)
			dic = db_get(Announs_archi , now)
			title = announToTitle(dic)
			title.append("뒤로가기")
			announ_archi_view['keyboard']['buttons'] = title
			return JsonResponse(announ_archi_view)
		if(strs == "건축공학부"):
			db_update_idx(ids, 26)
			dic = db_get(Announs_archeng , now)
			title = announToTitle(dic)
			title.append("뒤로가기")
			announ_archeng_view['keyboard']['buttons'] = title
			return JsonResponse(announ_archeng_view)
		if(strs == "신소재공학부"):
			db_update_idx(ids, 27)
			dic = db_get(Announs_ame , now)
			title = announToTitle(dic)
			title.append("뒤로가기")
			announ_ame_view['keyboard']['buttons'] = title
			return JsonResponse(announ_ame_view)
		if(strs == "산업시스템공학과"):
			db_update_idx(ids, 28)
			dic = db_get(Announs_ie , now)
			title = announToTitle(dic)
			title.append("뒤로가기")
			announ_ie_view['keyboard']['buttons'] = title
			return JsonResponse(announ_ie_view)
		if(strs == "광공학과"):
			db_update_idx(ids, 29)
			dic = db_get(Announs_optical , now)
			title = announToTitle(dic)
			title.append("뒤로가기")
			announ_optical_view['keyboard']['buttons'] = title
			return JsonResponse(announ_optical_view)
	# 공과 대학 끝

	# 사범 대학 부분
	elif(strs == "사범대학"):
		if(db_not_friend(ids) != 'X'):
			if(db_get_idx(ids) == 17):
				db_update_idx(ids, 30)
				return JsonResponse(notics_sabum)
		else:
			return JsonResponse(notfriend)

	elif(db_get_idx(ids) == 30):
		if(strs == "사범대학공지"):
			db_update_idx(ids,31)
			dic = db_get(Announs_sabum , now)
			title = announToTitle(dic)
			title.append("뒤로가기")
			announ_sabum_view['keyboard']['buttons'] = title
			return JsonResponse(announ_sabum_view)
		if(strs == "지구과학교육과"):
			db_update_idx(ids,32)
			dic = db_get(Announs_earth, now)
			title = announToTitle(dic)
			title.append("뒤로가기")
			announ_earth_view['keyboard']['buttons'] = title
			return JsonResponse(announ_earth_view)
	# 사범 대학 끝
	# 인사대 시작
	elif(strs == "인문사회과학대학"):
		if(db_not_friend(ids) != 'X'):
			if(db_get_idx(ids) == 17):
				db_update_idx(ids, 33)
				return JsonResponse(notics_insa)
		else:
			return JsonResponse(notfriend)
	elif(db_get_idx(ids) == 33):
		if(strs == "인문사회과학대학공지"):
			db_update_idx(ids, 34)
			dic = db_get(Announs_insa , now)
			title = announToTitle(dic)
			title.append("뒤로가기")
			announ_insa_view['keyboard']['buttons'] = title
			return JsonResponse(announ_insa_view)
		if(strs == "중어중문학과"):
			db_update_idx(ids, 35)
			dic = db_get(Announs_chinese , now)
			title = announToTitle(dic)
			title.append("뒤로가기")
			announ_chinese_view['keyboard']['buttons'] = title
			return JsonResponse(announ_chinese_view)
		if(strs == "영어영문학과"):
			db_update_idx(ids, 36)
			dic = db_get(Announs_eng , now)
			title = announToTitle(dic)
			title.append("뒤로가기")
			announ_eng_view['keyboard']['buttons'] = title
			return JsonResponse(announ_eng_view)
		if(strs == "불어불문학과"):
			db_update_idx(ids, 37)
			dic = db_get(Announs_france , now)
			title = announToTitle(dic)
			title.append("뒤로가기")
			announ_france_view['keyboard']['buttons'] = title
			return JsonResponse(announ_france_view)
		if(strs == "독어독문학과"):
			db_update_idx(ids, 38)
			dic = db_get(Announs_german , now)
			title = announToTitle(dic)
			title.append("뒤로가기")
			announ_german_view['keyboard']['buttons'] = title
			return JsonResponse(announ_german_view)
		if(strs == "사학과"):
			db_update_idx(ids, 39)
			dic = db_get(Announs_history , now)
			title = announToTitle(dic)
			title.append("뒤로가기")
			announ_history_view['keyboard']['buttons'] = title
			return JsonResponse(announ_history_view)
		if(strs == "지리학과"):
			db_update_idx(ids, 40)
			dic = db_get(Announs_geography , now)
			title = announToTitle(dic)
			title.append("뒤로가기")
			announ_geography_view['keyboard']['buttons'] = title
			return JsonResponse(announ_geography_view)
		if(strs == "경제학전공"):
			db_update_idx(ids, 41)
			dic = db_get(Announs_economics , now)
			title = announToTitle(dic)
			title.append("뒤로가기")
			announ_economics_view['keyboard']['buttons'] = title
			return JsonResponse(announ_economics_view)
		if(strs == "국제통상학전공"):
			db_update_idx(ids, 42)
			dic = db_get(Announs_intrade , now)
			title = announToTitle(dic)
			title.append("뒤로가기")
			announ_intrade_view['keyboard']['buttons'] = title
			return JsonResponse(announ_intrade_view)
		if(strs == "경영학과"):
			db_update_idx(ids, 43)
			dic = db_get(Announs_business , now)
			title = announToTitle(dic)
			title.append("뒤로가기")
			announ_business_view['keyboard']['buttons'] = title
			return JsonResponse(announ_business_view)
		if(strs == "관광경영학전공"):
			db_update_idx(ids, 44)
			dic = db_get(Announs_tourism , now)
			title = announToTitle(dic)
			title.append("뒤로가기")
			announ_tourism_view['keyboard']['buttons'] = title
			return JsonResponse(announ_tourism_view)
		if(strs == "관광영어통역학전공"):
			db_update_idx(ids, 45)
			dic = db_get(Announs_tourismenglish , now)
			title = announToTitle(dic)
			title.append("뒤로가기")
			announ_tourismenglish_view['keyboard']['buttons'] = title
			return JsonResponse(announ_tourismenglish_view)
		if(strs == "행정학과"):
			db_update_idx(ids, 46)
			dic = db_get(Announs_public , now)
			title = announToTitle(dic)
			title.append("뒤로가기")
			announ_public_view['keyboard']['buttons'] = title
			return JsonResponse(announ_public_view)
		if(strs == "법학과"):
			db_update_idx(ids, 47)
			dic = db_get(Announs_law , now)
			title = announToTitle(dic)
			title.append("뒤로가기")
			announ_law_view['keyboard']['buttons'] = title
			return JsonResponse(announ_law_view)
		if(strs == "사회복지학과"):
			db_update_idx(ids, 48)
			dic = db_get(Announs_socialwelfare , now)
			title = announToTitle(dic)
			title.append("뒤로가기")
			announ_socialwelfare_view['keyboard']['buttons'] = title
			return JsonResponse(announ_socialwelfare_view)
		# 인사대 끝
		#자연과학대학
	#elif(strs == "자연과학대학"):
	#	if(db_get_idx(ids) == 18):
	#		db_update_idx(ids,50)
	#		dic = db_get(Announs_natural , now)
	#		title = announToTitle(dic)
	#		title.append("뒤로가기")
	#		announ_natural_view['keyboard']['buttons'] = title
	#		return JsonResponse(announ_natural_view)
	#	return JsonResponse(call_admin)
	# 자연과학대학 끝

	# 산업과학대학 시작
	elif(strs == "산업과학대학"):
		if(db_get_idx(ids) == 17):
			db_update_idx(ids,50)
			return JsonResponse(notics_indu)
	elif(db_get_idx(ids) == 50):
		if(strs == "산업과학대학공지"):
			db_update_idx(ids, 51)
			dic = db_get(Announs_indu , now)
			title = announToTitle(dic)
			title.append("뒤로가기")
			announ_indu_view['keyboard']['buttons'] = title
			return JsonResponse(announ_indu_view)
		if(strs == "산업유통학과"):
			db_update_idx(ids, 52)
			dic = db_get(Announs_cm , now)
			title = announToTitle(dic)
			title.append("뒤로가기")
			announ_cm_view['keyboard']['buttons'] = title
			return JsonResponse(announ_cm_view)
		if(strs == "식물자원학과"):
			db_update_idx(ids, 53)
			dic = db_get(Announs_pr , now)
			title = announToTitle(dic)
			title.append("뒤로가기")
			announ_pr_view['keyboard']['buttons'] = title
			return JsonResponse(announ_pr_view)
		if(strs == "원예학과"):
			db_update_idx(ids, 54)
			dic = db_get(Announs_hort , now)
			title = announToTitle(dic)
			title.append("뒤로가기")
			announ_hort_view['keyboard']['buttons'] = title
			return JsonResponse(announ_hort_view)
		if(strs == "동물자원학과"):
			db_update_idx(ids, 55)
			dic = db_get(Announs_ars , now)
			title = announToTitle(dic)
			title.append("뒤로가기")
			announ_ars_view['keyboard']['buttons'] = title
			return JsonResponse(announ_ars_view)
		if(strs == "지역건설공학전공"):
			db_update_idx(ids, 56)
			dic = db_get(Announs_rce , now)
			title = announToTitle(dic)
			title.append("뒤로가기")
			announ_rce_view['keyboard']['buttons'] = title
			return JsonResponse(announ_rce_view)
		if(strs == "생물산업기계공학"):
			db_update_idx(ids, 57)
			dic = db_get(Announs_bme , now)
			title = announToTitle(dic)
			title.append("뒤로가기")
			announ_bme_view['keyboard']['buttons'] = title
			return JsonResponse(announ_bme_view)
		if(strs == "산림자원학과"):
			db_update_idx(ids, 58)
			dic = db_get(Announs_forest , now)
			title = announToTitle(dic)
			title.append("뒤로가기")
			announ_forest_view['keyboard']['buttons'] = title
			return JsonResponse(announ_forest_view)
		if(strs == "조경학과"):
			db_update_idx(ids, 59)
			dic = db_get(Announs_la , now)
			title = announToTitle(dic)
			title.append("뒤로가기")
			announ_la_view['keyboard']['buttons'] = title
			return JsonResponse(announ_la_view)
		if(strs == "식품영양학전공"):
			db_update_idx(ids, 60)
			dic = db_get(Announs_fan , now)
			title = announToTitle(dic)
			title.append("뒤로가기")
			announ_fan_view['keyboard']['buttons'] = title
			return JsonResponse(announ_fan_view)
		if(strs == "식품공학과"):
			db_update_idx(ids, 61)
			dic = db_get(Announs_food , now)
			title = announToTitle(dic)
			title.append("뒤로가기")
			announ_food_view['keyboard']['buttons'] = title
			return JsonResponse(announ_food_view)
		if(strs == "특수동물학과"):
			db_update_idx(ids, 62)
			dic = db_get(Announs_clas , now)
			title = announToTitle(dic)
			title.append("뒤로가기")
			announ_clas_view['keyboard']['buttons'] = title
			return JsonResponse(announ_clas_view)

		#산업과학대학 끝

	# 간호보건대학 시작
	elif(strs == "간호보건대학"):
		if(db_get_idx(ids) == 17):
			db_update_idx(ids, 63)
			return JsonResponse(notics_cnh)
	elif(db_get_idx(ids) == 63):
		if(strs=="간호보건대학공지"):
			db_update_idx(ids,64)
			dic = db_get(Announs_cnh , now)
			title = announToTitle(dic)
			title.append("뒤로가기")
			announ_cnh_view['keyboard']['buttons'] = title
			return JsonResponse(announ_cnh_view)
		if(strs == "보건행정학과"):
			db_update_idx(ids, 65)
			dic = db_get(Announs_dhm, now)
			title = announToTitle(dic)
			title.append("뒤로가기")
			announ_dhm_view['keyboard']['buttons'] = title
			return JsonResponse(announ_dhm_view)
		if(strs == "응급구조학과"):
			db_update_idx(ids, 66)
			dic = db_get(Announs_emt, now)
			title = announToTitle(dic)
			title.append("뒤로가기")
			announ_emt_view['keyboard']['buttons'] = title
			return JsonResponse(announ_emt_view)
		if(strs == "의료정보학과"):
			db_update_idx(ids, 67)
			dic = db_get(Announs_dmrhim, now)
			title = announToTitle(dic)
			title.append("뒤로가기")
			announ_dmrhim_view['keyboard']['buttons'] = title
			return JsonResponse(announ_dmrhim_view)
		#간호보건대학 끝

		#예술대학 시작
	elif(strs == "예술대학"):
		if(db_get_idx(ids) == 17):
			db_update_idx(ids, 68)
			return JsonResponse(notics_art)
		return JsonResponse(call_admin)
	elif(db_get_idx(ids) == 68):
		if(strs == "예술대학공지"):
			db_update_idx(ids, 69)
			dic = db_get(Announs_art, now)
			title = announToTitle(dic)
			title.append("뒤로가기")
			announ_art_view['keyboard']['buttons'] = title
			return JsonResponse(announ_art_view)
		if(strs == "조형디자인학부"):
			db_update_idx(ids, 70)
			dic = db_get(Announs_fdesign, now)
			title = announToTitle(dic)
			title.append("뒤로가기")
			announ_fdesign_view['keyboard']['buttons'] = title
			return JsonResponse(announ_fdesign_view)
		if(strs == "무용학과"):
			db_update_idx(ids, 71)
			dic = db_get(Announs_dance, now)
			title = announToTitle(dic)
			title.append("뒤로가기")
			announ_dance_view['keyboard']['buttons'] = title
			return JsonResponse(announ_dance_view)
	elif(strs == "버스시간"):
		if(db_not_friend(ids) != 'X'):
			db_update_idx(ids, 72)
			return JsonResponse(bus_noc)
		else:
			return JsonResponse(notfriend)
	elif(db_get_idx(ids) == 72):
		if(strs == "등교버스"):
			db_update_idx(ids, 73)
			return JsonResponse(bus_deung)
		if(strs == "순환버스"):
			db_update_idx(ids, 78)
			return JsonResponse(bus_sun)
	elif(db_get_idx(ids) == 73):
		if(strs == "유성"):
			db_update_idx(ids, 74)
			sz, lnk = image_lnk("유성-등교")
			print(lnk)
			bus_val['message']['photo']['url'] = lnk
			bus_val['message']['photo']['width'] = sz[0]
			bus_val['message']['photo']['height'] = sz[1]
			return JsonResponse(bus_val)
		if(strs == "청주"):
			db_update_idx(ids, 75)
			sz, lnk = image_lnk("청주-등교")
			bus_val['message']['photo']['url'] = lnk
			bus_val['message']['photo']['width'] = sz[0]
			bus_val['message']['photo']['height'] = sz[1]
			return JsonResponse(bus_val)
		if(strs == "천안"):
			db_update_idx(ids, 76)
			sz, lnk = image_lnk("천안-등교")
			bus_val['message']['photo']['url'] = lnk
			bus_val['message']['photo']['width'] = sz[0]
			bus_val['message']['photo']['height'] = sz[1]
			return JsonResponse(bus_val)
		if(strs == "대전"):
			db_update_idx(ids, 77)
			sz, lnk = image_lnk("대전-등교")
			bus_val['message']['photo']['url'] = lnk
			bus_val['message']['photo']['width'] = sz[0]
			bus_val['message']['photo']['height'] = sz[1]
			return JsonResponse(bus_val)
	elif(db_get_idx(ids) == 78):
		if(strs == "천안캠퍼스"):
			db_update_idx(ids, 79)
			sz, lnk = image_lnk("천안")
			bus_val['message']['photo']['width'] = sz[0]
			bus_val['message']['photo']['height'] = sz[1]
			return JsonResponse(bus_val)
		if(strs == "공주캠퍼스"):
			db_update_idx(ids, 80)
			sz, lnk = image_lnk("공주")
			bus_val['message']['photo']['width'] = sz[0]
			bus_val['message']['photo']['height'] = sz[1]
			return JsonResponse(bus_val)
		if(strs == "예산캠퍼스"):
			db_update_idx(ids, 81)
			sz, lnk = image_lnk("예산")
			bus_val['message']['photo']['width'] = sz[0]
			bus_val['message']['photo']['height'] = sz[1]
			return JsonResponse(bus_val)
	elif(strs == "내정보"):
		if(db_not_friend(ids) != 'X'):
			db_update_idx(ids, 82)
			return JsonResponse(mypage)
		else:
			return JsonResponse(notfriend)
	elif(strs == "KNUCOIN"):
		db_update_idx(ids,83)
		return JsonResponse(knucoin_main)

	if(db_get_idx(ids) == 18):
		g_url = announToURL(Announs_kongju,strs)
		if(g_url == "X"):
			return JsonResponse(call_admin)
		else:
			tmp = "[" + strs + "]\n공지사항의 링크는 아래에 적혀있습니다.\nurl : " + g_url 
			notics_value['message']['text'] = tmp
			return JsonResponse(notics_value)
		
	if(db_get_idx(ids) == 20):
		g_url = announToURL(Announs_brain,strs)
		if(g_url == "X"):
			return JsonResponse(call_admin)
		else:
			tmp = "[" + strs + "]\n공지사항의 링크는 아래에 적혀있습니다.\nurl : " + g_url 
			notics_value['message']['text'] = tmp
			return JsonResponse(notics_value)
	if(db_get_idx(ids) == 21):
		g_url = announToURL(Announs_cse,strs)
		if(g_url == "X"):
			return JsonResponse(call_admin)
		else:
			tmp = "[" + strs + "]\n공지사항의 링크는 아래에 적혀있습니다.\nurl : " + g_url 
			notics_value['message']['text'] = tmp
			return JsonResponse(notics_value)
	if(db_get_idx(ids) == 22):
		g_url = announToURL(Announs_control,strs)
		if(g_url == "X"):
			return JsonResponse(call_admin)
		else:
			tmp = "[" + strs + "]\n공지사항의 링크는 아래에 적혀있습니다.\nurl : " + g_url 
			notics_value['message']['text'] = tmp
			return JsonResponse(notics_value)
	if(db_get_idx(ids) == 23):
		g_url = announToURL(Announs_mech,strs)
		if(g_url == "X"):
			return JsonResponse(call_admin)
		else:
			tmp = "[" + strs + "]\n공지사항의 링크는 아래에 적혀있습니다.\nurl : " + g_url 
			notics_value['message']['text'] = tmp
			return JsonResponse(notics_value)
	if(db_get_idx(ids) == 24):
		g_url = announToURL(Announs_civil,strs)
		if(g_url == "X"):
			return JsonResponse(call_admin)
		else:
			tmp = "[" + strs + "]\n공지사항의 링크는 아래에 적혀있습니다.\nurl : " + g_url 
			notics_value['message']['text'] = tmp
			return JsonResponse(notics_value)
	if(db_get_idx(ids) == 25):
		g_url = announToURL(Announs_archi,strs)
		if(g_url == "X"):
			return JsonResponse(call_admin)
		else:
			tmp = "[" + strs + "]\n공지사항의 링크는 아래에 적혀있습니다.\nurl : " + g_url 
			notics_value['message']['text'] = tmp
			return JsonResponse(notics_value)
	if(db_get_idx(ids) == 26):
		g_url = announToURL(Announs_archeng,strs)
		if(g_url == "X"):
			return JsonResponse(call_admin)
		else:
			tmp = "[" + strs + "]\n공지사항의 링크는 아래에 적혀있습니다.\nurl : " + g_url 
			notics_value['message']['text'] = tmp
			return JsonResponse(notics_value)
	if(db_get_idx(ids) == 27):
		g_url = announToURL(Announs_ame,strs)
		if(g_url == "X"):
			return JsonResponse(call_admin)
		else:
			tmp = "[" + strs + "]\n공지사항의 링크는 아래에 적혀있습니다.\nurl : " + g_url 
			notics_value['message']['text'] = tmp
			return JsonResponse(notics_value)
	if(db_get_idx(ids) == 28):
		g_url = announToURL(Announs_ie,strs)
		if(g_url == "X"):
			return JsonResponse(call_admin)
		else:
			tmp = "[" + strs + "]\n공지사항의 링크는 아래에 적혀있습니다.\nurl : " + g_url 
			notics_value['message']['text'] = tmp
			return JsonResponse(notics_value)
	if(db_get_idx(ids) == 29):
		g_url = announToURL(Announs_optical,strs)
		if(g_url == "X"):
			return JsonResponse(call_admin)
		else:
			tmp = "[" + strs + "]\n공지사항의 링크는 아래에 적혀있습니다.\nurl : " + g_url 
			notics_value['message']['text'] = tmp
			return JsonResponse(notics_value)


	if(db_get_idx(ids) == 31):
		g_url = announToURL(Announs_sabum,strs)
		if(g_url == "X"):
			return JsonResponse(call_admin)
		else:
			tmp = "[" + strs + "]\n공지사항의 링크는 아래에 적혀있습니다.\nurl : " + g_url 
			notics_value['message']['text'] = tmp
			return JsonResponse(notics_value)
	if(db_get_idx(ids) == 32):
		g_url = announToURL(Announs_earth, strs)
		if(g_url == "X"):
			return JsonResponse(call_admin)
		else:
			tmp = "[" + strs + "]\n공지사항의 링크는 아래에 적혀있습니다.\nurl : " + g_url
			notics_value['message']['text'] = tmp
			return JsonResponse(notics_value)
	if(db_get_idx(ids) == 34):
		g_url = announToURL(Announs_insa,strs)
		if(g_url == "X"):
			return JsonResponse(call_admin)
		else:
			tmp = "[" + strs + "]\n공지사항의 링크는 아래에 적혀있습니다.\nurl : " + g_url 
			notics_value['message']['text'] = tmp
			return JsonResponse(notics_value)
	if(db_get_idx(ids) == 35):
		g_url = announToURL(Announs_chinese, strs)
		if(g_url == "X"):
			return JsonResponse(call_admin)
		else:
			tmp = "[" + strs + "]\n공지사항의 링크는 아래에 적혀있습니다.\nurl : " + g_url
			notics_value['message']['text'] = tmp
			return JsonResponse(notics_value)
	if(db_get_idx(ids) == 36):
		g_url = announToURL(Announs_eng, strs)
		if(g_url == "X"):
			return JsonResponse(call_admin)
		else:
			tmp = "[" + strs + "]\n공지사항의 링크는 아래에 적혀있습니다.\nurl : " + g_url
			notics_value['message']['text'] = tmp
			return JsonResponse(notics_value)
	if(db_get_idx(ids) == 37):
		g_url = announToURL(Announs_france, strs)
		if(g_url == "X"):
			return JsonResponse(call_admin)
		else:
			tmp = "[" + strs + "]\n공지사항의 링크는 아래에 적혀있습니다.\nurl : " + g_url
			notics_value['message']['text'] = tmp
			return JsonResponse(notics_value)
	if(db_get_idx(ids) == 38):
		g_url = announToURL(Announs_german, strs)
		if(g_url == "X"):
			return JsonResponse(call_admin)
		else:
			tmp = "[" + strs + "]\n공지사항의 링크는 아래에 적혀있습니다.\nurl : " + g_url
			notics_value['message']['text'] = tmp
			return JsonResponse(notics_value)
	if(db_get_idx(ids) == 39):
		g_url = announToURL(Announs_history, strs)
		if(g_url == "X"):
			return JsonResponse(call_admin)
		else:
			tmp = "[" + strs + "]\n공지사항의 링크는 아래에 적혀있습니다.\nurl : " + g_url
			notics_value['message']['text'] = tmp
			return JsonResponse(notics_value)
	if(db_get_idx(ids) == 40):
		g_url = announToURL(Announs_geography, strs)
		if(g_url == "X"):
			return JsonResponse(call_admin)
		else:
			tmp = "[" + strs + "]\n공지사항의 링크는 아래에 적혀있습니다.\nurl : " + g_url
			notics_value['message']['text'] = tmp
			return JsonResponse(notics_value)
	if(db_get_idx(ids) == 41):
		g_url = announToURL(Announs_economics, strs)
		if(g_url == "X"):
			return JsonResponse(call_admin)
		else:
			tmp = "[" + strs + "]\n공지사항의 링크는 아래에 적혀있습니다.\nurl : " + g_url
			notics_value['message']['text'] = tmp
			return JsonResponse(notics_value)
	if(db_get_idx(ids) == 42):
		g_url = announToURL(Announs_intrade, strs)
		if(g_url == "X"):
			return JsonResponse(call_admin)
		else:
			tmp = "[" + strs + "]\n공지사항의 링크는 아래에 적혀있습니다.\nurl : " + g_url
			notics_value['message']['text'] = tmp
			return JsonResponse(notics_value)
	if(db_get_idx(ids) == 43):
		g_url = announToURL(Announs_business, strs)
		if(g_url == "X"):
			return JsonResponse(call_admin)
		else:
			tmp = "[" + strs + "]\n공지사항의 링크는 아래에 적혀있습니다.\nurl : " + g_url
			notics_value['message']['text'] = tmp
			return JsonResponse(notics_value)
	if(db_get_idx(ids) == 44):
		g_url = announToURL(Announs_tourism, strs)
		if(g_url == "X"):
			return JsonResponse(call_admin)
		else:
			tmp = "[" + strs + "]\n공지사항의 링크는 아래에 적혀있습니다.\nurl : " + g_url
			notics_value['message']['text'] = tmp
			return JsonResponse(notics_value)
	if(db_get_idx(ids) == 45):
		g_url = announToURL(Announs_tourismenglish, strs)
		if(g_url == "X"):
			return JsonResponse(call_admin)
		else:
			tmp = "[" + strs + "]\n공지사항의 링크는 아래에 적혀있습니다.\nurl : " + g_url
			notics_value['message']['text'] = tmp
			return JsonResponse(notics_value)
	if(db_get_idx(ids) == 46):
		g_url = announToURL(Announs_public, strs)
		if(g_url == "X"):
			return JsonResponse(call_admin)
		else:
			tmp = "[" + strs + "]\n공지사항의 링크는 아래에 적혀있습니다.\nurl : " + g_url
			notics_value['message']['text'] = tmp
			return JsonResponse(notics_value)
	if(db_get_idx(ids) == 47):
		g_url = announToURL(Announs_law, strs)
		if(g_url == "X"):
			return JsonResponse(call_admin)
		else:
			tmp = "[" + strs + "]\n공지사항의 링크는 아래에 적혀있습니다.\nurl : " + g_url
			notics_value['message']['text'] = tmp
			return JsonResponse(notics_value)
	if(db_get_idx(ids) == 48):
		g_url = announToURL(Announs_socialwelfare, strs)
		if(g_url == "X"):
			return JsonResponse(call_admin)
		else:
			tmp = "[" + strs + "]\n공지사항의 링크는 아래에 적혀있습니다.\nurl : " + g_url
			notics_value['message']['text'] = tmp
			return JsonResponse(notics_value)

	#if(db_get_idx(ids) == 49):
	#	g_url = announToURL(Announs_natural,strs)
	#	if(g_url == "X"):
	#		return JsonResponse(call_admin)
	#	else:
	#		tmp = "[" + strs + "]\n공지사항의 링크는 아래에 적혀있습니다.\nurl : " + g_url 
	#		notics_value['message']['text'] = tmp
	#		return JsonResponse(notics_value)

	if(db_get_idx(ids) == 51):
		g_url = announToURL(Announs_indu,strs)
		if(g_url == "X"):
			return JsonResponse(call_admin)
		else:
			tmp = "[" + strs + "]\n공지사항의 링크는 아래에 적혀있습니다.\nurl : " + g_url 
			notics_value['message']['text'] = tmp
			return JsonResponse(notics_value)

	if(db_get_idx(ids) == 52):
		g_url = announToURL(Announs_cm,strs)
		if(g_url == "X"):
			return JsonResponse(call_admin)
		else:
			tmp = "[" + strs + "]\n공지사항의 링크는 아래에 적혀있습니다.\nurl : " + g_url 
			notics_value['message']['text'] = tmp
			return JsonResponse(notics_value)
	if(db_get_idx(ids) == 53):
		g_url = announToURL(Announs_pr,strs)
		if(g_url == "X"):
			return JsonResponse(call_admin)
		else:
			tmp = "[" + strs + "]\n공지사항의 링크는 아래에 적혀있습니다.\nurl : " + g_url 
			notics_value['message']['text'] = tmp
			return JsonResponse(notics_value)
	if(db_get_idx(ids) == 54):
		g_url = announToURL(Announs_hort,strs)
		if(g_url == "X"):
			return JsonResponse(call_admin)
		else:
			tmp = "[" + strs + "]\n공지사항의 링크는 아래에 적혀있습니다.\nurl : " + g_url 
			notics_value['message']['text'] = tmp
			return JsonResponse(notics_value)
	if(db_get_idx(ids) == 55):
		g_url = announToURL(Announs_ars,strs)
		if(g_url == "X"):
			return JsonResponse(call_admin)
		else:
			tmp = "[" + strs + "]\n공지사항의 링크는 아래에 적혀있습니다.\nurl : " + g_url 
			notics_value['message']['text'] = tmp
			return JsonResponse(notics_value)
	if(db_get_idx(ids) == 56):
		g_url = announToURL(Announs_rce,strs)
		if(g_url == "X"):
			return JsonResponse(call_admin)
		else:
			tmp = "[" + strs + "]\n공지사항의 링크는 아래에 적혀있습니다.\nurl : " + g_url 
			notics_value['message']['text'] = tmp
			return JsonResponse(notics_value)
	if(db_get_idx(ids) == 57):
		g_url = announToURL(Announs_bme,strs)
		if(g_url == "X"):
			return JsonResponse(call_admin)
		else:
			tmp = "[" + strs + "]\n공지사항의 링크는 아래에 적혀있습니다.\nurl : " + g_url 
			notics_value['message']['text'] = tmp
			return JsonResponse(notics_value)
	if(db_get_idx(ids) == 58):
		g_url = announToURL(Announs_forest,strs)
		if(g_url == "X"):
			return JsonResponse(call_admin)
		else:
			tmp = "[" + strs + "]\n공지사항의 링크는 아래에 적혀있습니다.\nurl : " + g_url 
			notics_value['message']['text'] = tmp
			return JsonResponse(notics_value)
	if(db_get_idx(ids) == 59):
		g_url = announToURL(Announs_la,strs)
		if(g_url == "X"):
			return JsonResponse(call_admin)
		else:
			tmp = "[" + strs + "]\n공지사항의 링크는 아래에 적혀있습니다.\nurl : " + g_url 
			notics_value['message']['text'] = tmp
			return JsonResponse(notics_value)
	if(db_get_idx(ids) == 60):
		g_url = announToURL(Announs_fan,strs)
		if(g_url == "X"):
			return JsonResponse(call_admin)
		else:
			tmp = "[" + strs + "]\n공지사항의 링크는 아래에 적혀있습니다.\nurl : " + g_url 
			notics_value['message']['text'] = tmp
			return JsonResponse(notics_value)
	if(db_get_idx(ids) == 61):
		g_url = announToURL(Announs_food,strs)
		if(g_url == "X"):
			return JsonResponse(call_admin)
		else:
			tmp = "[" + strs + "]\n공지사항의 링크는 아래에 적혀있습니다.\nurl : " + g_url 
			notics_value['message']['text'] = tmp
			return JsonResponse(notics_value)
	if(db_get_idx(ids) == 62):
		g_url = announToURL(Announs_clas,strs)
		if(g_url == "X"):
			return JsonResponse(call_admin)
		else:
			tmp = "[" + strs + "]\n공지사항의 링크는 아래에 적혀있습니다.\nurl : " + g_url 
			notics_value['message']['text'] = tmp
			return JsonResponse(notics_value)



	if(db_get_idx(ids) == 64):
		g_url = announToURL(Announs_cnh,strs)
		if(g_url == "X"):
			return JsonResponse(call_admin)
		else:
			tmp = "[" + strs + "]\n공지사항의 링크는 아래에 적혀있습니다.\nurl : " + g_url 
			notics_value['message']['text'] = tmp
			return JsonResponse(notics_value)
	if(db_get_idx(ids) == 65):
		g_url = announToURL(Announs_dhm,strs)
		if(g_url == "X"):
			return JsonResponse(call_admin)
		else:
			tmp = "[" + strs + "]\n공지사항의 링크는 아래에 적혀있습니다.\nurl : " + g_url 
			notics_value['message']['text'] = tmp
			return JsonResponse(notics_value)
	if(db_get_idx(ids) == 66):
		g_url = announToURL(Announs_emt,strs)
		if(g_url == "X"):
			return JsonResponse(call_admin)
		else:
			tmp = "[" + strs + "]\n공지사항의 링크는 아래에 적혀있습니다.\nurl : " + g_url 
			notics_value['message']['text'] = tmp
			return JsonResponse(notics_value)
	if(db_get_idx(ids) == 67):
		g_url = announToURL(Announs_dmrhim,strs)
		if(g_url == "X"):
			return JsonResponse(call_admin)
		else:
			tmp = "[" + strs + "]\n공지사항의 링크는 아래에 적혀있습니다.\nurl : " + g_url 
			notics_value['message']['text'] = tmp
			return JsonResponse(notics_value)





	if(db_get_idx(ids) == 69):
		g_url = announToURL(Announs_art,strs)
		if(g_url == "X"):
			return JsonResponse(call_admin)
		else:
			tmp = "[" + strs + "]\n공지사항의 링크는 아래에 적혀있습니다.\nurl : " + g_url 
			notics_value['message']['text'] = tmp
			return JsonResponse(notics_value)
	if(db_get_idx(ids) == 70):
		g_url = announToURL(Announs_fdesign,strs)
		if(g_url == "X"):
			return JsonResponse(call_admin)
		else:
			tmp = "[" + strs + "]\n공지사항의 링크는 아래에 적혀있습니다.\nurl : " + g_url 
			notics_value['message']['text'] = tmp
			return JsonResponse(notics_value)
	if(db_get_idx(ids) == 71):
		g_url = announToURL(Announs_dance,strs)
		if(g_url == "X"):
			return JsonResponse(call_admin)
		else:
			tmp = "[" + strs + "]\n공지사항의 링크는 아래에 적혀있습니다.\nurl : " + g_url 
			notics_value['message']['text'] = tmp
			return JsonResponse(notics_value)


	else:
		return JsonResponse(sorry)
