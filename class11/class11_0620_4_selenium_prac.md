수업에서 __selenium__ 을 이용하여 정보를 가져오는 방법에 대해서 배웠습니다.  
동일한 정보를 `id`나 `name`, `xpath`,`link_text` 등과 같이 다양한 방식으로 가져오는 것을 연습해보았습니다. 

### myStudy 1 에서는...
첫번째 강의 페이지에서 목록의 내용을 가져옵니다.   
`selenium`의 `tag_name`과 `xpath`, `partial_link_text`, `css_selector`을 이용하였습니다. 

### myStudy 2 에서는...
두번째 강의 페이지에서도 목록의 내용을 가져옵니다.  
`selenium`의 `class_name`, `xpath`, `css_selector`를 이용하였습니다.

### myStudy 3 에서는...
`selenium`과 `BeautifulSoup`을 이용해서 다음 부동산에서 코스피 시가총액상위 정보 가져오고 csv 파일로 정리합니다. csv 파일 이름은 *daum_market_cap.csv*입니다.

#### selenium으로 정보 가져오는 방식

- find_element_by_id : 속성 id로 가져오기
- find_element_by_name : 속성 name으로 가져오기
- find_element_by_xpath : 고유식별자 xpath로 가져오기
- find_element_by_link_text : 속성 text으로 가져오기
- find_element_by_partial_link_text : 속성 text 내용 중 일부로 가져오기
- find_element_by_tag_name : tag 종류로 가져오기
- find_element_by_class_name : 속성 class로 가져오기
- find_element_by_css_selector : 특정 경로로 가져오기 (BeautifulSoup.select와 비슷)


## myStudy 1 : selenium 이용해서 원하는 정보 가져오기 - page 1
페이지1 이미지 ↓  

![image-2.png](attachment:image-2.png)


```python
# 지금은 selenium을 연습하지만 나중에 selenium+beautifulsoup을 사용할 것이기 때문에 기본 틀을 연습해놓는 것이 좋겠다.
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import lxml

url = 'https://pythonstart.github.io/web/'
start = time.time()
driver = webdriver.Chrome('./chromedriver')
driver.get(url)
```

### 목록(text) 가져오기
1) tag_name으로 가져오기


```python
sel_a = driver.find_elements_by_tag_name("a")
for idx, one in enumerate(sel_a) :
    print(one.text)
```

    01. 제목 가져오기(title)
    02. 텍스트 가져오기(p)
    03. 링크 가져오기(a)
    04. 이미지 정보 가져오기(img)
    05. 리스트 정보 가져오기(ul,ol)
    06. id를 활용한 정보 획득
    07. class를 활용한 정보 획득
    08. 하나의 이미지 다운로드
    09. 여러개의 이미지 다운로드
    10. 랭킹 정보 가져오기(웹 크롤링)


2) xpath로 가져오기


```python
"""
xpath = '/html/body/ul/a[1]'
xpath = '/html/body/ul/a[2]' ...
"""

for i in range(1,11):
    xpath_basic = f'/html/body/ul/a[{i}]'
    sel_xpath = driver.find_element_by_xpath(xpath_basic)
    print(sel_xpath.text)
```

    01. 제목 가져오기(title)
    02. 텍스트 가져오기(p)
    03. 링크 가져오기(a)
    04. 이미지 정보 가져오기(img)
    05. 리스트 정보 가져오기(ul,ol)
    06. id를 활용한 정보 획득
    07. class를 활용한 정보 획득
    08. 하나의 이미지 다운로드
    09. 여러개의 이미지 다운로드
    10. 랭킹 정보 가져오기(웹 크롤링)


3) partial_link_text로 가져오기


```python
for i in range(1, 10) :
    basic_text = f'0{i}'
    sel_text = driver.find_element_by_partial_link_text(basic_text)
    print(sel_text.text)
```

    01. 제목 가져오기(title)
    02. 텍스트 가져오기(p)
    03. 링크 가져오기(a)
    04. 이미지 정보 가져오기(img)
    05. 리스트 정보 가져오기(ul,ol)
    06. id를 활용한 정보 획득
    07. class를 활용한 정보 획득
    08. 하나의 이미지 다운로드
    09. 여러개의 이미지 다운로드


4) css selector로 가져오기


