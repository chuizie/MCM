import random

# 目标函数，例如最小化的函数
def objective_function(x):
    return x**2

# 初始化种群
def initialize_population(population_size, lower_limit, upper_limit):
    return [random.uniform(lower_limit, upper_limit) for _ in range(population_size)]

# 评估适应度
def evaluate_fitness(population):
    return [objective_function(individual) for individual in population]

# 选择父代
def select_parents(population, fitness_values):
    # 这里简单地选择适应度较高的两个个体作为父代
    sorted_indices = sorted(range(len(fitness_values)), key=lambda k: fitness_values[k])
    return population[sorted_indices[-2:]]

# 交叉操作
def crossover(parent1, parent2):
    # 一种简单的交叉方式，取两个父代的平均值
    return (parent1 + parent2) / 2.0

# 变异操作
def mutate(individual, mutation_rate, lower_limit, upper_limit):
    # 随机决定是否进行变异，以及变异的程度
    if random.uniform(0, 1) < mutation_rate:
        mutation_amount = random.uniform(-0.5, 0.5)
        individual += mutation_amount
        # 限制变异后的值在合理范围内
        individual = max(lower_limit, min(upper_limit, individual))
    return individual

# 遗传算法主循环
def genetic_algorithm(population_size, generations, mutation_rate, lower_limit, upper_limit):
    population = initialize_population(population_size, lower_limit, upper_limit)

    for generation in range(generations):
        fitness_values = evaluate_fitness(population)
        parents = select_parents(population, fitness_values)

        # 生成下一代种群
        new_population = [crossover(*parents) for _ in range(population_size // 2)]

        # 变异
        new_population = [mutate(individual, mutation_rate, lower_limit, upper_limit) for individual in new_population]

        # 更新种群
        population = new_population

    # 返回最终的最优解
    best_solution = min(population, key=objective_function)
    return best_solution

# 使用遗传算法优化目标函数
result = genetic_algorithm(population_size=50, generations=100, mutation_rate=0.1, lower_limit=-10, upper_limit=10)
print("Optimal solution:", result)