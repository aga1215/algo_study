#include<string>
#include <iostream>
#include <stack>

using namespace std;

bool solution(string s)
{
    stack<char> bracket_stack;
    int str_size = s.size();
    
    for(int i = 0; i < str_size; i ++)
    {
        char bracket = s[i];
        
        if (bracket == '(')
        {
            bracket_stack.push(bracket);
        }
        else if (bracket == ')')
        {
            if (bracket_stack.empty())
            {
                return false;
            }
            else
            {
                bracket_stack.pop();
            }
        }
    }

    return bracket_stack.empty();
}