```python
sel_css = driver.find_elements_by_css_selector("body ul a")
for idx, one in enumerate(sel_css):
    print(one.text)
```

    01. 제목 가져오기(title)
    02. 텍스트 가져오기(p)
    03. 링크 가져오기(a)
    04. 이미지 정보 가져오기(img)
    05. 리스트 정보 가져오기(ul,ol)
    06. id를 활용한 정보 획득
    07. class를 활용한 정보 획득
    08. 하나의 이미지 다운로드
    09. 여러개의 이미지 다운로드
    10. 랭킹 정보 가져오기(웹 크롤링)


## myStudy 2 : selenium으로 원하는 정보 가져오기 - page 2
페이지2 이미지 ↓  
![image.png](attachment:image.png)


```python
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import lxml

# 객체 할당
start = time.time()
driver = webdriver.Chrome("./chromedriver")
driver
```




    <selenium.webdriver.chrome.webdriver.WebDriver (session="94b3d9c194be0d0cef2cbb31d3aaaf87")>




```python
# 웹페이지 띄우기
url = 'https://ldjwj.github.io/00_SBA01_BigData/05_HTML/idx_lec_list'
driver.get(url)
```

### contents 내용(text) 가져오기
1) class_name으로 가져오기


```python
sel_class = driver.find_elements_by_class_name("cell")
for idx, one in enumerate(sel_class):
    if idx%4 == 2:
        print(one.text)
```

    Content
    R 기본 전체(전 수업 링크)
    통계기본이해하기(1)
    가설검정이해(1)
    통계기본이해_실습(1)-통계가설검정
    통계기본이해_실습(1)-통계가설검정
    회귀분석이해(1)
    첫번째 모델 만들기
    회귀 모델 실습(1)-mtcars
    회귀 모델 실습(2)-Boston 집값 예측
    회귀 모델 실습(3) - 캐글 데이터-집값 예측
    로지스틱 회귀 모델 실습(1) - 인디언 암 예측
    의사결정트리 기본 이해(1)
    의사결정트리 실습(1)
    의사결정트리 실습(2)
    데이터 탐색 - Boston 집값
    텍스트 마이닝 시작하기
    KoNLP를 패키지를 활용한 텍스트 분석(1)
    텍스트 감정 분석(1)
    TFIDF 이해하기(1)
    R과 MySQL 연동 환경 만들기
    R과 MySQL 연동 실습하기
    데이터 시각화 기본(1)
    데이터 시각화 기본(2)
    데이터 시각화 기본(3)
    데이터 시각화 기본(4)
    데이터 시각화 활용(5)
    데이터 시각화 참고자료(1)
    데이터 시각화 참고자료(2)


2) xpath로 가져오기
- 단점 : 몇번째 인덱스가 끝인지 직접 세어야 한다.


```python
'''
xpath0 = /html/body/div/div/div/div/div[1]/div[3]
xpath1 = /html/body/div/div/div/div/div[2]/div[3]
'''
### 1) 
xpath_base = '/html/body/div/div/div/div/div/div[3]'
sel_xpath = driver.find_elements_by_xpath(xpath_base)
for idx, one in enumerate(sel_xpath):
    print(one.text)

### 2)    
# for i in range(1, 11):
#     xpath_base = f'/html/body/div/div/div/div/div[{i}]/div[3]'
#     sel_xpath = driver.find_element_by_xpath(xpath_base)
#     print(sel_xpath.text)
    
```

    0 Content
    1 R 기본 전체(전 수업 링크)
    2 통계기본이해하기(1)
    3 가설검정이해(1)
    4 통계기본이해_실습(1)-통계가설검정
    5 통계기본이해_실습(1)-통계가설검정
    6 회귀분석이해(1)
    7 첫번째 모델 만들기
    8 회귀 모델 실습(1)-mtcars
    9 회귀 모델 실습(2)-Boston 집값 예측
    10 회귀 모델 실습(3) - 캐글 데이터-집값 예측
    11 로지스틱 회귀 모델 실습(1) - 인디언 암 예측
    12 의사결정트리 기본 이해(1)
    13 의사결정트리 실습(1)
    14 의사결정트리 실습(2)
    15 데이터 탐색 - Boston 집값
    16 텍스트 마이닝 시작하기
    17 KoNLP를 패키지를 활용한 텍스트 분석(1)
    18 텍스트 감정 분석(1)
    19 TFIDF 이해하기(1)
    20 R과 MySQL 연동 환경 만들기
    21 R과 MySQL 연동 실습하기
    22 데이터 시각화 기본(1)
    23 데이터 시각화 기본(2)
    24 데이터 시각화 기본(3)
    25 데이터 시각화 기본(4)
    26 데이터 시각화 활용(5)
    27 데이터 시각화 참고자료(1)
    28 데이터 시각화 참고자료(2)


