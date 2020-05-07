t = int(input())

for tc in range(1, t+1):
    n, m = map(int, input().split())
    cargos = list(map(int, input().split()))
    trucks = list(map(int, input().split()))
    cnt = 0
    ans = 0
    cargo_idx = 0
    cargos.sort(reverse=True)
    trucks.sort(reverse=True)

    
    for truck in trucks:
        while cargos[cargo_idx] > truck:
            cargo_idx += 1
            if cargo_idx == n:
                break
        if cargo_idx < n and cargos[cargo_idx] <= truck:
            cnt += 1
            ans += cargos[cargo_idx]
            cargo_idx += 1
        if cnt == m or cargo_idx == n:
            break
    print("#%d"%tc, ans)