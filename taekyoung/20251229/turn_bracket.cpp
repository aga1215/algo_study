#include <stack>
#include <string>
#include <vector>

using namespace std;
bool is_correct_bracket(string s);

int solution(string s) {
    int answer = 0;
    int s_size = s.size();
    
    for(int i = 0; i < s_size; i ++)
    {
        s = s.substr(1, s_size - 1) + s[0];
        if (is_correct_bracket(s)) answer++;
    }
    
    return answer;
}

bool is_correct_bracket(string s)
{
    stack<char> brackets;
    
    for(int i = 0; i < s.size(); i++)
    {
        if (s[i] == '(' || s[i] == '{' || s[i] == '[')
        {     
            brackets.push(s[i]);
        }
        else
        {
            if (brackets.size() == 0) return false;
            
            char top = brackets.top();
            if (top == s[i] - 1 || top == s[i] - 2)
            {
                brackets.pop();
            }
            else return false;
        }
    }
    return brackets.size() == 0;
}