count_objects, count_varin_callers = map(int, input().split())
if count_varin_callers <= 2:
    ans = 2 + count_objects + count_objects * count_varin_callers
else:
    ans = 2 + count_objects + count_objects * count_varin_callers + count_objects * count_varin_callers * (count_varin_callers-1) // 2
print(ans)