"""Nelder-Mead downhill simplex minimisation (Numerical Recipes 10.4)."""
def nelder_mead(function, start, step=0.5, tolerance=1e-10, max_iterations=1000):
    n = len(start)
    simplex = [list(start)]
    for i in range(n):
        point = list(start)
        point[i] += step
        simplex.append(point)
    for _ in range(max_iterations):
        simplex.sort(key=function)
        if max(abs(simplex[0][i] - simplex[-1][i]) for i in range(n)) < tolerance:
            break
        centroid = [sum(simplex[j][i] for j in range(n)) / n for i in range(n)]
        worst = simplex[-1]
        reflected = [centroid[i] + (centroid[i] - worst[i]) for i in range(n)]
        if function(simplex[0]) <= function(reflected) < function(simplex[-2]):
            simplex[-1] = reflected
        elif function(reflected) < function(simplex[0]):
            expanded = [centroid[i] + 2.0 * (centroid[i] - worst[i]) for i in range(n)]
            simplex[-1] = expanded if function(expanded) < function(reflected) else reflected
        else:
            contracted = [centroid[i] + 0.5 * (worst[i] - centroid[i]) for i in range(n)]
            if function(contracted) < function(worst):
                simplex[-1] = contracted
            else:
                best = simplex[0]
                for j in range(1, n + 1):
                    simplex[j] = [(best[i] + simplex[j][i]) / 2.0 for i in range(n)]
    simplex.sort(key=function)
    return simplex[0]


if __name__ == "__main__":
    result = nelder_mead(lambda p: (p[0] - 3.0) ** 2 + (p[1] + 2.0) ** 2, [0.0, 0.0])
    assert abs(result[0] - 3.0) < 1e-4 and abs(result[1] + 2.0) < 1e-4
    print("nelder mead ok")
