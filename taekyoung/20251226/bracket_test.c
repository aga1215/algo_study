#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

// 파라미터로 주어지는 문자열은 const로 주어집니다. 변경하려면 문자열을 복사해서 사용하세요.
bool solution(const char* s) {
    int cor = 0;
    char *temp = s;
    
    for (; *temp; temp++)
    {
        *temp & 1 ? cor-- : cor++;
        if (cor < 0) break;
    }
    
    return cor == 0;
}