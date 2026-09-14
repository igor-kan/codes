module MachineLearning

function linear_regression(X::Matrix{Float64}, y::Vector{Float64})
    # Closed-form solution: theta = (X^T X)^-1 X^T y
    # Adding bias term to X
    n = size(X, 1)
    X_b = hcat(ones(n), X)
    theta = inv(X_b' * X_b) * X_b' * y
    return theta
end

function predict(X::Matrix{Float64}, theta::Vector{Float64})
    n = size(X, 1)
    X_b = hcat(ones(n), X)
    return X_b * theta
end

end
