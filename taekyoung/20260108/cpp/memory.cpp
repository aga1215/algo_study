#include <string>
#include <vector>
#include <unordered_map>

using namespace std;

vector<int> solution(vector<string> name, vector<int> yearning, vector<vector<string>> photo) {
    
    int name_len = name.size();
    int photo_len = photo.size();
    vector<int> answer(photo_len);
    unordered_map<string, int> misses;
    
    for(int i = 0; i < name_len; i ++)
    {
        misses[name[i]] = yearning[i];
    }
    
    for(int i = 0; i < photo_len; i ++)
    {
        int miss = 0;
        auto v = photo[i];
        
        for(auto p : v)
        {
            miss += misses[p];
        }
        answer[i] = miss;
    }
    return answer;
}