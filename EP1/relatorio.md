# PCS3438 - Inteligência Artificial

Daniel Nery Silva de Oliveira
9349051

---------------

Para a resolução deste Exercício Programa, foi utilizada a biblioteca TSP disponível no CRAN, que pode ser instalado com:

```install.packages('TSP')```

O método escolhido para ser utilizado foi o "Arbitrary Insrtion" para escolha do caminho inicial e "2-Opt" para sua otimização, esse método foi escolhido entre os disponíveis na biblioteca por ter se mostrado o mais eficiente dentre os disponibilizados pela biblioteca, como pode ser visto no gráfico a seguir, gerado a partir de testes num dataset com 1889 cidades:



Esse algoritmo consiste em iniciar o caminho por uma cidade aleatória e a cada passo escolher uma outra cidade aleatória `k` que ainda não esteja no caminho e inseri-la entre duas outras cidades de modo que o crescimento no custo `d(i,k) + d(k,j) - d(i,j)` seja minimizado. O algoritmo para quando todas as cidades estiverem no caminho.



## Referências
https://cran.r-project.org/web/packages/TSP/vignettes/TSP.pdf
