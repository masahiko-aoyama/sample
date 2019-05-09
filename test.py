# サンプルコード
from test1 import Test1
from test2 import Test2
from test3 import Test3

y = 0
while y < 10:
    # yに1を加算
    y += 1
    # yを表示
    print(y)

# 外部に引数を飛ばして加算表示
Test1.a(y)

# 外部に引数を飛ばして表示（initのサンプル）
t1 = Test2("てすと", 1)
t1.aaa()
t1.bbb()

Test3.kuku()

