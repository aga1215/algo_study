#include <string>
#include <vector>

using namespace std;

string solution(vector<string> cards1, vector<string> cards2, vector<string> goal) {
    
    string answer;
    int one_len = cards1.size();
    int two_len = cards2.size();
    int one_i = 0, two_i = 0;
    
    for (auto word : goal)
    {
        string one_word = "";
        string two_word = "";
        
        if (one_i < one_len) one_word = cards1[one_i];
        if (two_i < two_len) two_word = cards2[two_i];
        
        if (word == one_word) one_i++;
        else if (word == two_word) two_i++;
        else return "No";
    }
    
    return "Yes";
}