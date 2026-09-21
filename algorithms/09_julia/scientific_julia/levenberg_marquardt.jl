module LevenbergMarquardt
export lm_damping_step

function lm_damping_step(lambda_val::Float64, success::Bool)
    return success ? lambda_val / 10.0 : lambda_val * 10.0
end
end
