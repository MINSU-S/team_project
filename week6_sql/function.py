# 블로그 검색 함수
def	blog_search(keyword):
    # 모듈설치
    from	bs4	import	BeautifulSoup
    import	requests
    from	itertools import count
    from	selenium import	webdriver
    from	konlpy.tag import Okt
    from	collections import Counter
    from	wordcloud import WordCloud
    import	matplotlib.pyplot as plt
    import matplotlib.font_manager as fm
    from urllib.request import urlopen
    import platform
    import pandas as pd
    import re
    okt = Okt()
    
    blog_title_text=[]
    noun_list =[]
    counts =[]
    tag =[]
    
    for i in range(1,10):
        wd	= webdriver.Chrome('C:\MINSU\chromedriver')
        main_url =f"https://section.blog.naver.com/Search/Post.naver?pageNo={i}&rangeType=ALL&orderBy=sim&keyword={keyword}" #

        wd.get(main_url)	
        
        html	=	wd.page_source
        soupData =	BeautifulSoup(html,	'html.parser')
        blog_title =	soupData.find_all('span',	{'class':'title'})
        
        for i in range(7):
            blog_title_text.append(blog_title[i].text)
        
        for data in blog_title_text:
            sentences_tag = okt.pos(data)
            # tag가 명사인 단어들만 noun_adj_list에 넣어준다.
            for word, tag in sentences_tag:
                if tag in ['Noun']:
                    if keyword in word:
                        continue
                    elif '여행' in word:
                        continue
                    else:
                        noun_list.append(word)
        wd.quit()
        
    counts	= Counter(noun_list)
    tags	= counts.most_common(50)
    
    if	platform.system()	==	'Windows':
        path	=	r'c:\Windows\Fonts\malgun.ttf'
    elif platform.system()	==	'Darwin':		#	Mac	OS
        path	=	r'/System/Library/Fonts/AppleGothic'
    else:
        path	=	r'/usr/share/fonts/truetype/name/NanumMyeongjo.ttf'

    wc = WordCloud(font_path=path,	background_color='white',	width=800,	height=600, random_state = 30)
    # print(dict(tags))
    cloud =	wc.generate_from_frequencies(dict(tags))
    plt.figure(figsize=(12,	6))
    #plt.text(x=800, y = 300 ,s= f'<-{keyword}', color = 'black', fontsize = 30)
    plt.title(f'[{keyword}]', size=40)
    plt.axis('off')
    plt.imshow(cloud)
    plt.show() 
    # return(tags)    

