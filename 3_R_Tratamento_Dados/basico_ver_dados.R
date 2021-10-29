dados <- read.csv("Churn.csv", sep = ";", na.strings = "", stringsAsFactors = T)

#head(dados)
#summary(dados)

colnames(dados) <- c("Id", "Score", "Estado", "Genero", "Idade", "Patrimonio", "Saldo", "Produtos", "Tem_Cart_Credito",
 "Ativo", "Salario", "Saiu")

 head(dados)

#AQUI É AGRUPADO EM TABELA UNICA OS DADOS DE TABELAS ESCOLHIDAS
counts <- table(dados$Estado)
counts
barplot(counts, main = "Estados", xlab = "Estados")

gnder <- table(dados$Genero)
gnder
barplot(gnder, main = "Genero", xlab = "Genero")

# summary(dados$Score)
# boxplot(dados$Score)
# hist(dados$Score)

summary(dados$Idade)

summary(dados$Saldo)