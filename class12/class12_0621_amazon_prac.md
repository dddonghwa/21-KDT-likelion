# 아마존에서 상품 리뷰 가져오기

`Selenium`과 `BeautifulSoup`을 이용해서 아마존 홈페이지에 상품 리뷰를 가져오는 실습입니다.   
아마존에서 'imac 24inch 2021'을 검색해서 리뷰 정보를 가져와보았습니다.    

#### 실습 순서
|순서|내용| 주요 함수|
|----|---|---|
|1|웹드라이버 객체 할당| `selenium.webdriver.Chrome`  | 
|2|웹사이트 열기 | `object.get(url)` |
|3|검색 키워드 설정 및 검색 | `object.clear/send_keys` |
|4|목록 선택 및 '모든 리뷰 보기' 페이지로 이동 | `object.click` |
|5|원하는 정보 가져오기 | `object.page_source` `find/find_all` |
|6|csv 파일로 내보내기 | `object.to_csv` |

cf. 정보 카테고리 
사용자 이름, 평점, 작성일자, 작성국가, 리뷰 제목, 리뷰 내용, 도움받은 사람의 수

#### 추후 개선이 가능한 사항
1. 검색어 사용자 입력
2. 검색 목록 중 자동 선택 


#### 1) 웹드라이버 객체 할당


```python
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import pandas as pd

driver = webdriver.Chrome("./chromedriver")
driver
```




    <selenium.webdriver.chrome.webdriver.WebDriver (session="f3395dce04d463771e9938bfd7ab9307")>



#### 2) 아마존 웹사이트 열기


```python
main_url = "https://www.amazon.com/"
driver.get(main_url)
```

#### 3) 검색 키워드 설정 및 검색


```python
keyword = "imac 24inch 2021"

sel_search = driver.find_element_by_id("twotabsearchtextbox")
sel_btn = driver.find_element_by_id("nav-search-submit-button")

# print(sel_search.text, sel_btn.text)
sel_search.clear()
sel_search.send_keys(keyword)
sel_btn.click()
```

#### 4) 목록 중 원하는 상품 선택 및 모든 리뷰 보기 페이지로 이동


```python
page = driver.page_source
soup = BeautifulSoup(page, 'html.parser')
all_soup = soup.find_all("div",class_="s-main-slot s-result-list s-search-results sg-row")[0]
one_soup = all_soup.find_all("div", class_="s-result-item s-asin sg-col-0-of-12 sg-col-16-of-20 sg-col sg-col-12-of-16")[0]
href_soup = one_soup.find("a", class_="a-link-normal a-text-normal")
prod_url = main_url +href_soup.get("href")
# print(prod_url)
```


```python
driver.get(prod_url)
sel_r = driver.find_element_by_xpath('//*[@id="acrCustomerReviewText"]')
sel_r.click()

sel_r_all = driver.find_element_by_xpath('//*[@id="reviews-medley-footer"]/div[2]/a')
sel_r_all.click()
```

#### 5) 원하는 정보 가져오기


```python
# 한 페이지, 한 개의 리뷰만
page = driver.page_source
soup = BeautifulSoup(page, 'html.parser')
all_soup = soup.find_all("div", class_="a-section review aok-relative")

one_soup = all_soup[1]

usr = one_soup.find("span", class_="a-profile-name").text
score = one_soup.find("span", class_="a-icon-alt").text[:3]
title = one_soup.find("a", class_="a-size-base a-link-normal review-title a-color-base review-title-content a-text-bold").span.text
info = one_soup.find("span", class_="a-size-base a-color-secondary review-date").text
body = one_soup.find("span", class_="a-size-base review-text review-text-content").span.text.strip()

date = info.split(" ")[-3:]
date = " ".join(date)

cntry = info.split(" ")[3:-4]
cntry = " ".join(cntry)

npp = one_soup.find("span", class_="a-size-base a-color-tertiary cr-vote-text").text
npp = npp.split(" ")[0]

print(usr, score, date, cntry, npp, title, body)
```


```python
# 여러 페이지, 여러 리뷰
url_1page = 'https://www.amazon.com/Apple-24-inch-8%E2%80%91core-7%E2%80%91core-256GB/product-reviews/B0932FPBV8/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews'
driver.get(url_1page)

usr_all = []
score_all = []
title_all = []
date_all = []
cntry_all = []
npp_all = []
body_all = []

while True:
    
    time.sleep(3)
    page = driver.page_source
    soup = BeautifulSoup(page, "html.parser")
    all_soup = soup.find_all("div", class_="a-section review aok-relative")
    
    
    for one in all_soup :
        usr = one.find("span", class_="a-profile-name").text
        score = one.find("span", class_="a-icon-alt").text[:3]
        title = one.find("a", class_="a-size-base a-link-normal review-title a-color-base review-title-content a-text-bold").span.text
        info = one.find("span", class_="a-size-base a-color-secondary review-date").text
        body = one.find("span", class_="a-size-base review-text review-text-content").span.text.strip()
        
        date = info.split(" ")[-3:]
        date = " ".join(date)

        cntry = info.split(" ")[3:-4]
        cntry = " ".join(cntry)
        try :
            npp = one.find("span", class_="a-size-base a-color-tertiary cr-vote-text").text
            npp = npp.split(" ")[0]
            npp_all.append(npp)
        except :
            npp = "0"
            npp_all.append(npp)

        usr_all.append(usr)
        score_all.append(score)
        title_all.append(title)
        body_all.append(body)
        date_all.append(date)
        cntry_all.append(cntry)
    
    try :
        sel_next = driver.find_element_by_xpath('//*[@id="cm_cr-pagination_bar"]/ul/li[2]/a')
        sel_next.click()
    except :
        break
```

