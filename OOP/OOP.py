class SoccerPlayer() : # SoccerPlayer라는 Class 생성
    def __init__(self, name, possition, back_number):
        self.name = name                # 파라미터로 넘어온 name이라는 변수를 self.name에 저장
        self.position = possition       # 파라미터로 넘어온 possition이라는 변수를 self.possition에 저장
        self.back_number = back_number  # 파라미터로 넘어온 back_number이라는 변수를 self.back_number에 저장

    def change_back_number(self,new_number) :
        print("선수의 등번호를 변경합니다 : From {} to {}".format(self.back_number, new_number))
        self.back_number = new_number


    def now_back_number(self) :
        print("{} 선수의 현재 등번호는 {}입니다".format(self.name, self.back_number))

    def get_position(self) :
        print("{} 선수의 포지션은 {}입니다".format(self.name, self.position))

    def __str__(self) :
        return ("{} 선수의 정보\n".format(self.name)+"포지션 : {}\n등번호 : {}".format(self.position, self.back_number))

# self는 java의 this와 같은 기능을 함
# Class는 객체를 만드는 틀이고 instance는 실제 객체를 의미함
# 축구선수 민수와 정수는 같은 축구선수지만 서로 다른 "속성 즉 변수"를 가지고 있으며
# 서로 다른 사람이므로 서로 다른 "행동 즉 함수"를 가지고 있음
# 예를들어 민수와 정수 모두 "back_number"를 가지고 있지만 서로의 "back_number"는 다름
# 여기서 self는 민수와 정수 각각 다른 "변수와 함수"를 사용하기 위한 자기 자신의 주소를 가르키는 함수로 이해하면 편함



minsu = SoccerPlayer("minsu","attacker","10")       # minsu의 이름을 가진 attacker 등번호는 10인 객체 생성
jungsu = SoccerPlayer("junsu","midfileder","15")    # jungsu의 이름을 가진 midfileder 등번호는 15인 객체 생성

minsu.now_back_number()         # 민수의 등번호 출력
minsu.change_back_number(5)     # 민수의 등번호 변경
minsu.now_back_number()         # 민수의 등번호 출력
minsu.get_position()            # 민수의 포지션 출력
print(minsu)                    # 예약어를 활용한 minsu 출력
print("##########################")
jungsu.now_back_number()        # 정수의 등번호 출력
jungsu.get_position()           # 정수의 포지션 출력
print(jungsu)                   # 예약어를 활용한 jungsu 출력


# minsu의 now_back_number method를 call 하게 되면 minsu = SoccerPlayer("minsu","attacker","10") 에서와 같이 민수의 등번호를 10으로 초기화 하여 10이 출력됨
# jungsu의 now_back_number method를 call 하게 되면 jungsu = SoccerPlayer("junsu","midfileder","15") 에서와 같이 정수의 등번호를 15로 초기화 하여 15가 출력됨
# 즉 minsu의 self.back_number와 jungsu의 self.back_number가 서로 다르다는것을 알 수 있음