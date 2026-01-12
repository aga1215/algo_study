#include <string>
#include <vector>
#include <unordered_map>

using namespace std;

bool solution(vector<string> phone_book) {
    
    unordered_map<string, int> hash;
    
    for(auto p : phone_book)
    {
        hash.emplace(make_pair(p, 0));
    }
    
    for(auto p : phone_book)
    {
        string pref = "";
        for(int i = 0; i < p.size(); i ++)
        {
            pref += p[i];
            if(hash.count(pref) && pref != p) return false;
        }
    }
    
    bool answer = true;
    return answer;
}