3) css_selector로 가져오기


```python
### 1)
sel_css = driver.find_elements_by_css_selector("body div div div div div div")
for idx, one in enumerate(sel_css) :
    if idx%4 == 2:
        print(one.text)
        
### 2) 이거 어떤 방식인지 대충 이해는 가는데, 자꾸 오류가 난다?    
# sel_css = driver.find_elements_by_css_selector("div[data-title='Content']")
# for one in sel_css:
#     print(one.text)
```

    Content
    R 기본 전체(전 수업 링크)
    통계기본이해하기(1)
    가설검정이해(1)
    통계기본이해_실습(1)-통계가설검정
    통계기본이해_실습(1)-통계가설검정
    회귀분석이해(1)
    첫번째 모델 만들기
    회귀 모델 실습(1)-mtcars
    회귀 모델 실습(2)-Boston 집값 예측
    회귀 모델 실습(3) - 캐글 데이터-집값 예측
    로지스틱 회귀 모델 실습(1) - 인디언 암 예측
    의사결정트리 기본 이해(1)
    의사결정트리 실습(1)
    의사결정트리 실습(2)
    데이터 탐색 - Boston 집값
    텍스트 마이닝 시작하기
    KoNLP를 패키지를 활용한 텍스트 분석(1)
    텍스트 감정 분석(1)
    TFIDF 이해하기(1)
    R과 MySQL 연동 환경 만들기
    R과 MySQL 연동 실습하기
    데이터 시각화 기본(1)
    데이터 시각화 기본(2)
    데이터 시각화 기본(3)
    데이터 시각화 기본(4)
    데이터 시각화 활용(5)
    데이터 시각화 참고자료(1)
    데이터 시각화 참고자료(2)


### 페이지의 전체 내용을 가져와 csv 파일로 정리하기
1) xpath 사용


```python
"""
xpath0_1 = /html/body/div/div/div/div/div[1]/div[1]
xpath0_2 = /html/body/div/div/div/div/div[1]/div[2]
xpath0_4 = /html/body/div/div/div/div/div[1]/div[4]/a
...

xpath1_1 = /html/body/div/div/div/div/div[2]/div[1]
xpath1_2 = /html/body/div/div/div/div/div[2]/div[2]
xpath1_4 = /html/body/div/div/div/div/div[2]/div[4]/a
"""

xpath1 = '/html/body/div/div/div/div/div/div[1]'
xpath2 = '/html/body/div/div/div/div/div/div[2]'
xpath3 = '/html/body/div/div/div/div/div/div[3]'
xpath4 = '/html/body/div/div/div/div/div/div[4]/a'

    
cate = driver.find_elements_by_xpath(xpath1)
lc_code = driver.find_elements_by_xpath(xpath2)
content = driver.find_elements_by_xpath(xpath3)
link = driver.find_elements_by_xpath(xpath4)

with open("page_xpath.csv", "w") as fp :
    for i in range(len(cate)) :
        try :
            fp.write(cate[i].text+",")
            fp.write(lc_code[i].text+",")
            fp.write(content[i].text+",")
            if i == 0 :
                fp.write("Link"+",")
            else :
                fp.write(link[i-1].get_attribute("href")+",")
            fp.write("\n")
        except :
            print(i)

```

2) css_selector 사용


```python

css_base = 'body div div div div div div'
css4link = 'body div div div div div div a'

sel_css = driver.find_elements_by_css_selector(css_base)
sel_link = driver.find_elements_by_css_selector(css4link)

with open("page_css.csv", "w") as fp :
    
    for idx, one in enumerate(sel_css):
        try :
            if idx == 3:
                fp.write("Link"+"\n")
            elif idx%4 == 3:
                fp.write(sel_link[idx//4-1].get_attribute("href")+"\n")
            else :
                fp.write(one.text+"\t")
        except :
            print(idx)
            print(len(sel_link))

```

## myStudy 3 : 다음 부동산을 통해 코스피 시가총액상위 정보 가져오기
### BeautifulSoup + Selenium


```python
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import lxml


start = time.time() 
driver = webdriver.Chrome('./chromedriver')
driver
```




    <selenium.webdriver.chrome.webdriver.WebDriver (session="d8d0afc39f541582b2e4d11c0c1e9d73")>




