import random

class Particle:
    def __init__(self, dim, lower_limit, upper_limit):
        self.position = [random.uniform(lower_limit, upper_limit) for _ in range(dim)]
        self.velocity = [random.uniform(-1, 1) for _ in range(dim)]
        self.best_position = self.position
        self.best_fitness = float('inf')

def objective_function(x):
    # 以最小化为目标的示例函数
    return sum(xi**2 for xi in x)

def update_velocity(particle, global_best_position, inertia_weight, cognitive_weight, social_weight):
    for i in range(len(particle.velocity)):
        r1, r2 = random.random(), random.random()
        cognitive_component = cognitive_weight * r1 * (particle.best_position[i] - particle.position[i])
        social_component = social_weight * r2 * (global_best_position[i] - particle.position[i])
        inertia_component = inertia_weight * particle.velocity[i]
        particle.velocity[i] = inertia_component + cognitive_component + social_component

def update_position(particle):
    for i in range(len(particle.position)):
        particle.position[i] += particle.velocity[i]

def pso_algorithm(dim, population_size, iterations, lower_limit, upper_limit, cognitive_weight, social_weight, inertia_weight):
    particles = [Particle(dim, lower_limit, upper_limit) for _ in range(population_size)]

    global_best_particle = min(particles, key=lambda p: objective_function(p.position))

    for _ in range(iterations):
        for particle in particles:
            fitness = objective_function(particle.position)

            if fitness < particle.best_fitness:
                particle.best_fitness = fitness
                particle.best_position = particle.position

            if fitness < global_best_particle.best_fitness:
                global_best_particle = particle

        for particle in particles:
            update_velocity(particle, global_best_particle.best_position, inertia_weight, cognitive_weight, social_weight)
            update_position(particle)

    return global_best_particle.best_position

# 使用粒子群算法优化目标函数
result = pso_algorithm(dim=2, population_size=30, iterations=100, lower_limit=-10, upper_limit=10, cognitive_weight=1.5, social_weight=1.5, inertia_weight=0.7)
print("Optimal solution:", result)
