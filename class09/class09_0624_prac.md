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
# dat.to_csv("top종목_상한가.csv", index=False)
```


```python
dat
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>순위</th>
      <th>연속</th>
      <th>누적</th>
      <th>종목명</th>
      <th>현재가</th>
      <th>전일비</th>
      <th>등락률</th>
      <th>거래량</th>
      <th>시가</th>
      <th>고가</th>
      <th>저가</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>1</td>
      <td>6</td>
      <td>유유제약2우B</td>
      <td>37,600</td>
      <td>8,650</td>
      <td>+29.88%</td>
      <td>35,873</td>
      <td>37,600</td>
      <td>37,600</td>
      <td>37,600</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>2</td>
      <td>2</td>
      <td>솔고바이오</td>
      <td>993</td>
      <td>229</td>
      <td>+29.97%</td>
      <td>4,384,028</td>
      <td>993</td>
      <td>993</td>
      <td>993</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>1</td>
      <td>3</td>
      <td>한세엠케이</td>
      <td>9,490</td>
      <td>2,190</td>
      <td>+30.00%</td>
      <td>6,461,146</td>
      <td>7,460</td>
      <td>9,490</td>
      <td>7,300</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>1</td>
      <td>1</td>
      <td>타임기술</td>
      <td>2,665</td>
      <td>345</td>
      <td>+14.87%</td>
      <td>1,002</td>
      <td>2,320</td>
      <td>2,665</td>
      <td>2,320</td>
    </tr>
  </tbody>
</table>
</div>




```python

```
