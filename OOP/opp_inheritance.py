"""
<상속이란>
상속은 상위 클래스가 하위 클래스에게 속성을 물려주는 행위를 말한다.
예를들어 교육기관이라는 큰 범주안에 중학교 고등학교 대학교가 있고
다시 그 범주안에 학생, 교수, 교직원이 있다
중학교 교등학교 대학교는 교육기관을 상속받고
학생 교수 교직원은 중, 고, 대학교를 상속받는다
"""

class Education() :
    def __init__(self, locate) :
        self.locate = locate # 교육청의 소재지

    def get_locate(self) :
        return self.locate
        


class School(Education) :
    def __init__(self, locate, school_name):
        super().__init__(locate)
        self.school_name = school_name

    def get_school_name(self) :
        return self.school_name

class employee(School) :
    def __init__(self, locate, school_name, name, job):
        super().__init__(locate, school_name)

        self.name = name
        self.job = job

    def __str__(self) :
        return "저는 소재지 {} 인 {} 에서 {} 을 하고있는 {} 입니다".format(super().get_locate(), super().get_school_name(), self.job, self.name)


minsu = employee("경기도", "네이버고등학교", "민수", "행정업무")

print(minsu)