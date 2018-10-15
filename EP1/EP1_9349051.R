##
# PCS3438 - Inteligência Artificial
#
# Daniel Nery Silva de Oliveira - 9349051
#
# Resolve o Problema do Caixeiro Viajante a partir
# de uma matriz de adjacências dada num arquivo CSV
# no formato especificado, utilizando a biblioteca
# TSP do CRAN:
#
# Ver: https://cran.r-project.org/web/packages/TSP/vignettes/TSP.pdf
#
# 09/2018
##

library('TSP')

## Função principal
EP1_9349051 <- function(entrada, saida) {
    # Lê o arquivo de entrada
    dados <- read.table(
        entrada,
        header = TRUE,
        sep = ',')

    # Transforma os dados lidos numa matriz de
    # adjacencias
    dados <- as.dist(dados)

    # Transforma a matriz num objeto da classe
    # TSP, para ser resolvido
    tsp <- TSP(dados)

    # Computa o momento inicial de processamento
    initial_time <- Sys.time()

    # Resolve o TSP, usando o método da biblioteca
    # arbitrary insertion
    solved_tsp <- solve_TSP(tsp, method="arbitrary_insertion")

    # Extrai as informações necessárias da solução
    # Computa o tempo total de solução, a rota
    # começando pela cidade 1 e custo total
    execution_time <- as.numeric(Sys.time() - initial_time)
    tour <- cut_tour(solved_tsp, 1, exclude_cut=FALSE)
    total_cost <- tour_length(solved_tsp)

    # Imprime dados relevantes na tela
    cat(sprintf("Custo: %f\n", total_cost))
    cat(sprintf("Tempo de Execução: %fs\n", execution_time))
    cat("Rota:")
    for (city in tour) {
        cat(sprintf(" %d", city))
    }
    cat("\n")

    # Escreve os dados pedidos no arquivo de saída
    results <- matrix(c(total_cost, execution_time, tour), nrow=1)
    write.table(
        results,
        file=saida,
        sep=',',
        row.names=FALSE,
        col.names=FALSE)
}
