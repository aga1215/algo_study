#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

typedef struct
{
    int smaller;
    int bigger;
}line;
int *make_locs(const char *dirs, int dirs_len, int *result_len);
int get_line_len(int *locs, int locs_len);

// 파라미터로 주어지는 문자열은 const로 주어집니다. 변경하려면 문자열을 복사해서 사용하세요.
int solution(const char* dirs) {
    
    int result_len = 0;
    int dirs_len = strlen(dirs);
    int *locs = make_locs(dirs, dirs_len, &result_len);
    int answer = get_line_len(locs, result_len);
    return answer;
}

int *make_locs(const char *dirs, int dirs_len, int *result_len)
{
    int x = 0;
    int y = 0;
    int last_loc = 0;
    int locs_len = 0;
    int *locs = (int *)malloc((dirs_len + 1) * sizeof(int));
    
    locs[locs_len++] = 0;
    
    for(int i = 0; i < dirs_len; i ++)
    {
        switch(dirs[i])
        {
            case 'U':
                if (y < 5) y += 1;
                break;
            case 'L':
                if (x > -5) x -= 1;
                break;
            case 'D':
                if (y > -5) y -= 1;
                break;
            case 'R':
                if (x < 5) x += 1;
                break;
        }

        
        int cur_loc = y * 11 + x;        
        if (cur_loc != last_loc)
        {
            last_loc = cur_loc;
            locs[locs_len++] = cur_loc;
        }
    }
    
    *result_len = locs_len;
    
    return locs;
}

int get_line_len(int *locs, int locs_len)
{
    line *lines = (line *)malloc(locs_len * sizeof(line));
    int line_len = 0;
    
    for (int i = 0; i < locs_len - 1; i ++)
    {
        int first = locs[i];
        int second = locs[i + 1];
        int bigger;
        int smaller;
        
        if (first > second)
        {
            bigger = first;
            smaller = second;
        }
        else
        {
            bigger = second;
            smaller = first;
        }
        
        int check = 0;
        
        for (int j = 0; j < line_len; j ++)
        {
            if (lines[j].smaller == smaller && lines[j].bigger == bigger)
            {
                check = -1;
            }
        }
        
        if (check == 0)
        {
            line curr = {smaller, bigger};
            lines[line_len++] = curr;
        }
    }
    
    return line_len;
}