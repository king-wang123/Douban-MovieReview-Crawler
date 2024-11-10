import requests
from lxml import etree
import re
import time as t
import random
import os
import json
from statistic import MovieReviewStatistic

def get_html(url):
    cookies = {
    'bid': '092ZTg-TPCU',
    'douban-fav-remind': '1',
    'll': '"118282"',
    '_pk_id.100001.4cf6': '42fc2447fd2ea200.1728218982.',
    '__yadk_uid': 'gRYj5Ab7OAmlsu5GxBHhSnkElAWLFGAE',
    '_vwo_uuid_v2': 'D205B89730FF40BBB33EAB0F6345DA9F9|36efd1c6e2c4e06a6689fb1f5bd5b31e',
    '_gid': 'GA1.2.711515994.1731206145',
    'Hm_lvt_19fc7b106453f97b6a84d64302f21a04': '1731206149',
    'HMACCOUNT': '79001B93EB2FDDAE',
    'Hm_lpvt_19fc7b106453f97b6a84d64302f21a04': '1731206183',
    '_ga_PRH9EWN86K': 'GS1.2.1731206150.1.1.1731206183.0.0.0',
    '_ga': 'GA1.1.249836588.1731206144',
    '_ga_Y4GN1R87RG': 'GS1.1.1731206144.1.1.1731206185.0.0.0',
    '__utmc': '30149280',
    '__utmc': '223695111',
    '_pk_ref.100001.4cf6': '%5B%22%22%2C%22%22%2C1731217521%2C%22https%3A%2F%2Fwww.google.com%2F%22%5D',
    '_pk_ses.100001.4cf6': '1',
    'dbcl2': '"224267170:h5XlMnm8oz8"',
    'ck': 'OgWH',
    'ap_v': '0,6.0',
    '__utma': '30149280.1936358260.1727594394.1731209284.1731217534.5',
    '__utmz': '30149280.1731217534.5.4.utmcsr=open.weixin.qq.com|utmccn=(referral)|utmcmd=referral|utmcct=/',
    '__utma': '223695111.265593543.1728218983.1731209303.1731217534.4',
    '__utmb': '223695111.0.10.1731217534',
    '__utmz': '223695111.1731217534.4.3.utmcsr=open.weixin.qq.com|utmccn=(referral)|utmcmd=referral|utmcct=/',
    '__utmt_t1': '1',
    '__utmb': '30149280.3.8.1731217534',
    'push_noty_num': '0',
    'push_doumail_num': '0',
    'RT': 's=1731217544956&r=https%3A%2F%2Fmovie.douban.com%2Fsubject%2F36331304%2Fcomments%3Fstart%3D100%26limit%3D40%26status%3DP%26sort%3Dnew_score',
    }

    headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en,zh-CN;q=0.9,zh;q=0.8',
    'cache-control': 'max-age=0',
    # 'cookie': 'bid=092ZTg-TPCU; douban-fav-remind=1; ll="118282"; _pk_id.100001.4cf6=42fc2447fd2ea200.1728218982.; __yadk_uid=gRYj5Ab7OAmlsu5GxBHhSnkElAWLFGAE; _vwo_uuid_v2=D205B89730FF40BBB33EAB0F6345DA9F9|36efd1c6e2c4e06a6689fb1f5bd5b31e; _gid=GA1.2.711515994.1731206145; Hm_lvt_19fc7b106453f97b6a84d64302f21a04=1731206149; HMACCOUNT=79001B93EB2FDDAE; Hm_lpvt_19fc7b106453f97b6a84d64302f21a04=1731206183; _ga_PRH9EWN86K=GS1.2.1731206150.1.1.1731206183.0.0.0; _ga=GA1.1.249836588.1731206144; _ga_Y4GN1R87RG=GS1.1.1731206144.1.1.1731206185.0.0.0; __utmc=30149280; __utmc=223695111; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1731217521%2C%22https%3A%2F%2Fwww.google.com%2F%22%5D; _pk_ses.100001.4cf6=1; dbcl2="224267170:h5XlMnm8oz8"; ck=OgWH; ap_v=0,6.0; __utma=30149280.1936358260.1727594394.1731209284.1731217534.5; __utmz=30149280.1731217534.5.4.utmcsr=open.weixin.qq.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utma=223695111.265593543.1728218983.1731209303.1731217534.4; __utmb=223695111.0.10.1731217534; __utmz=223695111.1731217534.4.3.utmcsr=open.weixin.qq.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utmt_t1=1; __utmb=30149280.3.8.1731217534; push_noty_num=0; push_doumail_num=0; RT=s=1731217544956&r=https%3A%2F%2Fmovie.douban.com%2Fsubject%2F36331304%2Fcomments%3Fstart%3D100%26limit%3D40%26status%3DP%26sort%3Dnew_score',
    'priority': 'u=0, i',
    'referer': 'https://open.weixin.qq.com/',
    'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'cross-site',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
}
    return requests.get(url=url, cookies=cookies, headers=headers).text

