# [ 9주차 팀프로젝트 ]  신민수

# 영아 출산률 - 영아 사망률
# 연도별 (1955~ 2100) 5년 단위
# 국가별 (OECD국가: 36개, 대륙별 데이터 전체 결측치)
# 각각 꺾은선 그래프
# 두 지표 상관관계 : 버블플랏
# --------------------------------------------------------------

# 1) 데이터 불러오기
library(readxl)
library(VIM)

data_birth <- read_excel("./project_data.xlsx", sheet = '합계출산율')
data_dead  <- read_excel("./project_data.xlsx", sheet = '영아사망률')
data_1p_gdp <- read.csv("./1인당국내총생산.csv", na.strings=c('-'))
# 2. 데이터셋 확인

# 2-1) 행,열 수 확인 : 30행 44열
dim(data_birth)
dim(data_dead)
dim(data_1p_gdp)

# 2-2) 데이터 설명
str(data_birth)
str(data_dead)

str(data_1p_gdp)
names(data_1p_gdp) <- c('시점',1960:2020)
data_1p_gdp <- t(data_1p_gdp)
head(data_1p_gdp)
colnames(data_1p_gdp)
data_1p_gdp<-data.frame(data_1p_gdp)

data_1p_gdp <- data_1p_gdp[-1,]
data_1p_gdp$시점 <- row.names(data_1p_gdp)
data_1p_gdp

# 2-3) 결측치 확인 : 대륙별 통합 데이터 5열 전부 결측치
aggr(data_birth, prop = FALSE, numbers = TRUE)
aggr(data_dead, prop = FALSE, numbers = TRUE)
aggr(data_1p_gdp, prop = FALSE, numbers = TRUE)


data_birth <- data_birth[-c(2,7,11,15,42)]
data_dead <- data_dead[-c(2,7,11,15,42)]

# 3. 데이터 재구성
install.packages('reshape')
library(reshape)

# melt로 데이터 재구성
# 출산율합계
data_birth<-data.frame(data_birth) # df로 변환
data_birth <- data_birth[c(1:15),] # 20년도까지만 추출
data_birth <- melt(data_birth,id.vars=c('시점')) # 시점을 기준으로 각 국가별 데이터 재구성 ( 시점 / 국가 / 값 )
colnames(data_birth)[2]<-'country'
colnames(data_birth)[3]<-'birth_rate' # 컬럼 이름 변경
head(data_birth,100)
data_birth$continent<-c('아시아')
data_birth

# 영아사망률
data_dead<-data.frame(data_dead) # df로 변환
data_dead <- data_dead[c(1:15),] # 20년도까지만 추출
data_dead <- melt(data_dead,id.vars=c('시점')) # 시점을 기준으로 각 국가별 데이터 재구성 ( 시점 / 국가 / 값 )
colnames(data_dead)[2]<-'country' # 컬럼 이름 변경
colnames(data_dead)[3]<-'dead_rate'
head(data_dead,150)

# 1인당 gdp
data_1p_gdp <-data.frame(data_1p_gdp) # df로 변환
#data_1p_gdp <- data_dead[c(1:15),] # 20년도까지만 추출
data_1p_gdp <- melt(data_1p_gdp,id.vars=c('시점')) # 시점을 기준으로 각 국가별 데이터 재구성 ( 시점 / 국가 / 값 )
colnames(data_1p_gdp)[2]<-'country' # 컬럼 이름 변경
colnames(data_1p_gdp)[3]<-'data_1p_gdp'
data_1p_gdp <- data_1p_gdp[data_1p_gdp$시점 %in% seq(1960,2020,5),]
data_1p_gdp
head(data_1p_gdp,150)

# 데이터 합침




library(esquisse)
esquisse::esquisser()

library(plotly)
plot
m %>%
    plot_ly(x = ~ 시점,
            y = ~ value,
            name = ~ country,
            hoverinfo = 'x + y + name')

library(esquisse)
esquisse::esquisser()

library(ggplot2)

p <-ggplot(data = m, aes(x = 시점, y = value, col = country)) + geom_line(aes(group=1)) 
p

m
m %>%
    plot_ly(x = ~ 시점,
            y = ~ value,
            name = ~ country,
            hoverinfo = 'x + y + name ')
