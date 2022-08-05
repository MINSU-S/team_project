# 블로그 검색 함수 : 워드클라우드 50위/ 네이버 블로그 제목 70개 ---------------------------------------------------------------------
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
    okt = Okt()
    
    blog_title_text=[]
    noun_list =[]
    counts =[]
    tag =[]
    
    for i in range(1,10):
        wd	= webdriver.Chrome('C:\MINSU\chromedriver')
        main_url =f"https://section.blog.naver.com/Search/Post.naver?pageNo={i}&rangeType=ALL&orderBy=sim&keyword={keyword}" 

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
    
    # if platform.system() == 'Windows':
    #     font_name = fm.FontProperties(fname='./Fonts/malgun.ttf').get_name()
    #     plt.rc('font', family=font_name)
    # else:
    #     plt.rc('font', family='AppleGothic', size=8)
    
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
    
    
# DATABASE TABLE 불러오기 함수 ----------------------------------------------------------------------------------------------
def db_to_df(db,sql,col_list):
    # 변수 
    # db : 데이터베이스명 (str)
    # sql: 원하는 기능의 sql문(str)
    # col_list : 데이터프레임에 사용돨 컬럼명(list)
    # 반환값 df
    
    # 모듈 설치
    import pymysql
    import platform
    import matplotlib.pyplot as plt
    import pandas as pd
    
    # DB에서 불러오기
    conn	=	pymysql.connect(host='localhost',	user='root',	password='206477', db=f'{db}',	charset='utf8')
    curs	=	conn.cursor()
    sql =f"""{sql};"""
    curs.execute(sql)
    rows	=curs.fetchall()
    
    # 데이터프레임만들기	
    df = pd.DataFrame(rows,columns=col_list)
    return df

df_suicide_rate = db_to_df('teamproject6','SELECT LOCATION,Value FROM suicide_rate ORDER BY Value DESC',['국가','자살률'])
print(df_suicide_rate)


# 막대 그래프 그리기 ---------------------------------------------------------------------------------------------------------
    # import platform
    # import matplotlib.pyplot as plt
    
    # # 한글 패치
    # if	platform.system()	==	'Windows':
    #     plt.rc('font',	family='Malgun Gothic')
    # else:
    #     plt.rc('font',	family='AppleGothic')

    # plt.figure(figsize=(14,6))
    # plt.bar(df_suicide['국가'], df_suicide['자살률'],color=colors)
    # plt.title('국가별 60대 이상 노령인구 자살률')
    # #plt.xlabel('기간')
    # plt.ylabel('자살률')
    # plt.xticks(ticks=df_suicide['국가'], labels=df_suicide['국가'], rotation=40)
    # #plt.legend()
    # plt.show()

    
# 파이 그래프 ------------------------------------------------------------------------------------------------------------------

# # 생사가능인구, 경제활동인구, 비경제활동인구 비율 파이 그래프 그리기
# labels = ['20세미만', '21-29세', '31-39세', '41-49세','51-59세','60세이상']
# colors=['#ff9999', '#ffc000', '#8fd9b6', '#d395d0','#D8EF77','#56B4E9']
# wedgeprops={'width': 0.7, 'edgecolor': 'w', 'linewidth': 5}

# df_pop =connect_sql('teamproject6','경제활동인구비율',['age','인구(천명)','경제활동인구(천명)','비경제활동인구(천명)'])

# if	platform.system()	==	'Windows':
#     plt.rc('font',	family='Malgun Gothic')
# else:
#     plt.rc('font',	family='AppleGothic')

# fig, axes = plt.subplots(1,3, figsize=(20, 12))

# plt.subplot(1,3,1)
# plt.pie(df_pop['인구(천명)'],autopct = '%.1f%%',startangle=90,colors=colors,explode = [0.03, 0.03, 0.03, 0.03,0.03,0.03],shadow=True,wedgeprops = wedgeprops,labels=labels)
# plt.title('생산가능인구 비율',fontsize=20)

# plt.subplot(1,3,2)
# plt.pie(df_pop['경제활동인구(천명)'],autopct = '%.1f%%',startangle=90,colors=colors,explode = [0.05, 0.05, 0.05, 0.05,0.05,0.05],shadow=True,wedgeprops = wedgeprops,labels=labels)
# plt.title('경제활동인구 비율',fontsize=20)

# plt.subplot(1,3,3)
# plt.pie(df_pop['비경제활동인구(천명)'],autopct = '%.1f%%',startangle=90,colors=colors,explode = [0.05, 0.05, 0.05, 0.05,0.05,0.07],shadow=True,wedgeprops = wedgeprops,labels=labels)
# plt.title('비경제활동인구 비율',fontsize=20)

# plt.show()    



# 기본키, 외래키 설정하기 ----------------------------------------------------

# 1. 참조할 테이블 기본키 설정 : 실제 입력시 [] 생략 / ''필요없음
#  alter table [참조할 테이블명]
#  add constraint [pk_키컬럼] primary key ([키 컬럼명]);

# 2. 사용할 테이블 기본키 설정
#  alter table [사용할 테이블명]
#  ADD CONSTRAINT [pk_키컬럼] PRIMARY KEY([키 컬럼명]);

# 3. 참조하기
#  alter table [사용할 테이블명]
#  add constraint [fk_테이블_컬럼] foreign key ([키 컬럼명]) references [참조할 테이블명]([키 컬럼명]);