# '가나',
# '가봉',
# '가이아나',
# '감비아',
# '건지 섬',
# '과들루프',
# '과테말라',
# '괌',
# '그레나다',
# '조지아',
# '그리스',
# '그린란드',
# '기니',
# '기니비사우',
# '나미비아',
# '나우루',
# '나이지리아',
# '남극',
# '남아프리카 공화국',
# '네덜란드',
# '네덜란드령 안틸레스',
# '네팔',
# '노르웨이',
# '노퍽 섬',
# '누벨칼레도니',
# '뉴질랜드',
# '니우에',
# '니제르',
# '니카라과',
# '대한민국',
# '덴마크',
# '도미니카',
# '도미니카 공화국',
# '독일',
# '동티모르',
# '라오스',
# '라이베리아',
# '라트비아',
# '러시아',
# '레바논',
# '레소토',
# '레위니옹',
# '루마니아',
# '룩셈부르크',
# '르완다',
# '리비아',
# '리투아니아',
# '리히텐슈타인',
# '마다가스카르',
# '마르티니크',
# '마셜 제도',
# '마요트',
# '마카오',
# '마케도니아 공화국',
# '말라위',
# '말레이시아',
# '말리',
# '맨 섬',
# '멕시코',
# '모나코',
# '모로코',
# '모리셔스',
# '모리타니',
# '모잠비크',
# '몬테네그로',
# '몬트세랫',
# '몰도바',
# '몰디브',
# '몰타',
# '몽골',
# '미국',
# '미국령 군소 제도',
# '미국령 버진아일랜드',
# '미얀마',
# '미크로네시아 연방',
# '바누아투',
# '바레인',
# '바베이도스',
# '바티칸 시국',
# '바하마',
# '방글라데시',
# '버뮤다',
# '베냉',
# '베네수엘라',
# '베트남',
# '벨기에',
# '벨라루스',
# '벨리즈',
# '보스니아 헤르체고비나',
# '보츠와나',
# '볼리비아',
# '부룬디',
# '부르키나파소',
# '부베 섬',
# '부탄',
# '북마리아나 제도',
# '불가리아',
# '브라질',
# '브루나이',
# '사모아',
# '사우디아라비아',
# '사우스조지아 사우스샌드위치 제도',
# '산마리노',
# '상투메 프린시페',
# '생피에르 미클롱',
# '서사하라',
# '세네갈',
# '세르비아',
# '세이셸',
# '세인트루시아',
# '세인트빈센트 그레나딘',
# '세인트키츠 네비스',
# '세인트헬레나',
# '소말리아',
# '솔로몬 제도',
# '수단',
# '수리남',
# '스리랑카',
# '스발바르 얀마옌',
# '스와질란드',
# '스웨덴',
# '스위스',
# '스페인',
# '슬로바키아',
# '슬로베니아',
# '시리아',
# '시에라리온',
# '싱가포르',
# '아랍에미리트',
# '아루바',
# '아르메니아',
# '아르헨티나',
# '아메리칸사모아',
# '아이슬란드',
# '아이티',
# '아일랜드',
# '아제르바이잔',
# '아프가니스탄',
# '안도라',
# '알바니아',
# '알제리',
# '앙골라',
# '앤티가 바부다',
# '앵귈라',
# '에리트레아',
# '에스토니아',
# '에콰도르',
# '에티오피아',
# '엘살바도르',
# '영국',
# '영국령 버진아일랜드',
# '영국령 인도양 지역',
# '예멘',
# '오만',
# '오스트레일리아',
# '오스트리아',
# '온두라스',
# '올란드 제도',
# '요르단',
# '우간다',
# '우루과이
# '우즈베키스탄
# '우크라이나
# '왈리스 퓌튀나
# '이라크
# '이란
# '이스라엘
# '이집트
# '이탈리아
# '인도네시아
# '인도
# '일본
# '자메이카
# '잠비아
# '저지 섬
# '적도 기니
# '조선민주주의인민공화국
# '중앙아프리카 공화국
# '중화민국
# '중화인민공화국
# '지부티
# '지브롤터
# '짐바브웨
# '차드
# '체코
# '칠레
# '카메룬
# '카보베르데
# '카자흐스탄
# '카타르
# '캄보디아
# '캐나다
# '케냐
# '케이맨 제도
# '코모로
# '코스타리카
# '코코스 제도
# '코트디부아르
# '콜롬비아
# '콩고 공화국
# '콩고 민주 공화국
# '쿠바
# '쿠웨이트
# '쿡 제도
# '크로아티아
# '크리스마스 섬
# '키르기스스탄
# '키리바시
# '키프로스
# '타이
# '타지키스탄
# '탄자니아
# '터크스 케이커스 제도
# '터키
# '토고
# '토켈라우
# '통가
# '투르크메니스탄
# '투발루
# '튀니지
# '트리니다드 토바고
# '파나마
# '파라과이
# '파키스탄
# '파푸아 뉴기니
# '팔라우
# '팔레스타인
# '페로 제도
# '페루
# '포르투갈
# '포클랜드 제도
# '폴란드
# '푸에르토리코
# '프랑스
# '프랑스령 기아나
# '프랑스령 남부와 남극 지역
# '프랑스령 폴리네시아
# '피지
# '핀란드
# '필리핀
# '핏케언 제도
# '허드 맥도널드 제도
# '헝가리
# '홍콩