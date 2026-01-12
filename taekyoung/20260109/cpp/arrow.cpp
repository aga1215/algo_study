#include <string>
#include <vector>

using namespace std;
vector<int> make_score(vector<int> info, vector<int> scores, vector<int> &best, int n, int k, int diff, int &best_diff);

vector<int> solution(int n, vector<int> info) {
    
    int len = info.size();
    vector<int> temp(len);
    int score = 0;
    
    for (int i = 0; i < len; i ++)
    {
        score -= info[i] ? 10 - i : 0;
    }
    
    vector<int> answer = make_score(info, temp, temp, n, 0, score, score);

    if (score <= 0) return {-1};
    return answer;
}

vector<int> make_score(vector<int> info, vector<int> scores, vector<int> &best, int n, int k, int diff, int &best_diff)
{
    if (n == 0 || k == 10)
    {       
        scores[k] = n;
        if (diff > best_diff)
        {
            best = scores;
            best_diff = diff;
            return scores;
        }
        else if (best_diff > diff)
        {
            return best;
        }
        else
        {
            for(int i = 10; i >= 0; i --)
            {
                if (scores[i] > best[i])
                {
                    best = scores;
                    best_diff = diff;
                    return scores;
                }
                else if (scores[i] < best[i]) return best;
            }
            return best;
        }
    }
    else
    {
        if (n > info[k])
        {
            vector<int> new_score = scores;
            new_score[k] = info[k] + 1;
            int new_diff = info[k] ? diff + (10 - k) * 2 : diff + (10 - k);
            make_score(info, new_score, best, n - (info[k] + 1), k + 1, new_diff, best_diff);
        }
        make_score(info, scores, best, n, k + 1, diff, best_diff);
    }
    return best;
}