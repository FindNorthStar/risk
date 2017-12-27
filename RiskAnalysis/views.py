# -*- coding: UTF-8 -*-

import random

import time
from datetime import datetime, date

import json

import jieba
import re
from django.db import connection
from django.db.models import Count
from django.db.models.functions import TruncMonth
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, render_to_response

# Create your views here.
from RiskAnalysis.models import *


def platform_region(request):
    list_platform = CompanyList.objects.all()

    dict_region = {}

    for item in list_platform:
        if item.area not in dict_region:
            dict_region[item.area] = [item.platform]
        else:
            dict_region[item.area].append(item.platform)

    response_data = '[\n'

    for region, list_business in dict_region.items():
        length = len(list_business)

        # 一个省只有一个平台
        if length == 1:
            response_data += '{"source":"' + list_business[0] + '","target":"' + list_business[
                0] + '","region":"' + region + '"},\n'
            continue
        else:
            center_platform = list_business[0]
            for i in range(1, length):
                if i > 10:
                    break
                branch_platorm = list_business[i]
                response_data += '{"source":"' + center_platform + \
                                 '","target":"' + branch_platorm + \
                                 '","region":"' + region + '"},\n'

    response_data = response_data[:-2] + '\n'

    response_data += ']\n'

    return HttpResponse(response_data)

# 平台与其子公司的司法关系
def business_relation(request):
    platform_id = request.session.get('platform_id')

    company_name_list = CompanyList.objects.filter(id=platform_id)

    company_name = company_name_list[0].company

    branch_info = Branchinfo.objects.values('branch_name').filter(platform_name=company_name)

    law_result = Documentjudgment.objects.values("platform_name", "case_brief").annotate(
        case_count=Count("case_brief")).filter(platform_name=company_name)

    links_data = []

    links_data.append({
        'source': company_name,
        'target': company_name,
        'type': "anim_element remove_on_reload",
        'color': "c6dbef",
        'value': "60"
    })


    branch_num = 1

    if len(branch_info) > 0:
        for branch_item in branch_info:
            if branch_num > 10:
                break

            links_data.append({
                'source': company_name,
                'target': branch_item['branch_name'],
                'type': "anim_element remove_on_reload",
                'color': "c6dbef",
                'value': random.randint(20, 45)
            })

            for law_item in law_result:

                if random.randint(0, 10) < 5:
                    links_data.append({
                        'source': branch_item['branch_name'],
                        'target': law_item['case_brief'] + str(branch_num),
                        'type': "anim_element remove_on_reload",
                        'color': "FFB444",
                        'value': law_item['case_count']
                    })

                    links_data.append({
                        'source': branch_item['branch_name'],
                        'target': law_item['case_brief'] + str(branch_num),
                        'type': "anim_element remove_on_reload",
                        'color': "FFB444",
                        'value': law_item['case_count']
                    })

            branch_num += 1
    else:
        for law_item in law_result:
            links_data.append({
                'source': company_name,
                'target': law_item['case_brief'] + str(branch_num),
                'type': "anim_element remove_on_reload",
                'color': "FFB444",
                'value': law_item['case_count']*10
            })

            branch_num+=1


    flot_data = {'link_data': links_data}

    return JsonResponse(flot_data)


# 获取经营数据,拼成数组
def price(request):
    platform_id = request.session.get('platform_id')

    list_company = CompanyList.objects.filter(id=platform_id)

    # company_name = list_company[0].company
    platform_name = list_company[0].platform

    # 经营信息
    wdzj_info = Wdzjinfo.objects.filter(platform_name=platform_name, startdate__lt=date(2017, 10, 10))

    list_price = []
    list_sum_price = []

    sum_price = 0

    for item in wdzj_info:
        date_split = str(item.enddate).split('-')
        dtime = date(int(date_split[0]), int(date_split[1]), int(date_split[2]))
        unix_time = int(time.mktime(dtime.timetuple()) * 1000)

        sum_price += float(item.amount)

        list_sum_price.append([unix_time, sum_price])
        list_price.append([unix_time, float(item.amount)])

    flot_data = {'each_prices': list_price, 'sum_prices': list_sum_price}

    # return HttpResponse(json.dumps(flot_data), content_type="application/json")
    return JsonResponse(flot_data)


