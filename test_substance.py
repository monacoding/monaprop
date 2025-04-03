from substances.substance import Substance  #substances 라는 폴더의 substance.py 파일의 Substance 클래스 갖고 온다 
from substances.registry import substance_registry
#1. 물질 선택

print("사용가능한 물질",",".join(substance_registry.keys()))

name = input("사용할 물질의 이름을 입력하세요").lower()

if name not in substance_registry:
    print(f"'{name}'는 등록된 물질이 아닙니다.")
    exit()

sub = substance_registry[name]


#2. 상태 입력 
print("온도, 압력, 증기분율 중 2개를 입력하세요 (T,P,x)")

selected = input("입력할 항목을 쉼표로 구분해서 입력 하세요, (예 : T,x) ").replace("","").upper().split(',')

if len(selected) != 2 or not all(s in ['T','P','X'] for s in selected):
    print("입력 오류 : T,P,x 중 2개를 정확히 입력 하세요")
    exit()

T = P = x = None

if 'T' in selected:
    T = float(input("온도 T (K): "))

if 'P' in selected:
    P = float(input("압력 P (Pa): "))

if 'X' in selected:
    x_input = input("증기분율 x (0~1): ")
    x = float(x_input) if x_input.strip() != '' else None

# 조건에 맞게 상태 설정
try :
    #빈 값은 None 으로 처리 
    sub.set_state(
        T=T if T is not None and T > 0 else None,
        P=P if P is not None and P > 0 else None,
        x=x
    )

except ValueError as e:
    print("상태 설정 오류 :",e)
    exit()

# 3. 물질 정보 출력
print("\n[물질 정보]")
print(sub)

print("\n[상태 정보]")
for k, v in sub.state.items():
    if v is not None:
        print(f"{k} = {v}")
        
