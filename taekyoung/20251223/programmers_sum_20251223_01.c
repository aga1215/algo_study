#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

int *make_sums(int *numbers, int numbers_len, int *result_len);
int quicksort(int *arr, int arr_length);
int quicksort_recursive(int *arr, int left, int right);
int change_pivot(int *arr, int left, int right);

// numbers_len은 배열 numbers의 길이입니다.
int* solution(int numbers[], size_t numbers_len) {
    // return 값은 malloc 등 동적 할당을 사용해주세요. 할당 길이는 상황에 맞게 변경해주세요.
    int len = (int)numbers_len;
    int result_len = 0;
    int* answer = make_sums(numbers, len, &result_len);

    quicksort(answer, result_len);

    return answer;
}

int *make_sums(int *numbers, int numbers_len, int *result_len)
{
    int max_length = numbers_len * (numbers_len - 1) * 0.5;
    int sums = 0;
    int *arr = (int *)calloc(max_length, sizeof(int));

    for(int i = 0; i < numbers_len - 1; i ++)
    {
        for(int j = i + 1; j < numbers_len; j ++)
        {
            int check = 0;
            int sum = numbers[i] + numbers[j];

            for(int k = 0; k < sums; k ++)
            {
                if (arr[k] == sum) check = -1;
            }

            if (check == 0)
            {
                arr[sums++] = sum;
            }
        }
    }

    *result_len = sums;

    if (sums == max_length)
    {
        return arr;
    }
    else
    {
        int *result = (int *)malloc(sums * sizeof(int));
        memcpy(result, arr, sums * sizeof(int));
        free(arr);
        return result;
    }
}

int quicksort(int *arr, int arr_length)
{
    quicksort_recursive(arr, 0, arr_length - 1);
}

int quicksort_recursive(int *arr, int left, int right)
{
    if (left < right)
    {
        int pivot = change_pivot(arr, left, right);

        quicksort_recursive(arr, left, pivot - 1);
        quicksort_recursive(arr, pivot + 1, right);
    }
}

int change_pivot(int *arr, int left, int right)
{
    int pivot, temp;
    int low, high;

    pivot = arr[left];
    low = left;
    high = right + 1;

    do
    {
        do
        {
            low++;
        }while(low <= right && arr[low] < pivot);

        do
        {
            high--;
        }while(high >= left && arr[high] > pivot);

        if (low < high)
        {
            temp = arr[low];
            arr[low] = arr[high];
            arr[high] = temp;
        }
    }while(low < high);

    temp = arr[high];
    arr[high] = arr[left];
    arr[left] = temp;

    return high;
}