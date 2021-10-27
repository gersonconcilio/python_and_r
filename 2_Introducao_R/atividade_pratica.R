#PRIMEIRO EXERCICIOS
ana <- 8L
paulo <- 11L
ifelse(ana > paulo, "A Menina eh mais velha!", "O menino eh mais velho!")


#SEGUNDO EXERCICIO
class(BOD)


#TERCEIRO EXERCICIO
vet <- c()
for (i in 1:10) {
    vet[i] <- i
}
vet
for (i in vet) {
    if (vet[i] %% 2 == 0)
        print(vet[i])
}


#QUARTO EXERCICIO
tail(women, n <- 10)


#QUINTO EXERCICIO
x <- iris$Sepal.Width[50:100]
y <- iris$Petal.Length[50:100]
plot(x, y)
#novairis <- iris[50:100, c(2, 3)]
#plot(novairis)


#SEXTO EXERCICIO
vet1 <- c()
vet2 <- c()
for (i in 1:5) {
    vet1[i] <- i
    vet2[i] <- i
}
vet1
vet2
print(vet1 + vet2)


#SÉTIMO EXERCICIO
x <- length(colnames(CO2))
y <- length(rownames(CO2))
cat(sprintf("O numero de colunas eh: %i", x))
sprintf("O nome das colunas: ")
colnames(CO2)
cat(sprintf("O numero de linhas eh: %i", y))
sprintf("O nome das linhas: ")
rownames(CO2)
#dim(CO2)[1]
#dim(CO2)[2]
#rownames(CO2)
#colnames(CO2)