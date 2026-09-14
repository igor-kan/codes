#include <vector>
#include <cmath>
#include <cstdlib>
#include <limits>

using namespace std;

struct Point {
    vector<double> coordinates;
};

double distance(const Point& a, const Point& b) {
    double sum = 0;
    for (size_t i = 0; i < a.coordinates.size(); ++i) {
        sum += pow(a.coordinates[i] - b.coordinates[i], 2);
    }
    return sqrt(sum);
}

vector<int> k_means(const vector<Point>& data, int k, int max_iters) {
    vector<Point> centroids(k);
    for (int i = 0; i < k; ++i) centroids[i] = data[rand() % data.size()];

    vector<int> labels(data.size(), 0);
    for (int iter = 0; iter < max_iters; ++iter) {
        for (size_t i = 0; i < data.size(); ++i) {
            double min_dist = numeric_limits<double>::max();
            for (int j = 0; j < k; ++j) {
                double dist = distance(data[i], centroids[j]);
                if (dist < min_dist) {
                    min_dist = dist;
                    labels[i] = j;
                }
            }
        }
        
        vector<vector<double>> new_centroids(k, vector<double>(data[0].coordinates.size(), 0));
        vector<int> counts(k, 0);
        for (size_t i = 0; i < data.size(); ++i) {
            int cluster = labels[i];
            counts[cluster]++;
            for (size_t d = 0; d < data[i].coordinates.size(); ++d) {
                new_centroids[cluster][d] += data[i].coordinates[d];
            }
        }
        for (int j = 0; j < k; ++j) {
            if (counts[j] == 0) continue;
            for (size_t d = 0; d < new_centroids[j].size(); ++d) {
                centroids[j].coordinates[d] = new_centroids[j][d] / counts[j];
            }
        }
    }
    return labels;
}
