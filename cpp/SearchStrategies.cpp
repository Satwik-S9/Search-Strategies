#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <iterator>

// zip function as inbuilt in python
template <typename T, typename P>
void zip()
{

}

class Graph
{
    int num_nodes; 
    std::vector<std::vector<int>> edges;
    bool directed;
    bool weighted;
    std::vector<std::vector<int>> data;
    std::vector<std::vector<int>> weights;

public:
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

    void represent()
    {
        
    }
};

int main()
{
    return 0;
}