#### 6) DataFrame으로 만들어 csv로 저장하기


```python
dat = {"usr_id":usr_all, "score":score_all,"date":date_all,"country":cntry_all,"review_title": title_all,  "review_body": body_all} 
dat = pd.DataFrame(dat)
dat.to_csv("imac_review.csv")
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
      <th>usr_id</th>
      <th>score</th>
      <th>date</th>
      <th>country</th>
      <th>review_title</th>
      <th>review_body</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>daviddiy</td>
      <td>5.0</td>
      <td>June 2, 2021</td>
      <td>United States</td>
      <td>Best iMac so far</td>
      <td>I’m downsizing from a 27in iMac to this 24in a...</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Nick</td>
      <td>1.0</td>
      <td>May 28, 2021</td>
      <td>United States</td>
      <td>Strong mold smell</td>
      <td>Computer had a very strong mold smell due to s...</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Linda K.</td>
      <td>1.0</td>
      <td>June 6, 2021</td>
      <td>United States</td>
      <td>Buy your computers from Amazon</td>
      <td>3 weeks after buying this computer I was asked...</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Rolando Pizarro</td>
      <td>5.0</td>
      <td>May 30, 2021</td>
      <td>United States</td>
      <td>Best iMac ever made!</td>
      <td>I ordered the iMac since the spring loaded eve...</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Larry</td>
      <td>5.0</td>
      <td>June 7, 2021</td>
      <td>United States</td>
      <td>It works flawlessly</td>
      <td>I have favored using Apple products over the y...</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Michael U.</td>
      <td>4.0</td>
      <td>June 11, 2021</td>
      <td>United States</td>
      <td>Love the iMac but have already had problems wi...</td>
      <td>I have used the iMac for years and enjoy worki...</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Oregon T.</td>
      <td>1.0</td>
      <td>June 11, 2021</td>
      <td>United States</td>
      <td>Worked fine for a couple days then BRICK!</td>
      <td>Updated to newest OS - Worked for a couple day...</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Amazon Customer</td>
      <td>5.0</td>
      <td>June 13, 2021</td>
      <td>United States</td>
      <td>Greta. Clean and Sleek</td>
      <td>If you can afford to, get the one with the mos...</td>
    </tr>
    <tr>
      <th>8</th>
      <td>CAtoAKgal</td>
      <td>5.0</td>
      <td>June 14, 2021</td>
      <td>United States</td>
      <td>The feel of ease</td>
      <td>Both Apple amd Amazon strive to make it easy. ...</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Ray</td>
      <td>5.0</td>
      <td>May 27, 2021</td>
      <td>United States</td>
      <td>Refreshing green. Buy the base model!</td>
      <td>..Unless you are a “pro” user utilizing high l...</td>
    </tr>
    <tr>
      <th>10</th>
      <td>Christopher</td>
      <td>5.0</td>
      <td>May 28, 2021</td>
      <td>United States</td>
      <td>Excellent upgrade</td>
      <td>It’s super fast and the screen is fantastic. S...</td>
    </tr>
    <tr>
      <th>11</th>
      <td>Jong Lee</td>
      <td>4.0</td>
      <td>May 22, 2021</td>
      <td>United States</td>
      <td>Small footprint and light</td>
      <td>Nice machine and it is light. 24” is a bit sma...</td>
    </tr>
    <tr>
      <th>12</th>
      <td>smrtypnts</td>
      <td>2.0</td>
      <td>June 12, 2021</td>
      <td>United States</td>
      <td>NOT a touch screen ))=</td>
      <td>Very disappointed this is a very expensive com...</td>
    </tr>
    <tr>
      <th>13</th>
      <td>albert mead</td>
      <td>1.0</td>
      <td>June 18, 2021</td>
      <td>United States</td>
      <td>Disappointed and discouraged in my new IMac</td>
      <td>I have only had this $1600 INac for a couple o...</td>
    </tr>
    <tr>
      <th>14</th>
      <td>Joshua E. M.</td>
      <td>5.0</td>
      <td>May 23, 2021</td>
      <td>United States</td>
      <td>Most Gorgeous iMac Ever</td>
      <td>Ordered on Apple website, delivered yesterday,...</td>
    </tr>
    <tr>
      <th>15</th>
      <td>Robert L Powell</td>
      <td>3.0</td>
      <td>June 19, 2021</td>
      <td>United States</td>
      <td>Not happy</td>
      <td>Can't  get  it to pair with my old  computer.</td>
    </tr>
  </tbody>
</table>
</div>