# 获取经营数据,拼成数组
def guotai_price(request):
    platform_id = request.session.get('platform_id')

    list_company = CompanyList.objects.filter(id=platform_id)

    # company_name = list_company[0].company
    platform_name = list_company[0].platform

    # 经营信息
    guotai_info = Guotai.objects.filter(fullname=platform_name)

    list_price = []
    list_sum_price = []

    sum_price = 0

    for item in guotai_info[::-1]:
        # print(item.tradingdate, item.tradingvolume, item.avereturn)

        date_split = str(item.tradingdate).split('-')
        dtime = date(int(date_split[0]), int(date_split[1]), int(date_split[2]))
        unix_time = int(time.mktime(dtime.timetuple()) * 1000)
        sum_price += float(item.tradingvolume)
        list_sum_price.append([unix_time, sum_price])
        list_price.append([unix_time, float(item.tradingvolume)])

    flot_data = {'each_prices': list_price, 'sum_prices': list_sum_price}

    # return HttpResponse(json.dumps(flot_data), content_type="application/json")
    return JsonResponse(flot_data)

# 获取收益率,拼成数组
def income_rate(request):
    platform_id = request.session.get('platform_id')

    list_company = CompanyList.objects.filter(id=platform_id)

    # company_name = list_company[0].company
    platform_name = list_company[0].platform

    # 经营信息
    wdzj_info = Wdzjinfo.objects.filter(platform_name=platform_name, startdate__lt=date(2017, 10, 10))

    list_income_rate = []

    for item in wdzj_info:
        list_income_rate.append(float(item.incomerate))

    flot_data = {'income_rate': list_income_rate}

    return JsonResponse(flot_data)


# 获取收益率,拼成数组
def guotai_income_rate(request):
    platform_id = request.session.get('platform_id')

    list_company = CompanyList.objects.filter(id=platform_id)

    # company_name = list_company[0].company
    platform_name = list_company[0].platform

    # 经营信息
    guotai_info = Guotai.objects.filter(fullname=platform_name)

    list_income_rate = []

    for item in guotai_info[::-1]:

        list_income_rate.append(float(item.avereturn))

    flot_data = {'income_rate': list_income_rate}

    # return HttpResponse(json.dumps(flot_data), content_type="application/json")
    return JsonResponse(flot_data)


def get_season_dict(employ_info):
    dict_month_season = {
        '01': 'Q1',
        '02': 'Q1',
        '03': 'Q1',
        '04': 'Q2',
        '05': 'Q2',
        '06': 'Q2',
        '07': 'Q3',
        '08': 'Q3',
        '09': 'Q3',
        '10': 'Q4',
        '11': 'Q4',
        '12': 'Q4',
    }

    dict_season_employ = {}

    for item in employ_info:

        start_month = str(item['startmonth'])

        year = start_month[:4]
        month = start_month[4:]

        if month not in dict_month_season:
            continue

        season = str(year) + ' ' + dict_month_season[month]

        if season in dict_month_season:
            dict_season_employ[season] += int(item['case_count'])
        else:
            dict_season_employ[season] = int(item['case_count'])

    return dict_season_employ

def get_employ_num(employ_info,employ_info_bachlor,employ_info_no_degree):

    dict_season_employ = get_season_dict(employ_info)
    dict_season_employ_bachlor = get_season_dict(employ_info_bachlor)
    dict_season_employ_no_degree = get_season_dict(employ_info_no_degree)

    list_season_employ = []

    for key, val in dict_season_employ.items():
        dict_each_season = {'period': key, 'employee': val}

        if key in dict_season_employ_bachlor:
            dict_each_season['bachlor']=dict_season_employ_bachlor[key]
        else:
            dict_each_season['bachlor']=None

        if key in dict_season_employ_no_degree:
            dict_each_season['no_degree']=dict_season_employ_no_degree[key]
        else:
            dict_each_season['no_degree']=None

        list_season_employ.append(dict_each_season)

    return list_season_employ


# 获取每月招聘人数,拼成json
def employ_season(request):
    platform_id = request.session.get('platform_id')

    list_company = CompanyList.objects.filter(id=platform_id)

    company_name = list_company[0].company
    # platform_name = list_company[0].platform

    # 招聘信息
    employ_info = Employinfo.objects.values("platform_name", "startmonth").annotate(
        case_count=Count("startmonth")).filter(platform_name=company_name)

    employ_info_bachlor = Employinfo.objects.values("platform_name", "startmonth").annotate(
        case_count=Count("startmonth")).filter(platform_name=company_name,education='本科')

    employ_info_no_degree = Employinfo.objects.values("platform_name", "startmonth").annotate(
        case_count=Count("startmonth")).filter(platform_name=company_name, education='不限')

    list_season_employ = get_employ_num(employ_info,employ_info_bachlor,employ_info_no_degree)

    # flot_data = {'employ_data': list_season_employ}
    flot_data = {'employ_data': list_season_employ}

    return JsonResponse(flot_data)


