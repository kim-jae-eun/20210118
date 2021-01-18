try:
    f = open("sample.txt", "rt", encoding="UTF-8")
    g = open("sample_2021_01_18.txt", "at", encoding="UTF-8")
    for line in f:
        g.write(line)
    f.close()
    g.close()
    print('저장이 완료되었습니다.')
except FileNotFoundError as e:
    print(e)