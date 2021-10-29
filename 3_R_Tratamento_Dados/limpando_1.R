dados <- read.csv("Churn.csv", sep = ";", na.strings = "", stringsAsFactors = T)
colnames(dados) <- c("Id", "Score", "Estado", "Genero", "Idade", "Patrimonio", "Saldo", "Produtos", "Tem_Cart_Credito",
 "Ativo", "Salario", "Saiu")


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
dados[duplicated(dados$Id), ]
dados