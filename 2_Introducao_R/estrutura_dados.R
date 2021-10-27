#VETORES
vet <- c(1, 2, 3, 4, 5, 6)
vet[3] <- 10
vet

vet_int <- c(1L, 2L, 3L, 4L, 5L, 6L)
vet_int[3] <- 10L
vet_int

vet_char <- c("a", "b", "c", "d", "e")
vet_char[2] <- "h"
vet_char

#MATRIZES
VADeaths
colnames(VADeaths)
rownames(VADeaths)
VADeaths[1:3, ]
VADeaths[c(1, 3, 5), 4]

#DATAFRAME
longley
longley[, 1:3]
longley$Unemployed
longley["GNP"]

#LISTAS
ability.cov
ability.cov$cov
ability.cov[2]