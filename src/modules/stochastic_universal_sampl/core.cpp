#include "interface.hpp"
#include <algorithm>
#include <cmath>
#include <limits>
#include <numeric>
#include <queue>

namespace codes_stochastic_universal_sampl {

VoseAliasSampler::VoseAliasSampler(const std::vector<double>& weights) : table_(weights.size()) {
    int n = static_cast<int>(weights.size());
    double sum = std::accumulate(weights.begin(), weights.end(), 0.0);
    std::vector<double> scaled(n);
    std::vector<int> small, large;
    for (int i = 0; i < n; ++i) {
        scaled[i] = weights[i] * n / sum;
        if (scaled[i] < 1.0) small.push_back(i);
        else large.push_back(i);
    }
    while (!small.empty() && !large.empty()) {
        int s = small.back(); small.pop_back();
        int l = large.back(); large.pop_back();
        table_[s] = {scaled[s], l};
        scaled[l] = (scaled[l] + scaled[s]) - 1.0;
        if (scaled[l] < 1.0) small.push_back(l);
        else large.push_back(l);
    }
    for (int idx : large) table_[idx] = {1.0, idx};
    for (int idx : small) table_[idx] = {1.0, idx};
}

int VoseAliasSampler::sample_one(int bucket, double u01) const {
    return u01 < table_[bucket].prob ? bucket : table_[bucket].alias;
}

std::vector<int> VoseAliasSampler::stochastic_universal(const std::vector<double>& weights, int m, double u0) const {
    double sum = std::accumulate(weights.begin(), weights.end(), 0.0);
    double step = sum / m;
    std::vector<int> out;
    out.reserve(m);
    double ptr = u0 * step, acc = weights[0];
    int idx = 0;
    for (int k = 0; k < m; ++k) {
        while (ptr > acc && idx + 1 < static_cast<int>(weights.size())) {
            acc += weights[++idx];
        }
        out.push_back(idx);
        ptr += step;
    }
    return out;
}

} // namespace codes_stochastic_universal_sampl