```python
url = 'https://finance.daum.net/domestic/market_cap' # page 1만
driver.get(url)
```


```python
page = driver.page_source
soup = BeautifulSoup(page, 'lxml')
soup.title
```




    <title>시가총액별 | 다음 금융 </title>




```python
# header
def mod_head(str_org):
    str1 = str_org.replace(" -\n\n\n", "\n")
    str2 = str1.replace(" -\n\n","\n")
    str3 = str2.replace("\n\n","\n")
    str4 = str3.replace("\n", ",")
    return str4[1:-1]

head_soup = soup.find_all("tr")[1]
head = mod_head(head_soup.text)
head
```




    '순위,종목명,현재가,전일비,등락률,시가총액,상장주식수,외국인'




```python
# 한개만
soup1 = soup.find_all("tr")[10]
soup_td = soup1.find_all("td")
rank = soup_td[0].text
name = soup_td[1].text
price_now = soup_td[2].text.strip()
diff = soup_td[3].text.strip()
ratio = soup_td[4].span.text.strip()
val = soup_td[5].span.text.strip()
nstock = soup_td[6].span.text.strip()
foreign = soup_td[7].span.text.strip()

print(rank, name, price_now, diff, ratio, val, nstock, foreign)
```

    9 삼성SDI 674,000 ▲24,000 +3.69% 463,473 68,764,530 42.62%



```python
# 여러개

def mod_coma(str_org):
    return str_org.replace(",","")

with open("daum_marker_cap.csv","w") as fp :
    fp.write(head+"\n")
    for i in range(2, 32): # 31
        soup_one = soup.find_all("tr")[i]
        soup_td = soup_one.find_all("td")
        fp.write(soup_td[0].text+",")
        fp.write(soup_td[1].text+",")
        fp.write(mod_coma(soup_td[2].text.strip())+",")
        fp.write(mod_coma(soup_td[3].text.strip())+",")
        fp.write(mod_coma(soup_td[4].span.text.strip())+",")
        fp.write(mod_coma(soup_td[5].span.text.strip())+",")
        fp.write(mod_coma(soup_td[6].span.text.strip())+",")
        fp.write(mod_coma(soup_td[7].span.text.strip())+",")
        fp.write("\n")

```


