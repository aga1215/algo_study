#include <string>
#include <vector>
#include <stack>
#include <iostream>

using namespace std;

int solution(vector<vector<int>> board, vector<int> moves) {
    int len = board.size();
    int move_len = moves.size();
    vector<int> pivots(len, 0);
    stack<int> pops;
    int answer = 0;
    
    for(int i = 0; i < move_len; i ++)
    {
        int move = moves.at(i) - 1;
        int pivot = pivots.at(move);
        int item = 0;
        
        if (pivot >= len) continue;
        
        do
        {
            item = board[pivot++][move];
        }while(item == 0);
        
        pivots.at(move) = pivot;
        
        if (pops.size() > 0)
        {
            int top = pops.top();
            if (top == item)
            {
                answer += 2;
                pops.pop();
            }
            else
            {
                pops.push(item);             
            }
        }
        else
        {
            pops.push(item);
        }   
    }

    return answer;
}