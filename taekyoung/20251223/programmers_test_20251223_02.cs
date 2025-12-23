using System;
using System.Collections;
using System.Collections.Generic;

public class Solution {
    public int[] solution(int[] answers) {

        int first = Examine(answers, First(answers.Length));
        int second = Examine(answers, Second(answers.Length));
        int third = Examine(answers, Third(answers.Length));
        
        int[] answer = new int[] {first, second, third}; 
        
        return GetMax(answer);
    }
    
    public int[] GetMax(int[] arr)
    {
        int best = Int32.MinValue;
        List<int> maxs = new List<int>();
            
        for(int i = 0; i < arr.Length; i ++)
        {
            if (arr[i] > best)
            {
                best = arr[i];
                maxs.Clear();
                maxs.Add(i + 1);
            }
            else if (arr[i] == best)
            {
                maxs.Add(i + 1);
            }
        }
        
        return maxs.ToArray();
    }
    
    public int Examine(int[] answers, IEnumerator<int> person)
    {
        int examine = 0;
        person.MoveNext();
        for (int i = 0; i < answers.Length; i ++)
        {         
            if (answers[i] == person.Current)
            {
                examine++;
            }
            person.MoveNext();
        }
        
        return examine;
    }
    
    public IEnumerator<int> First(int length)
    {
        int answer = 0;
        for(int i = 0; i < length; i ++)
        {
            if (answer == 5) answer = 0;
            yield return ++answer;
        }
    }
    
    public IEnumerator<int> Second(int length)
    {
        int answer = 0;
        for(int i = 0; i < length; i ++)
        {
            if (answer == 5) answer = 0;
            
            if (i % 2 == 0) yield return 2;
            else yield return (++answer == 2) ? ++answer : answer;
        }
    }
    
    public IEnumerator<int> Third(int length)
    {
        int[] answers = new int[]{3, 1, 2, 4, 5};
        int index = 0;
        for(int i = 0; i < length; i ++)
        {
            if (index == 5) index = 0;
            yield return answers[index];
            yield return answers[index++];
        }
    }
}