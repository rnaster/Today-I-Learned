# programmers - 2019 kakao blind 매칭점수
import re
def solution(word, pages):
    heads = re.compile(r'<head>(.*)</head>', re.DOTALL)
    urls = re.compile(r'<meta.*"(https://.*?)"/>')
    hrefs = re.compile(r'<a href="(https://.*?)">')
    info = {}
    url_lst = [''] * len(pages)
    word = word.lower()
    for i, page in enumerate(pages):
        page = page.lower()
        head = heads.findall(page)[0]
        url = urls.findall(head)[0]
        url_lst[i] = url
        info[url] = [[], 0, 0]
        info[url][2] = re.sub(r'[^a-z]+', ' ', page).split().count(word)
    for i, page in enumerate(pages):
        url = url_lst[i]
        for href in hrefs.findall(page):
            info[url][1] += 1
            if href in info:
                info[href][0].append(url)
    ans = 0
    score = 0
    for i, url in enumerate(url_lst):
        tmp = info[url][2]
        tmp += sum(info[h][2] / info[h][1] for h in info[url][0])
        if score < tmp:
            ans = i
            score = tmp
    return ans
exit()