# 获取国泰安4种数据,拼成json
def guotai_data(platform_id):

    list_company = CompanyList.objects.filter(id=platform_id)

    # company_name = list_company[0].company
    platform_name = list_company[0].platform

    # 国泰安经营信息

    cursor = connection.cursor()
    cursor.execute('SELECT sum(TradingVolume),sum(CumulateRepay),sum(F30Repay),sum(F60Repay),'
                   'date_format(TradingDate, "%Y-%m") FROM guotai where FullName="'+platform_name+
                   '" group by date_format(TradingDate, "%Y-%m");')
    guotai_info = cursor.fetchall()

    dict_month_season = {
        '01': 'Jan',
        '02': 'Feb',
        '03': 'Mar',
        '04': 'Apr',
        '05': 'May',
        '06': 'Jun',
        '07': 'Jul',
        '08': 'Aug',
        '09': 'Sep',
        '10': 'Oct',
        '11': 'Nov',
        '12': 'Dec',
    }

    list_trading_volume = ['symbol,date,price\n']
    list_cumulate_repay = []
    list_f30_repay = []
    list_f60_repay = []

    for item in guotai_info:
        date_split = item[4].split('-')
        year = date_split[0]
        month = dict_month_season[date_split[1]]

        list_trading_volume.append('成交量,'+month+' '+year+','+str(item[0])+'\n')
        list_cumulate_repay.append('累计待还金额,'+month+' '+year+','+str(item[1])+'\n')
        list_f30_repay.append('近30日资金净流入,'+month+' '+year+','+str(item[2])+'\n')
        list_f60_repay.append('未来60日待还,'+month+' '+year+','+str(item[3])+'\n')

    list_trading_volume.extend(list_cumulate_repay)
    list_trading_volume.extend(list_f30_repay)
    list_trading_volume.extend(list_f60_repay)

    score_csv = 'RiskAnalysis/static/data/stocks.csv'

    with open(score_csv, 'w') as f:
        f.writelines(list_trading_volume)


# 获取招聘学历,拼成json
def employ_level(request):
    platform_id = request.session.get('platform_id')

    list_company = CompanyList.objects.filter(id=platform_id)

    company_name = list_company[0].company
    # platform_name = list_company[0].platform

    # 招聘信息
    employ_info = Employinfo.objects.values("platform_name", "education").annotate(
        case_count=Count("education")).filter(platform_name=company_name)

    list_education_employ = []

    for item in employ_info:

        education = item['education']
        employ_num = item['case_count']

        if education != '':
            list_education_employ.append({'label':education,'value':employ_num})

    flot_data = {'education_data': list_education_employ}

    return JsonResponse(flot_data)


# 获取舆情,拼成json
def news_words(request):
    stopwords = {}.fromkeys([line.rstrip() for line in open('RiskAnalysis/static/hlt_stop_words.txt')])

    dir_judge_score = 'RiskAnalysis/static/keywords.txt'

    dict_judge_score = {}

    with open(dir_judge_score, 'r') as f:
        lines = f.readlines()
        for line in lines:
            line_split = line.strip().split(',')
            keyword = line_split[0]
            score = int(line_split[1])
            dict_judge_score[keyword] = score

    platform_id = request.session.get('platform_id')

    list_company = CompanyList.objects.filter(id=platform_id)

    company_name = list_company[0].company
    platform_name = list_company[0].platform

    # 舆情信息
    news_info_short = News.objects.filter(platform_name=platform_name)
    news_info_long = News.objects.filter(platform_name=company_name)

    company_comment = [0,0,0]
    dict_words = {}

    for item in news_info_short:
        if str(item.label) != '':
            score = 0

            seg_list = jieba.cut(item.label, cut_all=True)  # jieba分词
            for t in seg_list:
                if len(t) > 1 and t not in stopwords:
                    if t in dict_words and dict_words[t] < 100:
                        dict_words[t] += 1
                    else:
                        dict_words[t] = 1

                    if t in dict_judge_score:
                        score += dict_judge_score[t]

            if score == -1:
                company_comment[0] += 1
            elif score == 0:
                company_comment[1] += 1
            else:
                company_comment[2] += 1

    for item in news_info_long:
        if str(item.label) != '':
            score = 0

            seg_list = jieba.cut(item.label, cut_all=True)  # jieba分词
            for t in seg_list:
                if len(t) > 1 and t not in stopwords:
                    if t in dict_words and dict_words[t] < 100:
                        dict_words[t] += 1
                    else:
                        dict_words[t] = 1

                    if t in dict_judge_score:
                        score += dict_judge_score[t]

            if score == -1:
                company_comment[0] += 1
            elif score == 0:
                company_comment[1] += 1
            else:
                company_comment[2] += 1

    dict_words_sorted = sorted(dict_words.items(), key=lambda d: d[1],reverse=True)

    if len(dict_words_sorted) > 100:
        dict_words_sorted = dict_words_sorted[:100]



    flot_data = {'words': dict_words_sorted,'comments':company_comment}

    return JsonResponse(flot_data)


