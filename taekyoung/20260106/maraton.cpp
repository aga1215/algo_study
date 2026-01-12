#include <string>
#include <vector>
#include <map>
#include <iostream>

using namespace std;

string solution(vector<string> participant, vector<string> completion) {
    map<string, int> m_part;
    
    for(auto p : participant)
    {
        int n = m_part[p];
        m_part[p] = n + 1;
    }
    
    for(auto c : completion)
    {
        int n = m_part[c];
        if (n - 1)
        {
            m_part[c] = n - 1;
        }
        else
        {
            m_part.erase(c);
        }
    }
    
    string answer = (*m_part.begin()).first;
    return answer;
}