def get_movie_id(movie_name):
    url = f'https://search.douban.com/movie/subject_search?search_text={movie_name}'
    
    response_text = get_html(url)
    # 使用正则表达式提取 "id" 和 "title"
    pattern = r'"id":\s*(\d+).*?"title":\s*"([^"]+)"'

    matches = re.findall(pattern, response_text)

    # 将结果转换为字典
    result = {int(match[0]): match[1].encode().decode('unicode_escape') for match in matches}

    return result

def get_movie_review_by_url(url):
    comments_dict = []

    tree = etree.HTML(get_html(url))

    comment_list = tree.xpath('//div[@class="comment-item "]')
    if len(comment_list) == 0:
        return comments_dict
    
    for comment_div in comment_list:
        try:
            name = comment_div.xpath('.//span[@class="comment-info"]/a/text()')[0].strip()
        except:
            name = ''
        try:
            content = comment_div.xpath('.//p[@class=" comment-content"]/span/text()')[0].strip()
        except:
            continue
        upvote = comment_div.xpath('.//span[@class="votes vote-count"]/text()')[0].strip()
        time = comment_div.xpath('.//span[@class="comment-time "]/@title')[0]
        location = comment_div.xpath('.//span[@class="comment-location"]/text()')[0].strip()
        
        try:
            star_attribute = comment_div.xpath('.//span[contains(@class,"rating")]/@class')[0]
            stars = re.search(r'\d+', star_attribute).group()[0]
        except:
            stars = 0

        comments_dict.append({
            'name': name,
            'content': content,
            'upvote': upvote,
            'time': time,
            'location': location,
            'stars': stars
        })

    return comments_dict

def get_movie_review(movie_id):
    comments_dict = []
    page = 0
    while True:
        url = f'https://movie.douban.com/subject/{movie_id}/comments?start={page}&limit=50&sort=new_score&status=P'
        print(url)

        tmp_comments_dict = get_movie_review_by_url(url)
        if len(tmp_comments_dict) == 0:
            break
        comments_dict.extend(tmp_comments_dict)

        page += 50
        t.sleep(random.uniform(1, 3)) # 随机等待时间是0.5秒和1秒之间的一个小数

    print("==================影评获取完毕===================")
    print(f'共获取{len(comments_dict)}条影评')
    return comments_dict
    
def save_movie_review(movie_name, comments_dict):
    dir_path = f'./data/{movie_name}'
    os.makedirs(dir_path, exist_ok=True)
    with open(os.path.join(dir_path, 'comments.json'), 'w', encoding='utf-8') as f:
        json.dump(comments_dict, f, ensure_ascii=False, indent=4)

def main():
    movie_name = input("请输入电影名称：")
    movie_id_dict = get_movie_id(movie_name)
    
    for index, movie_id in enumerate(movie_id_dict):
        print(f"{index+1}. {movie_id_dict[movie_id]}")
    
    movie_index = int(input("请输入电影ID："))
    movie_id = list(movie_id_dict.keys())[movie_index-1]
    
    comments_dict = get_movie_review(movie_id)
    save_movie_review(movie_name, comments_dict)
    
    movie_review_statistic = MovieReviewStatistic(movie_name, comments_dict)
    movie_review_statistic.stastic_star()
    movie_review_statistic.statistic_comment()
    

if __name__ == '__main__':
    main()