# 获取舆情,拼成json
def title_words(request):
    stopwords = {}.fromkeys([line.rstrip() for line in open('RiskAnalysis/static/hlt_stop_words.txt')])

    platform_id = request.session.get('platform_id')

    list_company = CompanyList.objects.filter(id=platform_id)

    company_name = list_company[0].company
    platform_name = list_company[0].platform

    # 舆情信息
    news_info_short = News.objects.filter(platform_name=platform_name)
    news_info_long = News.objects.filter(platform_name=company_name)

    dict_words = {}

    for item in news_info_short:
        if str(item.news_title) != '':
            seg_list = jieba.cut(item.news_title, cut_all=True)  # jieba分词
            for t in seg_list:
                if len(t) > 1 and t not in stopwords:
                    if t in dict_words:
                        dict_words[t] += 1
                    else:
                        dict_words[t] = 1

    for item in news_info_long:
        if str(item.news_title) != '':
            seg_list = jieba.cut(item.news_title, cut_all=True)  # jieba分词
            for t in seg_list:
                if len(t) > 1 and t not in stopwords:
                    if t in dict_words:
                        dict_words[t] += 1
                    else:
                        dict_words[t] = 1

    dict_words_sorted = sorted(dict_words.items(), key=lambda d: d[1], reverse=True)

    list_titles = []

    if len(dict_words_sorted) > 10:
        dict_words_sorted = dict_words_sorted[:10]

    for item in dict_words_sorted:
        list_titles.append({'text':item[0],'count':item[1]})

    flot_data = {'words': list_titles}

    return JsonResponse(flot_data)


# 获取裁判文书的省份,拼成json
def judgement_province(request):
    platform_id = request.session.get('platform_id')

    list_company = CompanyList.objects.filter(id=platform_id)

    company_name = list_company[0].company

    # 裁判文书信息
    law_result = Documentjudgment.objects.filter(platform_name=company_name)

    count = [0 for i in range(34)]

    for item in law_result:
        if str(item.province) != '':
            provice_code(str(item.province),count)

    flot_data = {'province_count':count}

    return JsonResponse(flot_data)

def provice_code(s,count):
    if (("澳门") in s):
        count[12]+=1
        return 'MAC'
    elif (("宁夏") in s):
        count[32]+=1
        return 'NXA'

    elif (("广东") in s):
        count[9] += 1
        return 'GUD'

    elif (("甘肃") in s):
        count[29] += 1
        return 'GAN'

    elif (("广西") in s):
        count[18] += 1
        return 'GXI'

    elif (("香港") in s):
        count[27] += 1
        return 'HKG'

    elif (("福建") in s):
        count[24] += 1
        return 'FUJ'

    elif (("北京") in s):
        count[11] += 1
        return 'BEJ'

    elif (("河南") in s):
        count[8] += 1
        return 'HEN'

    elif (("云南") in s):
        count[23] += 1
        return 'YUN'

    elif (("新疆") in s):
        count[6] += 1
        return 'XIN'

    elif (("陕西") in s):
        count[26] += 1
        return 'SHA'

    elif (("辽宁") in s):
        count[1] += 1
        return 'LIA'

    elif (("四川") in s):
        count[31] += 1
        return 'SCH'

    elif (("吉林") in s):
        count[20] += 1
        return 'JIL'

    elif (("青海") in s):
        count[28] += 1
        return 'QIH'

    elif (("海南") in s):
        count[19] += 1
        return 'HAI'

    elif (("上海") in s):
        count[4] += 1
        return 'SHH'

    elif (("河北") in s):
        count[15] += 1
        return 'HEB'

    elif (("黑龙江") in s):
        count[14] += 1
        return 'HLJ'

    elif (("山西") in s):
        count[21] += 1
        return 'SHX'

    elif (("西藏") in s):
        count[2] += 1
        return 'TIB'

    elif (("天津") in s):
        count[13] += 1
        return 'TAJ'

    elif (("贵州") in s):
        count[10] += 1
        return 'GUI'

    elif (("台湾") in s):
        count[33] += 1
        return 'TAI'

    elif (("湖北") in s):
        count[25] += 1
        return 'HUB'

    elif (("山东") in s):
        count[7] += 1
        return 'SHD'

    elif (("重庆") in s):
        count[5] += 1
        return 'CHQ'

    elif (("江西") in s):
        count[0] += 1
        return 'JXI'

    elif (("湖南") in s):
        count[22] += 1
        return 'HUN'

    elif (("浙江") in s):
        count[16] += 1
        return 'ZHJ'

    elif (("内蒙古") in s):
        count[3] += 1
        return 'NMG'

    elif (("安徽") in s):
        count[17] += 1
        return 'ANH'

    elif (("江苏") in s):
        count[30] += 1
        return 'JSU'


