# w: 'dkhc' 일 때
# 답: hcdk.
# k > h > d > c

# d가 첫글자일 때 내림차순으로 되어있어서 그 다음 글자는 h일 때이다.
# h와 d를 바꾼 후
# 다 내림차순으로 되어있어서 오름차순으로 바꾸기

def biggerIsGreater(w):
    w = list(w) # w: [dkhc]

    # Find non-increasing suffix: 뒷자리부터 시작해서 내림차순으로 되어있지 않은 부분 찾기
    i = len(w) - 1 # i=3
    while i > 0 and w[i - 1] >= w[i]: #(k > h > d > c) i가 1일 때 걸린다.
        i -= 1

    if i <= 0: # 입력된 w가 다 내림차순으로 되어있을 때
        return 'no answer'

    # Find the rightmost successor to pivot in the suffix
    j = len(w) - 1 # j=3
    while w[j] <= w[i - 1]: # 걸린 d보다 큰 글자 찾기. (h > d에서 걸린다)
        j -= 1

    # Swap the pivot with the rightmost character
    # w: dkhc
    w[i - 1], w[j] = w[j], w[i - 1] #i=1, j=2
    # w: hkdc

    # Reverse the sufix
    w[i:] = w[len(w) - 1:i - 1:-1] # w[1:] = w[4-1:1-1:-1](w[3:1:-1] -> 맨마지막 글자부터 i번째까지 역순을 넣기 (cdk)
    # w: hcdk
    return ''.join(w)

# 처음에는 조합을 통해 경우의 수를 구하고 가장 작은 값을 찾는 문제로 접근했다.
# 하지만 permutation 라이브러리 쓰든 조건부를 넣어서 직접 구현을 하든 테스트 케이스에서 걸리더라. (시간 초과로 예상된다)
# 이를 통해 조합은 접근하면 안된다는걸 깨달아야 했다. (하지만 난 이 방법 밖에 몰랐지.)
