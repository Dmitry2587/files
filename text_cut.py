title = '2020 год почти окончен, но не стоит расстраиваться, всё ещё впереди!'

n = 40
txt = title[:n]
c = txt.rfind(' ', 0, 10000000000)
alt_txt = title[:c] + '...'


if len(title) <= n:
    print(title)
else:
    print(alt_txt)
