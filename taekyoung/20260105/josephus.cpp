#include <iostream>
#include <vector>
#include <string>

using namespace std;

class Node
{
    public:
        Node(){};
        Node(int value)
        {
            m_value = value;
        }
        int m_value;
        Node *m_next;
};

Node *create_list(int n, Node *head)
{
    Node *last = head;

    for(int i = 2; i <= n; i ++)
    {
        Node *temp = new Node(i);
        last->m_next = temp;
        last = temp;
    }
    last->m_next = head;

    return last;
}

void solution(int n, int k)
{
    vector<int> answer;
    Node *head = new Node(1);
    Node *tail = create_list(n, head);

    Node *cur = head;
    Node *last = tail;
    Node *temp;
    
    while(true)
    {
        for(int i = 0; i < k - 1; i ++)
        {
            cur = cur->m_next;
            last = last->m_next;
        }
        answer.push_back(cur->m_value);
        last->m_next = cur->m_next;

        if (cur == cur->m_next) 
        {
            delete cur;
            break;
        };

        temp = cur;
        cur = cur->m_next;
        delete temp;
    }

    int size = answer.size();
    cout << "<";
    for(int i = 0; i < size - 1; i ++)
    {
        cout << answer[i] << ", ";
    }
    cout << answer[size - 1] << ">" << endl;
}

int main(int argc, char *argv[])
{
    int n, k;
    cin >> n >> k;

    solution(n, k);
}