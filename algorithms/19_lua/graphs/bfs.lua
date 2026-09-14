local M = {}

function M.bfs(graph, start)
    local visited = {}
    local queue = {start}
    local order = {}
    visited[start] = true

    while #queue > 0 do
        local node = table.remove(queue, 1)
        table.insert(order, node)
        for _, neighbor in ipairs(graph[node] or {}) do
            if not visited[neighbor] then
                visited[neighbor] = true
                table.insert(queue, neighbor)
            end
        end
    end
    return order
end

return M