def salary_level(request):
    platform_id = request.session.get('platform_id')

    list_company = CompanyList.objects.filter(id=platform_id)

    company_name = list_company[0].company
    # platform_name = list_company[0].platform

    # 招聘信息
    employ_info = Employinfo.objects.filter(platform_name=company_name)

    list_salary = [0 for i in range(5)]

    for item in employ_info:

        if str(item.average_salary) != '':
            salary = float(item.average_salary)
            if salary<100:
                salary=salary*1000

            employ_num_list = re.findall(r"\d+\.?\d*",str(item.employer_num))

            if len(employ_num_list) >0:
                employ_num = int(employ_num_list[0])
            else:
                employ_num = 1

            if salary <= 5000:
                list_salary[0] += employ_num
            elif salary <= 10000:
                list_salary[1] += employ_num
            elif salary <= 15000:
                list_salary[2] += employ_num
            elif salary <= 20000:
                list_salary[3] += employ_num
            else:
                list_salary[4] += employ_num

    employ_sum = sum(list_salary)

    for i in range(len(list_salary)):
        list_salary[i] = float(list_salary[i])/employ_sum

    flot_data = {'salary_data': list_salary}

    return JsonResponse(flot_data)


def home(request):
    list_wdzj = Guotai.objects.filter(tradingdate='2017-09-30')

    list_guotai = []

    # list_wdzj = Wdzjinfo.objects.filter(enddate='2017-10-31')
    for i in range(len(list_wdzj)):
        company_list = CompanyList.objects.filter(platform=list_wdzj[i].fullname)

        if len(company_list) > 0:
            list_guotai.append({
                'guotaiid':company_list[0].id,
                'fullname':list_wdzj[i].fullname,
                'tradingvolume':list_wdzj[i].tradingvolume,
                'avereturn':list_wdzj[i].avereturn,
                'avelimtime':list_wdzj[i].avelimtime,
                'loannum':list_wdzj[i].loannum,
                'riskval':random.randint(10,100)
                })

    return render(request, 'home.html', {'list_wdzj': list_guotai})


def search(request):
    # req = json.loads(request.body)
    # req = request.POST

    # print(request.POST['company_name'])

    req = request.POST['company_name']

    list_wdzj = Guotai.objects.filter(tradingdate='2017-09-30',fullname=req)

    list_guotai = []

    if len(list_wdzj) > 0:
        company_list = CompanyList.objects.filter(platform=list_wdzj[0].fullname)

        if len(company_list) > 0:
            list_guotai.append({
                'guotaiid':company_list[0].id,
                'fullname':list_wdzj[0].fullname,
                'tradingvolume':list_wdzj[0].tradingvolume,
                'avereturn':list_wdzj[0].avereturn,
                'avelimtime':list_wdzj[0].avelimtime,
                'loannum':list_wdzj[0].loannum,
                'riskval':random.randint(10,100)
                })

    if len(list_guotai) == 0:
        list_wdzj = Guotai.objects.filter(tradingdate='2017-09-30')[:2]

        for i in range(len(list_wdzj)):
            company_list = CompanyList.objects.filter(platform=list_wdzj[i].fullname)

            if len(company_list) > 0:
                list_guotai.append({
                    'guotaiid': company_list[0].id,
                    'fullname': list_wdzj[i].fullname,
                    'tradingvolume': list_wdzj[i].tradingvolume,
                    'avereturn': list_wdzj[i].avereturn,
                    'avelimtime': list_wdzj[i].avelimtime,
                    'loannum': list_wdzj[i].loannum,
                    'riskval': random.randint(10, 100)
                })

    flot_data = {'search_result': list_guotai}

    return JsonResponse(flot_data)


