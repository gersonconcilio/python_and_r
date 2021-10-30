setwd("/home/gconcilio/Documents/Programação/Curso Data Science/python_and_r/3_R_Tratamento_Dados")

dados <- read.csv("Churn.csv", sep = ";", na.strings = "", stringsAsFactors = T)

colnames(dados) <- c("Id", "Score", "Estado", "Genero", "Idade", "Patrimonio", "Saldo", "Produtos", "Tem_Cart_Credito",
 "Ativo", "Salario", "Saiu")

 dados

#-----------TRATANDO  SALÁRIO ----------------
print("\n")
dados[!complete.cases(dados), ]
dados[is.na(dados$Salario), ]

summary(dados$Salario)
median(dados$Salario, na.rm = T)

dados[is.na(dados$Salario), ]$Salario <- median(dados$Salario, na.rm = T)
dados[!complete.cases(dados$Salario)]


#FALTA DE PADRONIZAÇÃO DE GENERO
unique(dados$Genero)
summary(dados$Genero)

dados[is.na(dados$Genero) | dados$Genero == "M", ]$Genero <- "Masculino"
dados[dados$Genero == "Fem" | dados$Genero == "F", ]$Genero <- "Feminino"

dados$Genero <- factor(dados$Genero)


#-----------TRATANDO  IDADE ----------------
summary(dados$Idade)

dados[dados$Idade < 0 | dados$Idade > 110, ]$Idade
dados[is.na(dados$Idade), ]$Idade

dados[dados$Idade < 0 | dados$Idade > 110, ]$Idade <- median(dados$idade)


#-----------DADOS DUPLICADOS ----------------
x <- dados[duplicated(dados$Id), ]
x$Id
dados <- dados[-c(x$Id), ]
dados[dados$Id == x$Id, ]


#-----------ESTADOS FORA DO DOMINIO ----------------
unique(dados$Estado)
summary(dados$Estado)

dados[!dados$Estado %in% c("RS", "SC", "PR", "SP"), ]$Estado <- "RS" 
dados$Estado <- factor(dados$Estado)


#-----------OUTLIERS----------------
des <- sd(dados$Salario, na.rm = T)
des

dados[dados$Salario >= (2 * des), ]$Id
boxplot(dados$Salario)

mediana <- median(dados$Salario)
mediana

dados[dados$Salario >= des, ]$Salario <- mediana
