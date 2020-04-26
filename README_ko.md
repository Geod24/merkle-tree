# 머클 트리 구조

파이썬을 이용한 머클 트리 구현.  
C++ / D 로 구현 예정.  
업데이트 2020-04-25.  
*영어 버전: [English](README.md)*

## 목록
  - [설치](#설치)
    - [리눅스](#리눅스)
    - [macOS](#macos)
  - [사용법](#사용법)
    - [생성 모드](#생성-모드)
    - [확인 모드](#확인-모드)
  - [요구사항](#요구사항)
  - [개선해야할 사항](#개선해야할-사항)
  - [배운 개념](#배운-개념)
  - [배워야 할 개념](#배워야-할-개념)

## 설치

리포지토리 클론 또는 다운로드.

```
$ git clone https://github.com/kchulj/merkle-tree.git
```

### 리눅스

파이썬 설치 확인.
```bash
$ python --version
```

설치되어 있지 않은 경우, 파이썬 설치.
```bash
$ sudo apt-get install python3
```

### macOS

파이썬 설치 확인.
```bash
$ python 
```

설치되어 있지 않은 경우, Homebrew 이용해서 파이썬 설치.
```bash
$ brew install python3
```

## 사용법

### 생성 모드

생성 `produce` 모드는 입력된 문자열에 SHA256 알고리즘을 2번 적용함으로써 해시를 생성합니다.  

```
$ python merkle.py produce "The quick brown fox" "jump over" "the" "lazy dog"
```

해시값으로 구성된 머클 트리를 생성하고 출력합니다.  
레벨 0 해시는 머클 루트입니다.

```
Level 0:
018FB04252A594A8049CBFE9E34848249040E1FA7E170501E17ADC06393D4DC3
Level 1:
836C2FE675884DB41C49215F8A91E6560B1EA752F683DB793E9B86180CA235F8
49B9A6B1346DC768898A16C2DAD9D554349C9150F8B2809AC7D48B305C4D3650
Level 2:
7743034D22491720B723B68AFD046BE66969409254DC79A153E290C81A8F238A
F51DF418D9D7BAFDCFDC4320409E08E39858D0D686FEE959EA545E6D7C214F71
1E7C521A055F0F08CEA3FADED5923CCA2D8F4366A62AAA8A8B843A842AA656B8
144BEE93D8F6350C6E38C96EEB11DE2CD249A7BD5D23FF4C91EB46573B5AF3BA
```

인수 입력이 없거나 오류가 있을 경우, 프로그램은 종료하고 `EXIT_FAILURE` 메세지를 출력합니다.

이 테스트는 균형 이진 트리의 경우입니다. 균형 이진 트리에서의 인수의 갯수는 2의 지수입니다. 불균형 트리일 경우, 마지막 값이 반복됨으로써 균형 트리가 생성됩니다.

아래의 알고리즘은 불균형 머클 트리의 레벨을 정하는 알고리즘 입니다.  

입력 갯수 | (반복된 갯수) 마지막 레벨 노드 갯수 | 총 노드 수 | 레벨
------- | ------- | ------- | ------- 
1 | (+0) 1 | 1 | 0 
2 | (+0) 2 | 3 | 1 
3 | (+1) 4 | 7 | 2 
4 | (+0) 4 | 7 | 2 
5 | (+3) 8 | 15 | 3 
6 | (+2) 8 | 15 | 3 
7 | (+1) 8 | 15 | 3 
8 | (+0) 8 | 15 | 3 
9 | (+7) 16 | 31 | 4 
10 | (+6) 16 | 31 | 4 
...  | ... | ... | ... 

```python
lvl = 0 # 시작 레벨
while arrlen > 2**lvl: # 배열 길이를 순차적으로 2의 지수와 비교
    lvl += 1
    if arrlen <= 2**lvl: # 배열 길이가 다음 2의 지수보다 작거나 같을 경우, 루프는 break하고 레벨 결정
        break
```

5개의 문자열을 입력하면,

```
$ python merkle.py produce "The quick brown fox" "jump over" "the" "lazy" "dog"
```

마지막 해쉬를 3번 반복하고, 마지막 레벨에 8개의 노드와 레벨 3 트리를 생성합니다.

```
Level 0:
9AF409C11D320898DA335F82FAC8918014A6589E55F2C98F2B3C468ED83F6ACE
Level 1:
6E76CEB1CBD48BE752949D832B4AB2848E7B9DF6A4286A524C7B134A4A9DF458
156B626C730889C1CD1A1F05D55EC3C16AF6DC5BD6977E0BE2A1935C86A74CCF
Level 2:
836C2FE675884DB41C49215F8A91E6560B1EA752F683DB793E9B86180CA235F8
31A1892ED0C9857597D9D8902E1A05D5A3A99DEAD7FADB9E69BF319FC22C1AE6
CBBC43D5431E285C2770E9F9084663CB6CCF4B23228DD8E90A30B361A80CC57D
CBBC43D5431E285C2770E9F9084663CB6CCF4B23228DD8E90A30B361A80CC57D
Level 3:
7743034D22491720B723B68AFD046BE66969409254DC79A153E290C81A8F238A
F51DF418D9D7BAFDCFDC4320409E08E39858D0D686FEE959EA545E6D7C214F71
1E7C521A055F0F08CEA3FADED5923CCA2D8F4366A62AAA8A8B843A842AA656B8
6CFAC15CDF8A0065DCF55ADC0F9CE57847747EA94D63A276CACCEC6F64A8819D
9DA6BDB1E8A041F1795966F87619385B713E4BEFE723130ED2748939EF791579
9DA6BDB1E8A041F1795966F87619385B713E4BEFE723130ED2748939EF791579
9DA6BDB1E8A041F1795966F87619385B713E4BEFE723130ED2748939EF791579
9DA6BDB1E8A041F1795966F87619385B713E4BEFE723130ED2748939EF791579
```

### 확인 모드

**미완성**

확인 ```verify``` 모드는 해쉬가 머클 트리의 일부인지 확인합니다.
이 모드는 최소 6개의 인수를 아래와 같이 받아야 합니다:
- [1] verify *(모드)*
- [2] 머클 루트 : *str -> hash*
- [3] 값의 갯수 : *int*
- [4] 해쉬 인덱스  : *int*
- [5] 해쉬값 : *str -> hash*
- [6][...][6 + 레벨 - 1] 머클 경로 : *str -> hash*

> [0] 는 기본값 ```python``` 입니다.

예시:
```
$ python merkle.py verify 018FB04252A594A8049CBFE9E34848249040E1FA7E170501E17ADC06393D4DC3 4 1 F51DF418D9D7BAFDCFDC4320409E08E39858D0D686FEE959EA545E6D7C214F71 7743034D22491720B723B68AFD046BE66969409254DC79A153E290C81A8F238A 49B9A6B1346DC768898A16C2DAD9D554349C9150F8B2809AC7D48B305C4D3650
```
```
Valid Merkle path
```

확인이 실패할 경우 프로그램은 ```Invalid Merkle path``` 메시지를 출력하고 ```EXIT_FAILURE```를 리턴합니다. 확인이 성공하면 ```Valid Merkle path``` 메시지를 출력하고 ```EXIT_SUCCESS```를 리턴합니다.

## 요구사항
- [ ] 최신 Linux / Mac OS X 운영체제에서 실행
> Verify 모드 미완성
- [x] 다음 언어 중 한가지 사용: D, C++, C, Go, Rust, Python
- [x] 코드 빌딩 설명 제공
- [x] 해슁과 콘솔 쓰기를 제외한 라이브러리 함수 사용금지
- [x] 오류 처리 (e.g. 하드 크래시 없어야 함)
- [ ] 예시와 같은 서식으로 출력
> 해쉬 함수가 예시와 다른 값을 출력함. 외부 라이브러리로 테스트 예정.
- [ ] 설명서와 추가적 테스트 추가 가능

## 개선해야할 사항
- [ ] Verify 모드 미완성
  - [x] Verify 개념 이해
  - [ ] 문자열 입력을 해쉬 객체로 변환하는 방법
- [ ] OpenSSL, libsodium, Crypto++ 등 dependencies 사용

## 배운 개념
- [x] SHA-2 / SHA-256 알고리즘
- [x] 머클-담가드 구조 / 해쉬 함수
- [x] 해쉬 길이 확장공격
- [x] 정적 vs. 동적 링킹

## 배워야 할 개념
- [ ] 디펜던시 사용, IDE, compiler와 링킹
- [ ] 빌딩 도구: Makefile, CMake
- [ ] 컴파일러를 CLI에서 실행
- [ ] 유닉스 환경 개발 연습