def write_score_csv(law_risk_score,
                    admin_risk_score,
                    employ_risk_score,
                    news_risk_score,
                    outline_risk_score,
                    business_risk_score,
                    tax_risk_score):
    score_csv = 'RiskAnalysis/static/data.tsv'

    with open(score_csv,'w') as f:
        f.write("letter\tfrequency\n")
        f.write("司法("+str(law_risk_score)+")\t"+str(law_risk_score)+"\n")
        f.write("工商("+str(admin_risk_score)+")\t"+str(admin_risk_score)+"\n")
        f.write("招聘("+str(employ_risk_score)+")\t"+str(employ_risk_score)+"\n")
        f.write("舆情("+str(news_risk_score)+")\t"+str(news_risk_score)+"\n")
        f.write("违规("+str(outline_risk_score)+")\t"+str(outline_risk_score)+"\n")
        f.write("经营("+str(business_risk_score)+")\t"+str(business_risk_score)+"\n")
        f.write("税务("+str(tax_risk_score)+")\t"+str(tax_risk_score)+"\n")

def get_random_nums(sum,num):
    a = []
    for i in range(num-1):
        temp = random.randint(0, sum-1)
        a.append(temp)
        sum-=temp
    a.append(sum)
    return a


def write_visit_sequence_csv(law_risk_score,
                    admin_risk_score,
                    employ_risk_score,
                    news_risk_score,
                    outline_risk_score,
                    business_risk_score,
                    tax_risk_score):
    law_risk_list = get_random_nums(law_risk_score,6)
    admin_risk_list = get_random_nums(admin_risk_score,7)
    employ_risk_list = get_random_nums(employ_risk_score,4)
    news_risk_list = get_random_nums(news_risk_score,2)
    outline_risk_list = get_random_nums(outline_risk_score,4)
    business_risk_list = get_random_nums(business_risk_score,4)
    tax_risk_list = get_random_nums(tax_risk_score,4)

    sequence_list = []

    sequence_list.append('司法-破产信息,' + str(law_risk_list[0])+'\n')
    sequence_list.append('司法-司法拍卖,' + str(law_risk_list[1])+'\n')
    sequence_list.append('司法-失信公告,' + str(law_risk_list[2])+'\n')
    sequence_list.append('司法-司法曝光公告,' + str(law_risk_list[3])+'\n')
    sequence_list.append('司法-执行公告,' + str(law_risk_list[4])+'\n')
    sequence_list.append('司法-裁判文书,' + str(law_risk_list[5])+'\n')
    sequence_list.append('工商-严重违法,' + str(admin_risk_list[0])+'\n')
    sequence_list.append('工商-工商行政处罚信息,' + str(admin_risk_list[1])+'\n')
    sequence_list.append('工商-经营信息,' + str(admin_risk_list[2])+'\n')
    sequence_list.append('工商-关联信息,' + str(admin_risk_list[3])+'\n')
    sequence_list.append('工商-变更信息,' + str(admin_risk_list[4])+'\n')
    sequence_list.append('工商-工商公示信息,' + str(admin_risk_list[5])+'\n')
    sequence_list.append('工商-企业公示信息,' + str(admin_risk_list[6])+'\n')
    sequence_list.append('经营-交易规模,' + str(business_risk_list[0])+'\n')
    sequence_list.append('经营-贷款逾期率,' + str(business_risk_list[1])+'\n')
    sequence_list.append('经营-投资人投资情况,' + str(business_risk_list[2])+'\n')
    sequence_list.append('经营-贷款人贷款情况,' + str(business_risk_list[3])+'\n')
    sequence_list.append('税务-非正常户,' + str(tax_risk_list[0])+'\n')
    sequence_list.append('税务-行政处罚,' + str(tax_risk_list[1])+'\n')
    sequence_list.append('税务-欠税公告,' + str(tax_risk_list[2])+'\n')
    sequence_list.append('税务-纳税信用等级,' + str(tax_risk_list[3])+'\n')
    sequence_list.append('舆情-新闻媒体,' + str(news_risk_list[0])+'\n')
    sequence_list.append('舆情-网络论坛,' + str(news_risk_list[1])+'\n')
    sequence_list.append('违规-ICP认证,' + str(outline_risk_list[0])+'\n')
    sequence_list.append('违规-银行存管,' + str(outline_risk_list[1])+'\n')
    sequence_list.append('违规-央行处罚,' + str(outline_risk_list[2])+'\n')
    sequence_list.append('违规-银监会处罚,' + str(outline_risk_list[3])+'\n')
    sequence_list.append('招聘-管理层学历分布,' + str(employ_risk_list[0])+'\n')
    sequence_list.append('招聘-招聘学历分布,' + str(employ_risk_list[1])+'\n')
    sequence_list.append('招聘-岗位数量,' + str(employ_risk_list[2])+'\n')
    sequence_list.append('招聘-招聘人数,' + str(employ_risk_list[3])+'\n')

    sequence_csv = 'RiskAnalysis/static/vendor/sequences/visit-sequences.csv'

    with open(sequence_csv,'w') as f:
        f.writelines(sequence_list)


