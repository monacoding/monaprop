#substance.py

#1. 유체 정보를 저장하는 클래스 정의

class Substance : 
    """
    열역학 물질 클래스 : 물질의 기본 물성 정보를 저장하고, 
    상태(온도,압력,증기분율) 중 2개로 상태를 정의 할 수 있도록 한다. 
    """
    def __init__ (self, name, Tc, Pc, omega,M=None): #이 물질의 고유 특성 정의를 위한 함수 
        """_summary_
        Args:
            name (_type_): 유체 이름 예) methane 
            Tc (_type_): 입계온도(K) 예) 190.6
            Pc (_type_): 임계압력(Pa) 예) 4599000
            omega (_type_): 압축인자 예) 0.011
            M (float, optional) 분자량 [g/mol] 예) 16.04
        """
        self.name = name
        self.Tc = Tc
        self.Pc = Pc
        self.omega = omega
        self.M = M
        
        #상태 변수 초기화 
        self.state = {}

    def set_state(self, T=None, P=None, x=None): #이 물질이 어떤 상태에 있는가?
        """_summary_

        Args:
            T (_type_, optional): _온도_. 상태의 기준이 되는 온도
            P (_type_, optional): _압력_. 상태의 기준이 되는 압력 
            x (_type_, optional): _증기 분율_. 상태의 기준이 되는 증기 분율
            상기 3개 중 2개를 입력해야 함 
        """
        provided = [v is not None for v in [T,P,x]]
        if sum (provided) !=2 :
            raise ValueError("T,P,vapor fraction 중 2개를 입력하세요")
           
        self.state={"T":T,"P":P,"x":x}
        
    def __str__(self):
        return f"{self.name} : Tc={self.Tc}K, Pc= {self.Pc}Pa,"

