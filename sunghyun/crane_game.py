def solution(board, moves):
    """
    프로그래머스: 크레인 인형뽑기 게임
    https://school.programmers.co.kr/learn/courses/30/lessons/64061

    문제 설명:
    게임 화면의 격자의 상태가 담긴 2차원 배열 board와
    인형을 집기 위해 크레인을 작동시킨 위치가 담긴 배열 moves가 매개변수로 주어질 때,
    크레인을 모두 작동시킨 후 터트려져 사라진 인형의 개수를 return 하도록 solution 함수를 완성해주세요.

    제한사항:
    - board 배열은 2차원 배열로 크기는 "5 x 5" 이상 "30 x 30" 이하입니다.
    - board의 각 칸에는 0 이상 100 이하인 정수가 담겨있습니다.
    - 0은 빈 칸을 나타냅니다.
    - 1 ~ 100의 각 숫자는 각기 다른 인형의 모양을 의미하며 같은 숫자는 같은 모양의 인형을 나타냅니다.
    - moves 배열의 크기는 1 이상 1,000 이하입니다.
    - moves 배열 각 원소들의 값은 1 이상이며 board 배열의 가로 크기 이하인 자연수입니다.

    입출력 예:
    board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
    moves = [1,5,3,5,1,2,1,4]
    result = 4
    """
    bucket = []
    answer = 0

    for move in moves:
        index = move - 1
        for row in range(len(board)):
                if board[row][index] != 0:
                    picked = board[row][index]
                    board[row][index] = 0

                    if len(bucket) > 0 and bucket[-1] == picked:
                        bucket.pop()
                        answer += 2
                    else:
                        bucket.append(picked)
                    
                    break

    return answer