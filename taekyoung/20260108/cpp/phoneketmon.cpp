#include <vector>
#include <unordered_map>
using namespace std;

int solution(vector<int> nums)
{
    int max = nums.size() / 2;
    unordered_map<int, int> pkms;
    
    
    for(auto p : nums)
    {
        pkms[p]++;
    }
    
    int var_cnt = pkms.size();
    
    int answer = var_cnt > max ? max : var_cnt;
    return answer;
}