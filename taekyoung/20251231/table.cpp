#include <string>
#include <vector>
#include <stack>
#include <list>
#include <iostream>

using namespace std;

class Node
{
    public:
        Node(){};
        Node(int value, Node *prev, Node *next)
        {
            m_next = next;
            m_prev = prev;
            m_value = value;
        }
        Node *m_prev;
        int m_value;
        Node *m_next;
};

void create_list(int n, Node *head)
{
    Node *last = head;

    for(int i = 1; i < n; i ++)
    {
        Node *temp = new Node(i, last, nullptr);
        last->m_next = temp;
        last = temp;
    }
}

string solution(int n, int k, vector<string> cmd) {
    stack<Node *> del;
    Node *head = new Node(0, nullptr, nullptr);
    create_list(n, head);
    Node *cur = head;
    Node *top;
    int len = cmd.size();
    
    for(int i = 0; i < k; i ++)
    {
        cur = cur->m_next;
    }
    
    for(int i = 0; i < len; i ++)
    {
        char op = cmd[i][0];
        int move = 0;
        
        //cout << op << " ";
        switch(op)
        {
            case 'U':
                move = stoi(cmd[i].substr(2));
                for(int j = 0; j < move; j ++)
                {
                    if (cur->m_prev) cur = cur->m_prev;
                    else break;
                }
                //cout << move << " " << cur->m_value << " ";
                break;
            case 'D':
                move = stoi(cmd[i].substr(2));
                for(int j = 0; j < move; j ++)
                {
                    if (cur->m_next) cur = cur->m_next;
                    else break;
                }
                //cout << move << " " << cur->m_value << " ";
                break;
            case 'C':
                del.push(cur);
                //cout << cur->m_value << " ";

                if (cur->m_prev)
                {
                    cur->m_prev->m_next = cur->m_next;
                }
                else
                {
                    head = cur->m_next;
                }

                if (cur->m_next)
                {
                    cur->m_next->m_prev = cur->m_prev;
                    cur = cur->m_next;
                }
                else
                {
                    cur = cur->m_prev;
                }
                break;
            case 'Z':
                top = del.top();

                if (top->m_prev)
                {
                    top->m_prev->m_next = top;
                }
                else
                {
                    head = top;
                }

                if (top->m_next)
                {
                    top->m_next->m_prev = top;
                }
                //cout << top->m_value << " ";
                del.pop();
                break;
            default:
                break;
        }
        //cout << endl;
        
        // Node *deb = head;
        // while(deb->m_next)
        // {
        //     cout << deb->m_value << ", ";
        //     deb = deb->m_next;
        // }
        // cout << deb->m_value;
        // cout << endl;
    }

    // Node *deb = head;
    // while(deb->m_next)
    // {
    //     cout << deb->m_value << ", ";
    //     deb = deb->m_next;
    // }
    // cout << deb->m_value;
    // cout << endl;

    string answer = "";
    Node *ans = head;
    for(int i = 0; i < n; i ++)
    {
        if (ans->m_value == i)
        {
            answer.append("O");
            if (ans->m_next)
            {
                ans = ans->m_next;
            }
            else
            {
                ans->m_value = -1;
            }
        }
        else
        {
            answer.append("X");
        }
    }
    return answer;
}