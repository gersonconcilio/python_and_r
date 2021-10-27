library(xlsx)

#DUAS FORMAS DE ABRIR ARQUIVO

#PRIMEIRA FORMA
x <- read.csv(file.choose(), header <- TRUE, sep <- ",")
x

#SEGUNDA FORMA
x <- read.csv("caminho.csv", header <- TRUE, sep <- ",")

#ARQUIVOS EXCEL (NOME DO ARQUIVO, NÚMERO DA PLANILHA)
dados <- read.xlsx("nome.xlsx", sheetIndex = 1)