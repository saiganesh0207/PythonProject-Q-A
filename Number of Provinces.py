# Get the input from the user
isConnected = eval(input("Enter matrix: "))

n = len(isConnected)
visited = [False] * n
count = 0

def dfs(city):
    for i in range(n):
        if isConnected[city][i] == 1 and not visited[i]:
            visited[i] = True
            dfs(i)

for i in range(n):
    if not visited[i]:
        visited[i] = True
        dfs(i)
        count += 1

print("Number of provinces:", count)
