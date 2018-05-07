First_level = {'top-L': '4', 'top-M': '9', 'top-R': '2'}
Mid_level = {'mid-L': '3', 'mid-M': '5', 'mid-R': '7'}
Last_level = {'low-L': '8', 'low-M': '1', 'low-R': '6'}

"""
Yang_1 = ['甲子戊','甲戌己','甲申庚','甲午辛','甲辰壬','甲寅癸','丁','丙','乙']
Yang_2 = ['乙','甲子戊','甲戌己','甲申庚','甲午辛','甲辰壬','甲寅癸','丁','丙']
Yang_3 = ['丙','乙','甲子戊','甲戌己','甲申庚','甲午辛','甲辰壬','甲寅癸','丁']
Yang_4 = ['丁','丙','乙','甲子戊','甲戌己','甲申庚','甲午辛','甲辰壬','甲寅癸']
Yang_5 = ['甲寅癸','丁','丙','乙','甲子戊','甲戌己','甲申庚','甲午辛','甲辰壬']
Yang_6 = ['甲辰壬','甲寅癸','丁','丙','乙','甲子戊','甲戌己','甲申庚','甲午辛']
Yang_7 = ['甲午辛','甲辰壬','甲寅癸','丁','丙','乙','甲子戊','甲戌己','甲申庚']
Yang_8 = ['甲申庚','甲午辛','甲辰壬','甲寅癸','丁','丙','乙','甲子戊','甲戌己']
Yang_9 = ['甲戌己','甲申庚','甲午辛','甲辰壬','甲寅癸','丁','丙','乙','甲子戊']
Yin_1= ['乙','丙','丁','甲寅癸','甲辰壬','甲午辛','甲申庚','甲戌己','甲子戊']
Yin_2= ['丙','丁','甲寅癸','甲辰壬','甲午辛','甲申庚','甲戌己','甲子戊','乙']
Yin_3= ['丁','甲寅癸','甲辰壬','甲午辛','甲申庚','甲戌己','甲子戊','乙','丙']
Yin_4= ['甲寅癸','甲辰壬','甲午辛','甲申庚','甲戌己','甲子戊','乙','丙','丁']
Yin_5= ['甲辰壬','甲午辛','甲申庚','甲戌己','甲子戊','乙','丙','丁','甲寅癸']
Yin_6= ['甲午辛','甲申庚','甲戌己','甲子戊','乙','丙','丁','甲寅癸','甲辰壬']
Yin_7= ['甲申庚','甲戌己','甲子戊','乙','丙','丁','甲寅癸','甲辰壬','甲午辛']
Yin_8= ['甲戌己','甲子戊','乙','丙','丁','甲寅癸','甲辰壬','甲午辛','甲申庚']
Yin_9= ['甲子戊','乙','丙','丁','甲寅癸','甲辰壬','甲午辛','甲申庚','甲戌己']
"""

jz60 = ['甲子','乙丑','丙寅','丁卯','戊辰','己巳','庚午','辛未','壬申','癸酉',
        '甲戌','乙亥','丙子','丁丑','戊寅','己卯','庚辰','辛巳','壬午','癸未',
        '甲申','乙酉','丙戌','丁亥','戊子','己丑','庚寅','辛卯','壬辰','癸巳',
        '甲午','乙未','丙申','丁酉','戊戌','己亥','庚子','辛丑','壬寅','癸卯',
        '甲辰','乙巳','丙午','丁未','戊申','己酉','庚戌','辛亥','壬子','癸丑',
        '甲寅','乙卯','丙辰','丁巳','戊午','己未','庚申','辛酉','壬戌','癸亥']

def Num_of_Dun(attribute,round): #attribute = 1(阴),0(阳);round = 局数
    if attribute == 1:
        print(Yin)
    elif attribute == 0:
        print(Yang)
    else:
        print('Error!')
print(Num_of_Dun(3,0))

import datetime
import dateutil.parser
import ephem
import time
years = time.strftime('%Y',time.localtime(time.time()))
xz = ephem.next_summer_solstice(years)
dz = ephem.next_winter_solstice(years)
cf = ephem.next_vernal_equinox(years)
qf = ephem.next_autumnal_equinox(years)
xz = str(xz)
dz = str(dz)
cf = str(cf)
qf = str(qf)
print('Now(UTC+8) ' + time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
print('Summer_solstice    GMT=' + xz)
print('Winter_solstice    GMT=' + dz)
print('Vernal_equinox     GMT=' + cf)
print('Autumnal_equinox   GMT=' + qf)
def getDateTime(s):
    d = dateutil.parser.parse(s)
    return d
print(getDateTime(xz) + datetime.timedelta(hours = 8))
print(getDateTime(dz) + datetime.timedelta(hours = 8))
print(getDateTime(cf) + datetime.timedelta(hours = 8))
print(getDateTime(qf) + datetime.timedelta(hours = 8))

#年份天干地支
test_year = '2018' #上限2104
def cc_year (test_year):
    year_tg = int(test_year) - all_date_time[0] + 34
    if year_tg <= 59:
        print(jz60[year_tg])
    else:
        year_tg1 = year_tg - 60
        print(jz60[year_tg1])
print(cc_year(test_year))
