
df <- read.csv('./HousePrices.csv',header=T)
df <- df[,c('Id', 'MSSubClass')]
df
dim(df)
str(df)

library(VIM)
aggr(df, numbers=T,prop=F)

barplot(df$SalePrice)
 

#차고 관련 데이터
colnames(df)
df_car <- df[,c(59:65,81)]
table(df$GarageType)
table(df$GarageYrBlt)
table(df$GarageFinish)
table(df$GarageCars)
table(df$GarageArea) #평방 피트에 있는 차고의 크기
table(df$GarageQual)
table(df$GarageCond)
df$GarageArea

aggr(df$GarageType, numbers=T,prop=F)
aggr(df$GarageYrBlt, numbers=T,prop=F)
aggr(df$GarageFinish, numbers=T,prop=F)
aggr(df$GarageCond, numbers=T,prop=F)
table(df$GarageQual)

aggr(df$GarageCars, numbers=T,prop=F)
aggr(df$GarageArea, numbers=T,prop=F)

# 결측치제거 : 차가없는집은 차고데이터가 없음.
# row = 1460
dim(df_car)
df<- na.omit(df)
str(df)
# row = 1379
dim(df)

plot(df_car$GarageType,df_car$SalePrice,pch=19)
subplot(2,3)
df_car_agg <- aggregate(df_car$SalePrice,
          by=list(df_car$GarageType),
          FUN=mean)
barplot(df_car_agg$x,
        axisnames = TRU
        ,col=1:6)

str(df_car_agg)
df_car_agg$Group.1
?barplot

install.packages('ggplot2')
library(ggplot2)

df <- read.csv('./HousePrices.csv',header=T)
par(mar = c(1, 1, 1, 1))
par(mfrow = c(3,2))

# 차고관련 범주형 데이터 
boxplot(SalePrice~GarageType,data = df,pch=19, 
        col ="orange", border ="brown")
boxplot(SalePrice~GarageFinish,data = df,pch=19, 
        col ="orange", border ="brown")
boxplot(SalePrice~GarageCars,data = df,pch=19, 
        col ="orange", border ="brown")
boxplot(SalePrice~GarageQual,data = df,pch=19, 
        col ="orange", border ="brown")
boxplot(SalePrice~GarageCond,data = df,pch=19, 
        col ="orange", border ="brown")
par(mfrow =c(1,1))

# 차고 관련 수치형 데이터

par(mfrow=c(1,2))
plot(df$GarageYrBlt,df$SalePrice)
plot(df$SalePrice~df$GarageArea)
par(mfrow=c(1,1))

# 수치형 데이터 : 범주 팩터 너무 많음, 범위 구분하고싶은데 안됨 ㅜㅜ
year_t <- table(df$GarageYrBlt)
names(year_t)

barplot(year_t,names.arg=names(year_t))
plot(df$GarageYrBlt,df$SalePrice)
plot(df$SalePrice~df$GarageArea)

df <- df[,c(59:65,81)]
df <- na.omit(df)
plot(df$SalePrice,df$GarageArea,pch=20,col=as.numeric(factor(df$GarageType))+1)
as.numeric(factor(df$GarageType))

ggplot(df, aes(y=SalePrice,x=GarageArea,color=factor(GarageCars)))+geom_point()
as.numeric(factor(df$GarageType))

plot(df$SalePrice,df$GarageArea,pch=20,col=as.numeric(factor(df$GarageFinish))+1)
as.numeric(factor(df$GarageType))

plot(df$SalePrice,df$GarageArea,pch=20,col=as.numeric(factor(df$GarageQual))+1)
as.numeric(factor(df$GarageType))

plot(df$SalePrice,df$GarageArea,pch=20,col=as.numeric(factor(df$GarageCond))+1)
as.numeric(factor(df$GarageType))df$GarageYrBlt



pairs(df, panel=panel.smooth)

install.packages("corrplot")
library(corrplot)

df <- read.csv('./HousePrices.csv',header=T)
df <- df[,c('SalePrice','GarageArea','GarageYrBlt')]
df <- na.omit(df)
corrplot(cor(df), method='number')


colnames(df)
str(df)
df <- read.csv('./HousePrices.csv',header=T)
df <- df[,c(52:55,81)]
df
table(df$BedroomAbvGr)
table(df$KitchenAbvGr) #뺌
table(df$KitchenQual)
table(df$TotRmsAbvGrd)
str(df)
factor(df$KitchenQual)

barplot(table(df$BedroomAbvGr))
barplot(table(df$KitchenQual))
barplot(table(df$TotRmsAbvGrd))

boxplot(df$SalePrice~df$BedroomAbvGr)
boxplot(df$SalePrice~df$KitchenQual)
boxplot(df$SalePrice~df$TotRmsAbvGrd)

df <- read.csv('./HousePrices.csv',header=T)
df
df <- df[,c(52,53,55,81)]
corrplot(cor(df), method='number')

str(df)
colnames(df)



