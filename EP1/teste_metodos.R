#testa todos os metodos do TSP

library('TSP')

dados <- read_TSPLIB('rl1889.tsp')
dados_tsp <- TSP(dados)

results <- matrix(c("method", "cost", "time"), nrow=1)

methods <- c("identity", "random", "nearest_insertion", "farthest_insertion", "cheapest_insertion", "arbitrary_insertion", "nn", "repetitive_nn", "two_opt")
for (met in methods) {
    init <- Sys.time()
    solved_tsp <- solve_TSP(dados_tsp, method=met)
    end <- Sys.time()

    total_cost <- tour_length(solved_tsp)
    execution_time <- as.numeric(end-init)

    results <- rbind(results, c(met, total_cost, execution_time))
}

print(results)
