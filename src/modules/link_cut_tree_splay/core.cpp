#include "interface.hpp"
#include <algorithm>
#include <limits>

namespace codes_link_cut_tree_splay {

LinkCutTree::LinkCutTree(int n) : nodes_(n) {
    for (int i = 0; i < n; ++i) {
        nodes_[i].val = 0;
        nodes_[i].sum = 0;
        nodes_[i].max_val = 0;
    }
}

bool LinkCutTree::is_root(int x) const {
    int p = nodes_[x].parent;
    if (p == -1) return true;
    return nodes_[p].ch[0] != x && nodes_[p].ch[1] != x;
}

void LinkCutTree::push(int x) {
    if (x == -1 || !nodes_[x].rev) return;
    std::swap(nodes_[x].ch[0], nodes_[x].ch[1]);
    if (nodes_[x].ch[0] != -1) nodes_[nodes_[x].ch[0]].rev ^= true;
    if (nodes_[x].ch[1] != -1) nodes_[nodes_[x].ch[1]].rev ^= true;
    nodes_[x].rev = false;
}

void LinkCutTree::pull(int x) {
    nodes_[x].sum = nodes_[x].val;
    nodes_[x].max_val = nodes_[x].val;
    for (int side = 0; side < 2; ++side) {
        int c = nodes_[x].ch[side];
        if (c != -1) {
            nodes_[x].sum += nodes_[c].sum;
            nodes_[x].max_val = std::max(nodes_[x].max_val, nodes_[c].max_val);
        }
    }
}

void LinkCutTree::rotate(int x) {
    int p = nodes_[x].parent;
    int g = nodes_[p].parent;
    int dir = (nodes_[p].ch[1] == x) ? 1 : 0;
    int b = nodes_[x].ch[dir ^ 1];
    if (!is_root(p)) {
        if (nodes_[g].ch[0] == p) nodes_[g].ch[0] = x;
        else if (nodes_[g].ch[1] == p) nodes_[g].ch[1] = x;
    }
    nodes_[x].parent = g;
    nodes_[x].ch[dir ^ 1] = p;
    nodes_[p].parent = x;
    nodes_[p].ch[dir] = b;
    if (b != -1) nodes_[b].parent = p;
    pull(p);
    pull(x);
}

void LinkCutTree::splay(int x) {
    std::vector<int> stack;
    int cur = x;
    stack.push_back(cur);
    while (!is_root(cur)) {
        cur = nodes_[cur].parent;
        stack.push_back(cur);
    }
    for (int i = static_cast<int>(stack.size()) - 1; i >= 0; --i) push(stack[i]);
    while (!is_root(x)) {
        int p = nodes_[x].parent;
        int g = nodes_[p].parent;
        if (!is_root(p)) {
            bool zigzig = ((nodes_[p].ch[0] == x) == (nodes_[g].ch[0] == p));
            rotate(zigzig ? p : x);
        }
        rotate(x);
    }
}

void LinkCutTree::access(int x) {
    int last = -1;
    for (int y = x; y != -1; y = nodes_[y].parent) {
        splay(y);
        nodes_[y].ch[1] = last;
        pull(y);
        last = y;
    }
    splay(x);
}

void LinkCutTree::make_root(int u) {
    validate_vertex(size(), u);
    access(u);
    nodes_[u].rev ^= true;
    push(u);
}

int LinkCutTree::find_root(int u) {
    validate_vertex(size(), u);
    access(u);
    while (nodes_[u].ch[0] != -1) {
        push(u);
        u = nodes_[u].ch[0];
    }
    splay(u);
    return u;
}

bool LinkCutTree::connected(int u, int v) {
    validate_vertex(size(), u);
    validate_vertex(size(), v);
    if (u == v) return true;
    return find_root(u) == find_root(v);
}

bool LinkCutTree::link(int u, int v) {
    make_root(u);
    if (find_root(v) == u) return false;
    nodes_[u].parent = v;
    return true;
}

bool LinkCutTree::cut(int u, int v) {
    make_root(u);
    if (find_root(v) != u || nodes_[v].parent != u || nodes_[v].ch[0] != -1) {
        return false;
    }
    nodes_[v].parent = -1;
    nodes_[u].ch[1] = -1;
    pull(u);
    return true;
}

void LinkCutTree::set_value(int u, std::int64_t val) {
    validate_vertex(size(), u);
    access(u);
    nodes_[u].val = val;
    pull(u);
}

std::int64_t LinkCutTree::query_path_sum(int u, int v) {
    if (!connected(u, v)) throw std::invalid_argument("vertices disconnected");
    make_root(u);
    access(v);
    return nodes_[v].sum;
}

std::int64_t LinkCutTree::query_path_max(int u, int v) {
    if (!connected(u, v)) throw std::invalid_argument("vertices disconnected");
    make_root(u);
    access(v);
    return nodes_[v].max_val;
}

} // namespace codes_link_cut_tree_splay
