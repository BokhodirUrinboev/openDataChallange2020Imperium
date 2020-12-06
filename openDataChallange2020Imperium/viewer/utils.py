import requests

ACCESS_KEY = '?access_key=95a9fa57c856b26c903ea896335de9b1'
MAIN_URL = 'http://data.gov.uz/uz/api/v1/json'
DATASETS = '/dataset/'


DATASET_ID = [13894, 13892, 13891, 13890, 13888, 13887, 13886, 13885, 13884, 13883, 13882, 13881, 13880, 13879]
VERSION_CHECK = '/version'
VERSION_ID = 29894
INNER_CONTENT = '/' +  str(VERSION_ID)
TITLES = []



def get_and_write_title(title_id):
    URL = MAIN_URL + DATASETS + str(title_id) + ACCESS_KEY
    r = requests.get(url=URL)
    data = r.json()
    return data['structure']['meta'], data['title']


def get_version_id(title_id):
    URL = MAIN_URL + DATASETS + str(title_id) + VERSION_CHECK + ACCESS_KEY
    r = requests.get(url=URL)
    data = r.json()
    return data[0]['id']


def data_content(title_id, version_id):
    URL = MAIN_URL + DATASETS + str(title_id) + VERSION_CHECK + '/' + str(version_id) + ACCESS_KEY
    r = requests.get(url=URL)
    data = r.json()
    return data


def take_post(DATASET_ID):
    data_dict = {}
    list_titles = []
    data_title, title = get_and_write_title(DATASET_ID)
    date_title_id = []
    # print(title)
    print('____________________________________________')
    str_title = ''
    for i in range(0, len(data_title)):
        str_title = str_title + data_title[i]['title_uz'].rstrip("\n") + "|"
        TITLES.append(data_title[i]['title_uz'])
        date_title_id.append(data_title[i]['code'])
        data_dict[data_title[i]['title_uz']] = []
    # print(TITLES)
    # print(data_dict)
    # print(str_title)
    print('=============================================')
    version_id = get_version_id(DATASET_ID)
    data = data_content(DATASET_ID, version_id)
    # print(data)
    for i in range(0, len(data), len(date_title_id)):
        # printable = ""
        # print(data[i]['G1'])
        list_titles.append(data[i]['g1'])
        # for j in range(0, len(date_title_id)):
        #     data_dict[TITLES[j]].append(data[i][date_title_id[j]])
        #     printable = printable + data[i][date_title_id[j]] + ' | '
        # print(printable)
    print('____________________________________________')
    return list_titles


# data_title, list_title = take_post(13716)