```python
import pandas as pd

data = pd.read_csv('daum_marker_cap.csv')
data
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
      <th>종목명</th>
      <th>현재가</th>
      <th>전일비</th>
      <th>등락률</th>
      <th>시가총액</th>
      <th>상장주식수</th>
      <th>외국인</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>삼성전자</td>
      <td>80500</td>
      <td>▼400</td>
      <td>-0.49%</td>
      <td>4805675</td>
      <td>5969782550</td>
      <td>53.82%</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>SK하이닉스</td>
      <td>124500</td>
      <td>▼2000</td>
      <td>-1.58%</td>
      <td>906363</td>
      <td>728002365</td>
      <td>49.58%</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>카카오</td>
      <td>155000</td>
      <td>▲7000</td>
      <td>+4.73%</td>
      <td>688091</td>
      <td>443929585</td>
      <td>33.20%</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>NAVER</td>
      <td>398000</td>
      <td>▲8500</td>
      <td>+2.18%</td>
      <td>653768</td>
      <td>164263395</td>
      <td>56.87%</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>5</th>
      <td>삼성전자우</td>
      <td>74000</td>
      <td>▼300</td>
      <td>-0.40%</td>
      <td>608936</td>
      <td>822886700</td>
      <td>76.54%</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>6</th>
      <td>LG화학</td>
      <td>822000</td>
      <td>▼13000</td>
      <td>-1.56%</td>
      <td>580269</td>
      <td>70592343</td>
      <td>46.06%</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>7</th>
      <td>삼성바이오로직스</td>
      <td>836000</td>
      <td>▲3000</td>
      <td>+0.36%</td>
      <td>553139</td>
      <td>66165000</td>
      <td>10.05%</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>8</th>
      <td>현대차</td>
      <td>235000</td>
      <td>▼1500</td>
      <td>-0.63%</td>
      <td>502120</td>
      <td>213668187</td>
      <td>29.92%</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>9</th>
      <td>삼성SDI</td>
      <td>674000</td>
      <td>▲24000</td>
      <td>+3.69%</td>
      <td>463473</td>
      <td>68764530</td>
      <td>42.62%</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>10</th>
      <td>셀트리온</td>
      <td>270000</td>
      <td>▲1000</td>
      <td>+0.37%</td>
      <td>372375</td>
      <td>137916534</td>
      <td>20.73%</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>11</th>
      <td>기아</td>
      <td>88500</td>
      <td>▲900</td>
      <td>+1.03%</td>
      <td>358747</td>
      <td>405363347</td>
      <td>33.47%</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>12</th>
      <td>POSCO</td>
      <td>340000</td>
      <td>▼1000</td>
      <td>-0.29%</td>
      <td>296435</td>
      <td>87186835</td>
      <td>53.78%</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>13</th>
      <td>현대모비스</td>
      <td>287000</td>
      <td>▼500</td>
      <td>-0.17%</td>
      <td>272056</td>
      <td>94793094</td>
      <td>36.55%</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>14</th>
      <td>LG생활건강</td>
      <td>1701000</td>
      <td>▲36000</td>
      <td>+2.16%</td>
      <td>265666</td>
      <td>15618197</td>
      <td>46.12%</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>15</th>
      <td>LG전자</td>
      <td>157000</td>
      <td>▲2500</td>
      <td>+1.62%</td>
      <td>256927</td>
      <td>163647814</td>
      <td>30.67%</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>16</th>
      <td>SK이노베이션</td>
      <td>277000</td>
      <td>▼4500</td>
      <td>-1.60%</td>
      <td>256130</td>
      <td>92465564</td>
      <td>23.63%</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>17</th>
      <td>삼성물산</td>
      <td>136000</td>
      <td>▼500</td>
      <td>-0.37%</td>
      <td>254166</td>
      <td>186887081</td>
      <td>14.74%</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>18</th>
      <td>KB금융</td>
      <td>56800</td>
      <td>▼100</td>
      <td>-0.18%</td>
      <td>236179</td>
      <td>415807920</td>
      <td>68.92%</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>19</th>
      <td>SK텔레콤</td>
      <td>326500</td>
      <td>▼1000</td>
      <td>-0.31%</td>
      <td>235276</td>
      <td>72060143</td>
      <td>45.61%</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>20</th>
      <td>신한지주</td>
      <td>41100</td>
      <td>▼550</td>
      <td>-1.32%</td>
      <td>212322</td>
      <td>516599554</td>
      <td>60.86%</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>21</th>
      <td>SK</td>
      <td>282000</td>
      <td>▼3000</td>
      <td>-1.05%</td>
      <td>198416</td>
      <td>70360297</td>
      <td>20.36%</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>22</th>
      <td>엔씨소프트</td>
      <td>818000</td>
      <td>▼6000</td>
      <td>-0.73%</td>
      <td>179584</td>
      <td>21954022</td>
      <td>51.90%</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>23</th>
      <td>한국전력</td>
      <td>26900</td>
      <td>-</td>
      <td>0.00%</td>
      <td>172688</td>
      <td>641964077</td>
      <td>15.78%</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>24</th>
      <td>아모레퍼시픽</td>
      <td>281500</td>
      <td>▼3000</td>
      <td>-1.05%</td>
      <td>164561</td>
      <td>58458490</td>
      <td>33.82%</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>25</th>
      <td>LG</td>
      <td>103500</td>
      <td>▼500</td>
      <td>-0.48%</td>
      <td>162807</td>
      <td>157300993</td>
      <td>33.53%</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>26</th>
      <td>삼성생명</td>
      <td>80000</td>
      <td>▼1200</td>
      <td>-1.48%</td>
      <td>160000</td>
      <td>200000000</td>
      <td>13.32%</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>27</th>
      <td>HMM</td>
      <td>44400</td>
      <td>▼250</td>
      <td>-0.56%</td>
      <td>153354</td>
      <td>345392487</td>
      <td>12.37%</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>28</th>
      <td>삼성에스디에스</td>
      <td>186000</td>
      <td>▼1500</td>
      <td>-0.80%</td>
      <td>143923</td>
      <td>77377800</td>
      <td>11.68%</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>29</th>
      <td>하나금융지주</td>
      <td>45300</td>
      <td>▼700</td>
      <td>-1.52%</td>
      <td>136010</td>
      <td>300242062</td>
      <td>68.45%</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>30</th>
      <td>삼성전기</td>
      <td>178500</td>
      <td>▲2500</td>
      <td>+1.42%</td>
      <td>133328</td>
      <td>74693696</td>
      <td>31.08%</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>




```python

```
