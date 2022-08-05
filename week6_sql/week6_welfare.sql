-- Active: 1658994301812@@127.0.0.1@3306@teamproject6
select * from suicide_rate;
select * from life_expectancy_at;

--[ 외국과 비교한 우리나라 노령인구 실태 파악]
--1.suicide_rate -- 정렬 및 색 bar
--2.life_expendency_at -- 남,녀 테이블 나눠서 그 왼쪽,오른쪽 bar(수업시간에)

--[자살률 지표] : 1.경제, 2. 외로움,고독
--1.poverty_rate -- 정렬 및 색 bar
--2.독거노인비율 -- plot 일단? 증가추세니까

-- [ 은퇴시기 노령인구 상황 ] 임금,일자리,고용률 모두 최악인 상황에서 퇴직
-- 테이블 세개, PLOT 한곳에
-- 1.일자리 만족도, 임금만족도,고용률

-- [ 현상황 ]: 령 생산가능인구 많고,의지도 있지만, 사회적지지가 많이 부족한상황 
-- 1.워드클라우드: 일할 의지 높아보임
-- 2. social_support : 분류3개로 테이블 나눠서 plot (중간 데이터 없는데 되나?!)
-- 3.경제활동인구비율: 파이그래프 3개 SUPLOT
-----> 노령인구 가장 많음.  (생산가능인구 / 경제활동인구 / 비겅제활동인구 ) 
-----> 나라 생산가능인구 65세규정, 조정필요.


# 1.suicide_rate -- 정렬 및 색 bar

#2.life_expendaency_at -- 남,녀 테이블 나눠서 그 왼쪽,오른쪽 bar(수업시간에)
SELECT LOCATION,Value FROM life_expectancy_at
WHERE SUBJECT = 'MEN'
ORDER BY Value DESC;
SELECT LOCATION,Value FROM life_expectancy_at
WHERE SUBJECT = 'WOMEN'
ORDER BY Value DESC;

SELECT LOCATION FROM life_expectancy
WHERE SUBJECT = 'TOT' ORDER BY Value DESC;


SELECT LOCATION, Value FROM social_support
WHERE SUBJECT = 'YOUNG' ORDER BY Value DESC; 

SELECT LOCATION, Value FROM social_support
WHERE SUBJECT = 'MIDDLE_AGED' ORDER BY Value DESC; 

SELECT LOCATION, Value FROM social_support
WHERE SUBJECT = 'OLD' ORDER BY Value DESC; 

select * from 일자리만족도;
select * from 임금만족도;
select * from 고용률;

# 기본키, 외래키 설정하기

# 참조할 테이블 기본키 설정 : 실제 입력시 [] 생략 / ''필요없음
-- alter table [참조할 테이블명]
-- add constraint [LOC_ID] primary key ([키 컬럼명]);

# 사용할 테이블 기본키 설정
-- alter table [사용할 테이블명]
-- ADD CONSTRAINT [LOC_ID2] PRIMARY KEY([키 컬럼명]);

# 참조하기
-- alter table [사용할 테이블명]
-- add constraint [LOC_ID3] foreign key ([키 컬럼명]) references [참조할 테이블명]([키 컬럼명]);

alter table poverty_rate
ADD CONSTRAINT LOC_ID PRIMARY KEY(LOCATION);
alter table poverty_rate
add constraint LOC_ID4 foreign key (LOCATION) references 국가식별번호(LOCATION);

alter table life_expectancy
ADD CONSTRAINT LOC_ID PRIMARY KEY(LOCATION);
alter table life_expectancy
add constraint LOC_ID5 foreign key (LOCATION) references 국가식별번호(LOCATION);


alter table life_expectancy_at
ADD CONSTRAINT LOC_ID PRIMARY KEY(LOCATION);
alter table life_expectancy_at
add constraint LOC_ID6 foreign key (LOCATION) references 국가식별번호(LOCATION);



alter table social_support
ADD CONSTRAINT LOC_ID PRIMARY KEY(LOCATION);
alter table social_support
add constraint LOC_ID7 foreign key (LOCATION) references 국가식별번호(LOCATION);



SELECT `country name`,Value  FROM social_support	JOIN 국가식별번호	
ON social_support.LOCATION = 국가식별번호.LOCATION
WHERE SUBJECT='OLD' 
ORDER BY Value;

INSERT INTO 국가식별번호[countryname]
values();


alter table 임금만족도
ADD CONSTRAINT ECO_ID2 PRIMARY KEY(age);
alter table 경제활동인구비율
add constraint ECO_ID primary key (age);
alter table 임금만족도
add constraint ECO_ID3 foreign key (age) references 경제활동인구비율(age);

alter table 일자리만족도
ADD CONSTRAINT ECO_ID4 PRIMARY KEY(age);

alter table 일자리만족도
add constraint ECO_ID5 foreign key (age) references 경제활동인구비율(age);

alter table 고용률
ADD CONSTRAINT ECO_ID6 PRIMARY KEY(age);

alter table 고용률
add constraint ECO_ID7 foreign key (age) references 경제활동인구비율(age);
