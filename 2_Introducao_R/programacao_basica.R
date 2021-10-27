#IF
a <- 10
b <- 14
if (a == b) {
    print("Verdadeiro!")
}else {
    print("Falso!")
}

#IFELSE
a <- 10
b <- 2
x <- ifelse(b > a, x <- b, "FALSO")
x

#FOR
for (i in 1:10) {
    print(i)
}

#WHILE
a <- 0
while (a <= 10) {
    print(a)
    a <- a + 1
}

#FUNÇÃO PAR OU IMPAR
even_or_odd <- function(x) {
    return(ifelse(x %% 2 == 0, "PAR", "IMPAR"))
}

even_or_odd(2)
even_or_odd(3)