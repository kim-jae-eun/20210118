import os
while True:
    if os.path.exists('c:\\iotest'):
        f = open("c:\\iotest\\today.txt", "wt", encoding="UTF-8")
        f.write("""오늘은 2021년 01월 18일입니다.
오늘은 월요일입니다.
나는 화요일에 태어났습니다.""")
        f.close()
        break
    else:
        os.mkdir('c:\\iotest')
print('저장이 완료되었습니다.')