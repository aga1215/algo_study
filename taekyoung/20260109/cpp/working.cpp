#include <string>
#include <vector>
#include <iostream>

using namespace std;

int solution(vector<int> schedules, vector<vector<int>> timelogs, int startday) {
    
    int len =  schedules.size();
    int sat = startday == 7 ? 6 : 6 - startday;
    int sun = 7 - startday;
    int answer = 0;

    for(int i = 0; i < len; i ++)
    {
        int maginot = schedules[i] + 10;
        int remain = maginot % 100;
        if (remain >= 60)
        {
            maginot += 40;
        }
        
        bool recieve = true;
        for(int j = 0; j < 7; j ++)
        {
            if (j == sat || j == sun) continue;
            if (timelogs[i][j] > maginot) recieve = false;
        }
        answer += recieve;
    }
    
    return answer;
}