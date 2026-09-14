function order = bfs(adj, start)
% BFS Breadth-First Search on adjacency list
    n = length(adj);
    visited = false(1, n);
    queue = start;
    order = [];
    visited(start) = true;
    while ~isempty(queue)
        node = queue(1);
        queue(1) = [];
        order = [order, node];
        for neighbor = adj{node}
            if ~visited(neighbor)
                visited(neighbor) = true;
                queue = [queue, neighbor];
            end
        end
    end
end

function test_bfs()
    fprintf('[Matlab BFS] Testing BFS on adjacency list\n');
    adj = {[2 3], [1 4], [1 5], [2], [3], []};
    result = bfs(adj, 1);
    fprintf('BFS order from 1: ');
    fprintf('%d ', result);
    fprintf('\nExpected: 1 2 3 4 5\n');
    fprintf('[Matlab BFS] Test completed.\n');
end