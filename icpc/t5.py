n, m = map(int, input().split())

mn_team_num = n // m
left_team_m = n % m

mn = (left_team_m * mn_team_num * (mn_team_num + 1) + (m - left_team_m) * mn_team_num * (mn_team_num - 1)) // 2

mx_team_num = n - m + 1
mx = (mx_team_num * (mx_team_num - 1)) // 2

print(mn, mx)
