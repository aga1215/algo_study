#include <string>
#include <vector>
#include <stack>

using namespace std;

vector<int> solution(vector<int> prices) {
    int len = prices.size();
    int price_time[10000] = {};
    int current = prices.at(len - 1);
    int time = 0;
    vector<int> answer(len);
    answer.at(len - 1) = 0;
    
    for(int i = len - 2; i >= 0; i --)
    {
        time++;
        current = prices.at(i);
        int last = prices.at(i + 1);
        
        if (current > last)
        {
            for(int j = last; j < current; j ++)
            {
                price_time[j] = time - 1;
            }
        }

        int last_time = price_time[current - 1];
        answer.at(i) = time - last_time;
    }
    
    return answer;
}