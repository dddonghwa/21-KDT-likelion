# 네이버 금융 정보 가져오기

Top 종목-상한가에 있는 정보를 xlsx 파일로 정리하는 실습입니다.


```python
from bs4 import BeautifulSoup
from urllib.request import urlopen
import pandas as pd

url = 'https://finance.naver.com/sise/'
page = urlopen(url)
soup = BeautifulSoup(page, 'html.parser')

# 한 개만 (top1)
top = soup.find("table", summary="탑종목 상한가 리스트")
nlist = len(top.find_all("tr"))-4 # 종목 갯수

com1 = top.find_all("tr")[2]
numtag = com1.find_all("td",class_="number")
c2 = numtag[0].text # 연속
c3 = numtag[1].text # 누적
c5 = numtag[2].text # 현재가
c8 = numtag[5].text # 거래량
c9 = numtag[6].text # 시가
c10 = numtag[7].text # 고가
c11 = numtag[8].text # 저가

c4 = com1.find_all("a")[0].text # 종목명

redtag = com1.find_all("span", class_="tah p11 red01")
c6 = redtag[0].text.strip() # 전일비
c7 = redtag[1].text.strip() # 등락률

# print(com1)
```


```python
from bs4 import BeautifulSoup
from urllib.request import urlopen
import pandas as pd

url = 'https://finance.naver.com/sise/'
page = urlopen(url)
soup = BeautifulSoup(page, 'html.parser')

# 여러개 (top1~topn)
top = soup.find("table", summary="탑종목 상한가 리스트")
nlist = len(top.find_all("tr"))-4

c1 = list(range(1,1+nlist)) # 순위
c2 = [] # 연속
c3 = [] # 누적
c4 = [] # 종목명
c5 = [] # 현재가
c6 = [] # 전일비
c7 = [] # 등락률
c8 = [] # 거래량
c9 = [] # 시가
c10 = [] # 고가
c11 = [] # 저가

for idx in range(2,2+nlist):
    com = top.find_all("tr")[idx]
#     print(com)
    numtag = com.find_all("td",class_="number")
    c2.append(numtag[0].text) # 연속
    c3.append(numtag[1].text) # 누적
    c5.append(numtag[2].text) # 현재가
    c8.append(numtag[5].text) # 거래량
    c9.append(numtag[6].text) # 시가
    c10.append(numtag[7].text) # 고가
    c11.append(numtag[8].text) # 저가

    c4.append(com.find_all("a")[0].text) # 종목명

    redtag = com.find_all("span", class_="tah p11 red01")
    c6.append(redtag[0].text.strip()) # 전일비
    c7.append(redtag[1].text.strip()) # 등락률

dat = {"순위":c1, "연속":c2, "누적":c3, "종목명":c4,
       "현재가":c5, "전일비":c6, "등락률":c7, "거래량":c8,
       "시가":c9, "고가":c10, "저가":c11}

dat = pd.DataFrame(dat)
dat.to_excel("top종목_상한가.xlsx", index=False)
```


```python

```
