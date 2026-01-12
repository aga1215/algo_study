#include <string>
#include <vector>
#include <unordered_map>

using namespace std;

int solution(vector<vector<string>> clothes) {
    
    unordered_map<string, int> hashmap;
    
    for(auto c : clothes)
    {
        hashmap[c[1]]++;
    }
    
    int mult = 1;
    
    for(auto h : hashmap)
    {
        mult *= (h.second + 1);
    }
    
    int answer = mult - 1;
    return answer;
}