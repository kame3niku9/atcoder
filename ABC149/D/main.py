store_score = {}
win_hands = {"s": "r", "r": "p", "p": "s"}
scores = {}

def resolve():
    # k飛ばしで文字列を抽出し、それらの文字列ごとに最適なpathを考える
    N, K = map(int, input().split())
    R, S, P = map(int, input().split())
    T = input()

    global scores
    scores = {"s": S, "r": R, "p": P}

    total_score = 0
    for i in range(K):
        # print(T[i::K])
        target_text = T[i::K]
        # print(target_text)
        target_text += "o"

        previous_select = "o"
        local_score = 0
        for j in range(len(target_text) - 1):
            previous_select, score = judge(previous_select, target_text[j], target_text[j+1])
            local_score += score    

        total_score += local_score

    print(total_score)
                        

def judge(previous_select, current_machine, next_machine):
    # print(previous_select, current_machine, next_machine)
    ideal_hand = win_hands[current_machine]
    if previous_select == ideal_hand:
        # もし前回と同じハンドが理想ハンドならば、次回のハンドに邪魔しない手を選ぶ
        select = next_machine
        score = 0
    else:
        select = ideal_hand
        score = scores[select]
    # print(select, score)
    return select, score


if __name__ == "__main__":
    resolve()