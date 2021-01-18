import calendar
while True:
    try:
        year=int(input('연도를 입력하십시오.(숫자 4자리) : '))
        month=int(input('월을 입력하십시오.(1~12 중 하나) : '))
        break
    except ValueError:
        print('숫자 형식이 잘못되었습니다. 다시 입력해주세요.')
print(calendar.month(year,month))