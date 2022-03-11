#pyinstaller --onefile --icon ico.ico --noconsole main.py --name scoop-sd
import requests
import os
from bs4 import BeautifulSoup as bs
import re
import argparse
from prettytable import PrettyTable

aparser = argparse.ArgumentParser()
aparser.add_argument('search', nargs='?', default='')
search = aparser.parse_args()
def parser():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:97.0) Gecko/20100101 Firefox/97.0',
        'Accept': '*/*',
        'Accept-Language': 'uk-UA,uk;q=0.8,en-US;q=0.5,en;q=0.3',
        'Accept-Encoding': 'gzip, deflate, br',
        'Referer': 'https://scoopsearch.github.io/',
        'api-key': 'DC6D2BBE65FC7313F2C52BBD2B0286ED',
        'Origin': 'https://scoopsearch.github.io',
        'DNT': '1',
        'Connection': 'keep-alive',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'cross-site',
        'TE': 'trailers',
    }

    params = (
        ('api-version', '2020-06-30'),
    )

    json_data = {
        'count': True,
        'search': f'{search.search}',
        'searchMode': 'all',
        'filter': '',
        'orderby': 'search.score() desc, Metadata/OfficialRepositoryNumber desc, NameSortable asc',
        'skip': 0,
        'top': 20,
        'select': 'Id,Name,NamePartial,NameSuffix,Description,Homepage,License,Version,Metadata/Repository,Metadata/FilePath,Metadata/AuthorName,Metadata/OfficialRepository,Metadata/RepositoryStars,Metadata/Committed,Metadata/Sha',
        'highlight': 'Name,NamePartial,NameSuffix,Description,Version,License,Metadata/Repository,Metadata/AuthorName',
        'highlightPreTag': '<mark>',
        'highlightPostTag': '</mark>',
    }

    r = requests.post('https://scoopsearch.search.windows.net/indexes/apps/docs/search', headers=headers, params=params, json=json_data)
    soup = bs(r.text, "lxml")
    #print(soup)
    pac_name = re.compile(r'"NameSuffix":"(.*?)"', re.MULTILINE | re.DOTALL)
    packets_names = soup.find_all(text=pac_name)
    pac_repository = re.compile(r'"Repository":"(.*?)"', re.MULTILINE | re.DOTALL)
    packets_repository = soup.find_all(text=pac_repository)
    table = PrettyTable()
    table.field_names = ['Number','App Name','Bucket']
    array_app = []
    array_bucket = []
    i = -1
    for name in packets_names:
        i += 1
        i_number = f'{i})'
        rep_name = pac_repository.search(name.text).group(1).replace('/',' ').split()[-1]
        rep_url = pac_repository.search(name.text).group(1).replace('/',' ').replace(' ','/').split()[-1]
        bucket = f'scoop bucket add {rep_name} {rep_url}'
        app_name = pac_name.search(name.text).group(1)
        table.add_row([i_number, app_name, bucket])
        array_bucket.append(bucket)
        array_app.append(app_name)
    print(table)
    func_select = input('To install the app, type \'i\'.\nTo add a repository, type \'b\'.\nTo exit, type \'q\'.\n(Select)>> ')
    if func_select == 'q':
        exit()
    if func_select == 'i':
        app_number = input('Select the application number to install.\n(Install_app)>> ')
        app_install = "scoop install " + array_app[int(app_number)]
        os.system(app_install)
    if func_select == 'b':
        bucket_number = input('Select the bucket number to add it.\n(Add_bucket)>> ')
        bucket_add = array_bucket[int(bucket_number)]
        os.system(bucket_add)
parser()




