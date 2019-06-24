### python pickle 모듈이란 무엇이고, 어떤 경우에 사용하는가?

- `pickle 묘듈`은 파이썬 객체 구조의 직렬화와 역 직렬화를 위한 바이너리 프로토콜을 구현한다. `pickling`은 파이썬 객체 계층 구조가 바이트 스트림으로 변환되는 절차이며, `unpickling`은 반대 연산으로 바이트 스트림을 객체 계층 구조로 복원한다. 

  피클링은 "직렬화", "마샬링" 또는 "평탄화" 라고도 한다.



- 다음 형에서 가능하다.
  - None, True와 False
  - 정수, 실수, 복소수
  - 문자열, 바이트열, 바이트 배열
  - 피클 가능한 객체만 포함하는 튜플, 리스트, 집합과 딕셔너리
  - 모듈의 최상위 수준에서 정의된 함수, 내장함수, 클래스
  - 그런 클래스의 인스턴스 중에서 `__dict__` 나 `__getstate__()`를 호출한 결과가 피클 가능한 것들
  - 불가능한 객체는 `PicklingError`가 발생한다.

- 출처 <https://docs.python.org/ko/3/library/pickle.html>





Clustering

### 아래 빈칸에 들어갈 말과 군집 타당성 지표를 나타내는 3가지는?

#### 	클러스터링의 목적은?

#### 	(1) 군집 간 분산(inter-cluster variance)  ( _ _ _ )

#### 	(2) 군집 내 분산(inner-cluster variance) ( _ _ _ )



- 빈칸 : 최대화, 최소화

https://ratsgo.github.io/machine%20learning/2017/04/16/clustering/

- 군집 타당성 지표 3가지
  - 군집 간 거리
  - 군집의 지름
  - 군집의 분산



- 추가 

  - 군집 타당성 평가란 클러스터링 과업은 정답이 없기 때문에 단순정확도 등 지표로 평가할 수 없다. 하지만 군집을 만든 결과가 얼마나 유용한지 따지는 군집 타당성 지표가 있다. 군집 타당성 지표는 위의 세가지가 있으며 군집의 분산 등을 고려한다. 다시말해 군집 간 분산과 군집 내 분산을 따진다는 것이다.
  - Dunn Index는 군집간 거리의 최소값을 분자, 군집 내 요소 간 거리의 초대값을 분모로 하는 지표이다. 

  ![1561097551071](C:\Users\multicampus\AppData\Roaming\Typora\typora-user-images\1561097551071.png)

  - ![1561097562425](C:\Users\multicampus\AppData\Roaming\Typora\typora-user-images\1561097562425.png)

  - 군집 간 거리는 멀수록, 군집 내 분산은 작을 수록 좋은 군집화 결과라 말 할 수 있다. 이 경우에는 Dunn Index는 커지게 된다.