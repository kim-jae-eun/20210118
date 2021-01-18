# 첫 번째 방법
try:
    f = open("yesterday.txt", "rt", encoding="UTF-8")
    count_yesterday = 0
    for a in f:
        b = a.lower().count('yesterday')
        count_yesterday += b
    f.close()
except FileNotFoundError:
    print('파일을 읽을 수 없어요.')
else:
    print("Number of a Word 'Yesterday'", count_yesterday)
finally:
    print('수행완료!!')

# 두 번째 방법
try:
    f = open("yesterday.txt", "rt", encoding="UTF-8")
    count_yesterday = 0
    for a in f:
        b = a.replace('\n',' ').replace('.','').replace(',','').split(' ')
        count_yesterday+=b.count('yesterday')+b.count('Yesterday')
    f.close()
except FileNotFoundError:
    print('파일을 읽을 수 없어요.')
else:
    print("Number of a Word 'Yesterday'", count_yesterday)
finally:
    print('수행완료!!')