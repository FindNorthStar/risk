# -*- coding: UTF-8 -*-

import random

from django.core.serializers import json
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from RiskAnalysis.models import *


def platform_region(request):
    list_platform = Platform.objects.all()

    dict_region = {}

    for item in list_platform:
        if item.region not in dict_region:
            dict_region[item.region] = [item.name]
        else:
            dict_region[item.region].append(item.name)

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
            for i in range(1,length):
                branch_platorm = list_business[i]
                response_data += '{"source":"' + center_platform + \
                                 '","target":"' + branch_platorm + \
                                 '","region":"' + region + '"},\n'

            # for i in range(length - 1):
            #     for j in range(i + 1, length):
            #         name_i = list_business[i]
            #         name_j = list_business[j]
            #         if random.randint(0, 100) % 5 != 0 and j > 1 and i > 0:
            #             pass
            #         else:
            #             response_data += '{"source":"' + name_i + \
            #                              '","target":"' + name_j + \
            #                              '","region":"' + region + '"},\n'

    response_data = response_data[:-2] + '\n'

    response_data += ']\n'

    return HttpResponse(response_data)


def home(request):
    list_wdzj = Wdzjinfo.objects.filter(enddate='2017-10-31')
    #
    # for item in list_platform:
    #     print(item.name, item.region)
    return render(request, 'home.html',{'list_wdzj': list_wdzj})

def platform(request):
    # list_platform = Platform.objects.all()
    #
    # for item in list_platform:
    #     print(item.name, item.region)
    return render(request, 'platform.html')
