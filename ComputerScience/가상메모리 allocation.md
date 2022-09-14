# Allocation

각 프로세스에 얼만큼의 페이지 프레임을 할당할 것인가

### Allocation의 필요성

1. 메모리 참조 명령어 수행시 명령어, 데이터 등 여러 페이지 동시참조
   - 명령어 수행을 위해 최소한 할당되어야 하는 프레임의 수가 있음

2. Loop를 구성하는 page들은 한꺼번에 allocate 되는 것이 유리함
   - 최소한의 allocation이 없으면 매 loop 마다 page fault

### Allocation Scheme

1. Equal allocation : 모든 프로세스에 똑같은 갯수 할당
2. Propertional allocation : 프로세스 크기에 비례하여 할당
3. Priority allocation : 프로세스의 priority에 따라 다르게 할당

### Global replacement(프로세스 간 경쟁)

1. Replace 시 다른 process에 할당된 frame을 빼앗아 올 수 있다
2. Process별 할당량을 조절하는 또 다른 방법이다
3. FIFO , LRU, LFU 등의 알고리즘을 global replacement로 사용시에 해당
4. Working set, PFF 알고리즘 사용

![](C:\Users\a0511\Desktop\71147778-흰색-배경-벡터-일러스트-레이-션에-아기-돼지-삼형제.jpg)

### Local replacement(프로세스 내부에서 대체)

1. 자신에게 할당된 frame 내에서만 replacement
2. FIFO, LRU, LFU 등의 알고리즘을 process 별로 운영시

![](C:\Users\a0511\Desktop\120151222_02_01.jpg)

### Thrashing

1. 프로세스의 원활한 수행에 필요한 최소한의 page frame 수를 할당 받지 못한 경우 발생
2. page fault rate이 매우 높아짐
3. CPU utilization이 낮아짐
4. OS MPD(Multiprogramming degree)를 높여야 한다고 판단
5. 또 다른 프로세스가 시스템에 추가됨(higher MPD)
6. 프로세스 당 할당된 frame의 수가 더욱 감소
7. 프로세스는 page의 swap in / swap out으로 매우 바쁨
8. 대부분의 시간에 CPU는 한가함
9. 낮은 처리량

![](C:\Users\a0511\Desktop\42.jpg)

![](C:\Users\a0511\Desktop\70577700-19128800-1bef-11ea-8322-0f6e67d6334d.png)

### Working-set Model

1. Locality of reference
   - 프로세스는 특정 시간동안 일정 장소만을 집중적으로 참조한다
   - 집중적으로 참조되는 해당 page들의 집합을 locality set이라 함

2. Working-set Model
   - Locality에 기반하여 프로세스가 일정 시간 동안 원활하게 수행되기 위해 한꺼번에 메모리에 올라와 있어야 하는 page들의 집합을 Working set이라 정의함
   - Working set 모델에서는 process의 working set 전체가 메모리에 올라와 있어야 수행되고 그렇지 않을 경우 모든 frame을 반납한 후 swap out(suspend)
   - Thrashing을 방지함
   - Multiprogramming degree를 결정함

### Working-Set Algorithm

1. Working set의 결정

   - Woriking set window를 통해 알아냄

   - Window size 가  Δ인 경우

     시각 ti에서의 working set WS(ti)

     ​	Time interval[ti- Δ,ti] 사이에 참조된 서로 다른 페이지들의 집합

   - Working set에 속한 page는 메모리에 유지, 속하지 않은 것은 버림

     (즉, 참조된 후 Δ 시간 동안 해당 page를 메모리에 유지한 후 버림 )

![](C:\Users\a0511\Desktop\캡처2.JPG)

### PPF(Page-Fault Frequency) Scheme

1. page-fault rate의 상한값과 하한값을 둔다
   - Page fault rate이 상한값을 넘으면 frame을 더 할당한다
   - Page fault rate이 하한값 이하이면 할당 frame 수를 줄인다

2. 빈 frame이 없으면 일부 프로세스를 swap out

![](C:\Users\a0511\Desktop\캡처.JPG)