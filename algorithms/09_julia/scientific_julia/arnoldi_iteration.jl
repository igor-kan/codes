module ArnoldiIteration
export arnoldi_basis_dim

function arnoldi_basis_dim(m_steps::Int)
    return m_steps + 1
end
end
