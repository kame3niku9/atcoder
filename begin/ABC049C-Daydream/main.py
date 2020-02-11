import sys
sys.setrecursionlimit(100000)

def resolve():
    S = input()
    judge = dfs3(S)
    if judge:
        print("YES")
    else:
        print("NO")

def dfs(string):
    if len(string) == 0:
        return True
    if string[:5] == "dream":
        if dfs(string[5:]):
            return True
    if string[:7] == "dreamer":
        if dfs(string[7:]):
            return True
    if string[:5] == "erase":
        if dfs(string[5:]):
            return True
    if string[:6] == "eraser":
        if dfs(string[6:]):
            return True
    return False
    
def dfs2(string):
    # print(string)
    strings = [string]
    # print(strings)
    while True:
        candidate_num = len(strings)
        # print(candidate_num)
        if candidate_num == 0:
            return False
        string = strings.pop()
        if len(string) == 0:
            return True
        if string[:5] == "dream":
            strings.append(string[5:])
        if string[:7] == "dreamer":
            strings.append(string[7:])
        if string[:5] == "erase":
            strings.append(string[5:])
        if string[:6] == "eraser":
            strings.append(string[6:])
        # print(strings)
        # if candidate_num == len(strings):
        #    print("hoge")

def dfs3(ori_string):
    # print(string)
    starts = [0]
    # print(strings)
    while True:
        candidate_num = len(starts)
        # print(candidate_num)
        if candidate_num == 0:
            return False
        start = starts.pop()
        string = ori_string[start:]
        if len(string) == 0:
            return True
        if string[:5] == "dream":
            starts.append(start + 5)
        if string[:7] == "dreamer":
            starts.append(start + 7)
        if string[:5] == "erase":
            starts.append(start + 5)
        if string[:6] == "eraser":
            starts.append(start + 6)
        # print(strings)
        # if candidate_num == len(strings):
        #    print("hoge")

if __name__ == "__main__":
    resolve()