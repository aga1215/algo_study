#include <iostream>
#include<string>
#include<stack>
using namespace std;

int solution(string s)
{
    stack<char> str;
    int len = s.size();
    
    for(int i = 0; i < len; i ++)
    {
        if (str.size() > 0)
        {
            char top = str.top();
        
            if (top == s[i]) str.pop();
            else str.push(s[i]);
        }
        else str.push(s[i]);
    }

    return str.size() == 0;
}