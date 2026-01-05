#include <string>
#include <vector>
#include <queue>

using namespace std;

vector<int> solution(vector<int> progresses, vector<int> speeds) {
    vector<int> answer;
    queue<int *> q;
    int len = progresses.size();
    
    for(int i = 0; i < len; i ++)
    {
        q.push(&progresses[i]);
    }
    
    while(!q.empty())
    {
        for(int i = 0; i < len; i ++)
        {
            progresses[i] += speeds[i];
        }

        int sol = 0;
        while(!q.empty() && *q.front() >= 100)
        {
            sol++;
            q.pop();
        }
        if (sol > 0) answer.push_back(sol);
    }
    
    return answer;
}