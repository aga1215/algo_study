#include <string>
#include <sstream>
#include <vector>
#include <unordered_map>
#include <iostream>

using namespace std;

int strcmp(string str1, string str2)
{
    int str1_len = str1.size();
    int str2_len = str2.size();
    
    int min = str1_len > str2_len ? str2_len : str1_len;
    
    for(int i = 0; i < min; i ++)
    {
        if (str1[i] > str2[i]) return 1;
        else if (str1[i] < str2[i]) return -1;
    }
    
    if (str1_len > str2_len) return 1;
    else return -1;
}

int solution(vector<string> friends, vector<string> gifts) {
    
    unordered_map<string, int> record;
    unordered_map<string, int> score;
    unordered_map<string, int> result;
    
    int fr_len = friends.size();
    
    for(int i = 0; i < fr_len - 1; i ++)
    {
        for(int j = i + 1; j < fr_len; j ++)
        {
            string str1 = friends[i];
            string str2 = friends[j];
            
            if (strcmp(str1, str2) > 0)
            {
                record[str1 + ' ' + str2] = 0;
            }
            else
            {
                record[str2 + ' ' + str1] = 0;         
            }   
        }
    }
    
    for(auto g : gifts)
    {
        istringstream ss(g);
        string str1, str2, temp;
        int reversed = 1;
        
        getline(ss, str1, ' ');
        getline(ss, str2, ' ');
        
        score[str1]++;
        score[str2]--;
                
        if (strcmp(str1, str2) < 0)
        {
            temp = str2;
            str2 = str1;
            str1 = temp;
            reversed = -1;
        }
        
        //cout << str1 + ", " + str2 + " : " << reversed << endl;
        
        record[str1 + " " + str2] += reversed;
    }
    
    //cout << endl;
    
    for(auto r : record)
    {
        //cout << r.first << ", " << r.second << endl;
        
        istringstream ss(r.first);
        string str1, str2;
        
        getline(ss, str1, ' ');
        getline(ss, str2, ' ');
        
        int record_score = r.second;
        
        if (record_score > 0)
        {
            result[str1]++;
        }
        else if (record_score < 0)
        {
            result[str2]++;
        }
        else
        {
            int score_first = score[str1];
            int score_second = score[str2];
            
            if (score_first > score_second)
            {
                result[str1]++;    
            }
            else if (score_second > score_first)
            {
                result[str2]++;
            }
        }
    }
    
    int answer = 0;
    for(auto r : result)
    {
        if (r.second > answer) answer = r.second;
    }
    
    return answer;
}