def platform(request):
    platform_id = request.GET.get('id')

    request.session['platform_id'] = platform_id

    list_company = CompanyList.objects.filter(id=platform_id)

    company_name = list_company[0].company
    platform_name = list_company[0].platform

    list_company_info = Company.objects.filter(platform_name=company_name)

    company_info = list_company_info[0]

    # for item in list_company_info[0]:
    # 企业基本照面信息
    # print(list_company_info[0].company_name)  # 企业名称
    # print(list_company_info[0].register_num)  # 工商注册号
    # print(list_company_info[0].credit_code)  # 社会统一信用代码,可能为空
    # 组织机构代码,暂无
    # print(list_company_info[0].economy_code)  # 行业门类代码
    # print(list_company_info[0].trade_type_code)  # 国民经济行业名称
    # print(list_company_info[0].trade_type_code_old)  # 国民经济行业名代码
    # print(list_company_info[0].register_capital)  # 注册资本(万元)
    # print(list_company_info[0].paid_in_capital)  # 实收资本(万元)
    # print(list_company_info[0].start_date)  # 开业日期
    # print(list_company_info[0].business_state)  # 经营状态
    # print(list_company_info[0].business_start_date)  # 经营起始日期
    # print(list_company_info[0].business_end_date)  # 经营截止日期
    # print(list_company_info[0].check_day)  # 最后年检日期
    # print(list_company_info[0].end_date)  # 注销日期,可能为空
    # print(list_company_info[0].revoke_date)  # 吊销日期,可能为空
    # print(list_company_info[0].company_type)  # 企业类型
    # print(list_company_info[0].general_business)  # 一般经营项目,可能为空
    # print(list_company_info[0].business_scope)  # 经营业务范围
    # print(list_company_info[0].trade_type)  # 所属行业
    # print(list_company_info[0].address)  # 地址
    # print(list_company_info[0].register_department)  # 登记机关

    # 股权冻结信息
    freeze_info_result = Changeinfo.objects.filter(platform_name=company_name)
    freeze_info_count = len(freeze_info_result)

    # 清算信息
    liquidation_info_result = Liquidation.objects.filter(platform_name=company_name)
    liquidation_info_count = len(liquidation_info_result)

    # 行政处罚信息
    admin_penalty_info_result = Administrationpenalty.objects.filter(platform_name=company_name)
    admin_penalty_info_count = len(admin_penalty_info_result)

    # 失信公告
    fail_credit_info_result = Failcredit.objects.filter(company_name=company_name)
    fail_credit_info_count = len(fail_credit_info_result)

    # 执行公告统计
    ducument_execute_info_result = Documentexecute.objects.filter(platform_name=company_name)
    document_execute_info_count = len(ducument_execute_info_result)

    # 判决文书类型信息
    law_result = Documentjudgment.objects.values("platform_name", "case_brief").annotate(
        case_count=Count("case_brief")).filter(platform_name=company_name)

    list_law_type = []

    for item in law_result:
        if item['case_brief'] != '':
            list_law_type.append({'case_brief': item['case_brief'], 'case_count': item['case_count']})

    list_law_info = Documentjudgment.objects.filter(platform_name=company_name)

    # 裁判文书统计
    document_judgement_info_count = len(list_law_info)

    # 判决公告信息
    # document_execute_info = Documentexecute.objects.filter(platform_name=company_name)[:10]

    # 案件时间线
    dict_month = {
        '01': 'Jan',
        '02': 'Feb',
        '03': 'Mar',
        '04': 'Apr',
        '05': 'May',
        '06': 'Jun',
        '07': 'Jul',
        '08': 'Aug',
        '09': 'Sep',
        '10': 'Oct',
        '11': 'Nov',
        '12': 'Dec'
    }

    dict_cases = {}

    # case_num=0

    for item in list_law_info:
        # if len(item.end_date) > 1:
        date_split = str(item.end_date).split("-")
        if len(date_split) == 3 and item.case_brief != '':
            year = date_split[0]
            month = date_split[1]
            day = date_split[2]

            if year in dict_cases:
                if len(dict_cases[year]) < 2:
                    dict_cases[year].append(
                        {'day': day, 'month': dict_month[month], 'title': item.title, 'brief': item.case_brief})
            else:
                dict_cases[year] = [
                    {'day': day, 'month': dict_month[month], 'title': item.title, 'brief': item.case_brief}]

            # case_num += 1
            #
            # if case_num > 5:
            #     break

    dict_cases_sorted = sorted(dict_cases.items(), key=lambda d: d[0])

    # 企业变更信息
    change_info = Changeinfo.objects.filter(platform_name=company_name)
    change_info_count = len(change_info)

    # 纳税信用等级
    tax_credit_info = Taxcreditinfo.objects.filter(platform_name=company_name)
    tax_credit_info_count = len(tax_credit_info)

    # 欠税信息
    tax_info = Taxinfo.objects.filter(platform_name=company_name)
    tax_info_count = len(tax_info)

    # 涉税处罚信息
    tax_penalty_info = Taxpenalty.objects.filter(platform_name=company_name)
    tax_penalty_info_count = len(tax_penalty_info)

    # 纳税非正常户
    abnormal_tax_info = Abnormaltaxinfo.objects.filter(platform_name=company_name)
    abnormal_tax_info_count = len(abnormal_tax_info)

    # 经营信息
    # wdzj_info = Wdzjinfo.objects.filter(platform_name=platform_name, startdate__lt=date(2017, 10, 10))
    wdzj_info = Guotai.objects.filter(fullname=platform_name)

    # 招聘信息
    employ_info = Employinfo.objects.filter(platform_name=company_name)

    # for item in employ_info:
    #     print(item.title,item.salary,item.startdate)

    # ICP备案信息
    icp_info = Icp.objects.filter(company_name=company_name)
    icp_info_count = len(icp_info)

    # 银行存管信息
    bank_depository_info = Bankdepository.objects.filter(company_name=company_name)
    bank_depository_info_count = len(bank_depository_info)

    # 舆情信息
    news_info_short = News.objects.filter(platform_name=platform_name)
    news_info_long = News.objects.filter(platform_name=company_name)

    news_info = news_info_short | news_info_long

    news_info = news_info

    # 随机生成7个维度得分
    law_risk_score = random.randint(10, 100)
    admin_risk_score = random.randint(10, 100)
    business_risk_score = random.randint(10, 100)
    tax_risk_score = random.randint(10, 100)
    news_risk_score = random.randint(10, 100)
    outline_risk_score = random.randint(10, 100)
    employ_risk_score = random.randint(10, 100)
    total_risk_score = random.randint(10, 100)

    write_score_csv(law_risk_score,
                    admin_risk_score,
                    employ_risk_score,
                    news_risk_score,
                    outline_risk_score,
                    business_risk_score,
                    tax_risk_score)

    guotai_data(platform_id)

    write_visit_sequence_csv(law_risk_score,
                    admin_risk_score,
                    employ_risk_score,
                    news_risk_score,
                    outline_risk_score,
                    business_risk_score,
                    tax_risk_score)

    return render_to_response('platform.html', {'company_info': company_info,
                                                'law_type_info': list_law_type,
                                                'change_info': change_info[:10],
                                                'icp_info': icp_info,
                                                'bank_depository_info': bank_depository_info,
                                                'case_info': dict_cases_sorted,
                                                'list_law_info': list_law_info[:10],
                                                'wdzj_info': wdzj_info[:10],
                                                'tax_credit_info': tax_credit_info[:10],
                                                'tax_info': tax_info[:10],
                                                'tax_penalty_info': tax_penalty_info[:10],
                                                'abnormal_tax_info': abnormal_tax_info[:10],
                                                'news_info': news_info[:10],
                                                'law_risk_score': law_risk_score,
                                                'admin_risk_score': admin_risk_score,
                                                'business_risk_score': business_risk_score,
                                                'tax_risk_score': tax_risk_score,
                                                'news_risk_score': news_risk_score,
                                                'outline_risk_score': outline_risk_score,
                                                'employ_risk_score': employ_risk_score,
                                                'total_risk_score': total_risk_score,
                                                'platform_name':platform_name,
                                                'freeze_info_count':freeze_info_count,
                                                'liquidation_info_count':liquidation_info_count,
                                                'admin_penalty_info_count':admin_penalty_info_count,
                                                'change_info_count':change_info_count,
                                                'fail_credit_info_count':fail_credit_info_count,
                                                'document_execute_info_count':document_execute_info_count,
                                                'document_judgement_info_count':document_judgement_info_count,
                                                'tax_info_count':tax_info_count,
                                                'tax_penalty_info_count':tax_penalty_info_count,
                                                'tax_credit_info_count':tax_credit_info_count,
                                                'abnormal_tax_info_count':abnormal_tax_info_count,
                                                'icp_info_count':icp_info_count,
                                                'bank_depository_info_count':bank_depository_info_count,
                                                'employ_info':employ_info[:10]
                                                })
