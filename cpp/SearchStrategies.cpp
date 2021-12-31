#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <iterator>

template<typename T>
struct TreeNode
{
    T value;
    TreeNode *left;
    TreeNode *right;
    TreeNode *parent;
};

struct Graph
{
    int num_nodes; 
    std::vector<std::vector<int>> edges;
    bool directed;
    bool weighted;
    std::vector<std::vector<int>> data;
    std::vector<std::vector<int>> weights;

    Graph(int num_nodes, std::vector<std::vector<int>> edges, bool directed=false, bool weighted=false)
    {
        this->num_nodes = num_nodes;
        this->edges = edges;
        this->directed = directed;
        this->weighted = weighted;

        for (auto edge : edges)
        {
            if (weighted)
            {
                int node1 = edge[0];
                int node2 = edge[1];
                int weight = edge[2];

                this->data[node1].push_back(node2);
                this->weights[node1].push_back(weight);

                if (!directed)
                {
                    this->data[node2].push_back(node1);
                    this->weights[node1].push_back(weight);
                }

            }

            else
            {
                int node1 = edge[0];
                int node2 = edge[1];

                this->data[node1].push_back(node2);
                if (!directed)
                    this->data[node2].push_back(node1);
            }
        }
    }

    // void represent()
    // {
    //     std::string result = "";
    //     if (this->weighted)
    //     {

    //     }
    // }
};

int main()
{
    int num_nodes1 = 5;
    std::vector<std::vector<int>> edges1 = {{0, 1}, {0, 4}, {1, 2}, {1, 3}, {1, 4}, {2, 3}, {3, 4}};

    Graph g1(num_nodes1, edges1);
    
    for (int i=0; i<g1.weights.size(); i++)
        for (int j=0; j<g1.weights[i].size(); j++)
            std::cout << i << " : " << g1.weights[i][j] << std::endl;
    
    return 0;
}
