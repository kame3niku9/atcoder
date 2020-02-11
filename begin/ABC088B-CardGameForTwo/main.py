def resolve():
    N = int(input())
    a_list = map(int, input().split())
    a_sorted = sorted(a_list, reverse=True)
    # print(a_sorted)
    alice_hands = a_sorted[::2]
    bob_hands = a_sorted[1::2]
    # print("alice", alice_hands)
    # print("bob", bob_hands)
    diff = sum(alice_hands) - sum(bob_hands)
    print(diff)

if __name__ == "__main__":
    resolve()

