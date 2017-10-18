import os
import json
from .api import api

RESULT_DIRECTORY = '__results__/crawling'

def preprocess_tourspot_visitor(item):
    # addrCd
    del item['addrCd']

    # rnum
    del item['rnum']

    # gungu
    del item['gungu']

    # 내국인수
    if 'csNatCnt' not in item:
        item['count_locals'] = 0
    else:
        item['count_locals'] = item['csNatCnt']
        del item['csNatCnt']

    # 외국인 수
    if 'csForCnt' not in item:
        item['count_foreigner'] = 0
    else:
        item['count_foreigner'] = item['csForCnt']
        del item['csForCnt']

    # 관광지 이름
    if 'resNm' not in item:
        item['tourist_spot'] = 0
    else:
        item['tourist_spot'] = item['resNm']
        del item['resNm']

    # 년월
    if 'ym' not in item:
        item['date'] = 0
    else:
        item['date'] = item['ym']
        del item['ym']

    # 시도
    if 'sido' not in item:
        item['district'] = 0
    else:
        item['district'] = item['sido']
        del item['sido']


def crawlling_tourspot_visitor(
        district,
        start_year,
        end_year):
    results = []
    for year in range(start_year, end_year+1):
        for month in range(1, 13):
            for items in api.pd_fetch_tourspot_visitor(
                    district1=district,
                    year=year,
                    month=month):
                for item in items:
                    preprocess_tourspot_visitor(item)

                results += items

    # save data to file
    filename = '%s/%s_tourspot_%s_%s.json' % (RESULT_DIRECTORY, district, start_year, end_year)
    with open(filename, 'w', encoding='utf-8') as outfile:
        json_string = json.dumps(results, indent=4, sort_keys=True, ensure_ascii=False)
        outfile.write(json_string)


if not os.path.exists(RESULT_DIRECTORY):
    os.makedirs(RESULT_DIRECTORY)
