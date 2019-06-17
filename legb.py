# 1. local
# 2. Enclosing Function (내포한 함수)
# 3. Global
# 4. Built-in

# LEG 임
b = 300 # Global
def f():
    b = 200 # local도 아니고 global도 아닌 애매한 애랑 enclosing
    def g():
        b = 100  # Local
        print(b)
        print(__name__) # 이게 Built-in main에서 실행하니깐 main이 나옴
    g()

if __name__ == '__main__': # 만일 이 파일이 인터프리터에 의해서 실행되는 경우 라면
    f()
