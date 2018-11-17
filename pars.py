import requests
from bs4 import BeautifulSoup
import re


def find_numder(url_list):
    for url in url_list:
        page = requests.get(url)
        soup = BeautifulSoup(page.text, 'html.parser')

        number_template = re.compile(r"(\d{1}[\s-]\d{3}[\s-]\d{3}[\s-]\d{2}[\s-]\d{2})|(\d{11})|(\d{1}[\s-][\(]\d{3}[\)][\s-]\d{3}[\s-]\d{2}[\s-]\d{2})")
        res = re.findall(number_template, soup.prettify())
        # print(res[0])
        print("from url: ", url)
        answer = set()
        for r in res:
            for i in r:
                if i != "":
                    tmp = re.sub(r"\D", "", i)
                    if len(tmp) == 5:
                        tmp = "8495" + tmp
                    if tmp.startswith("7"):
                        tmp = "8" + tmp[1:]
                    answer.add(tmp)
        for number in answer:
            print(number)


if __name__ == "__main__":
    find_numder(["https://hands.ru/company/about/",
                 "https://repetitors.info/"])
