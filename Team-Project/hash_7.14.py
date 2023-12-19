M = 11  # 해시 테이블의 크기
table = [None] * M  # 해시 테이블. 모든 항목은 None으로 초기화

def hashFn(key):
    return key % M

# 코드 7.12: 선형조사법의 삽입 연산
def linear_probe_insert(key, probing_function):
    i = hashFn(key)
    count = M
    while count > 0:
        if table[i] is None or table[i] == -1:
            break  # 삽입 위치 발견
        i = probing_function(i)  # 다음 위치 조사
        count -= 1

    if count > 0:  # 삽입할 곳이 있으면 삽입
        table[i] = key

# 코드 7.13: 선형조사법의 탐색 연산
def linear_probe_search(key, probing_function):
    i = hashFn(key)
    count = M
    while count > 0:
        if table[i] is None:  # 탐색 실패
            return None
        if table[i] == key:  # 탐색 성공
            return table[i]
        i = probing_function(i)
        count -= 1

    return None  # 탐색 실패

# 코드 7.14: 선형조사법의 삭제 연산
def linear_probe_delete(key, probing_function):
    i = hashFn(key)
    count = M
    while count > 0:
        if table[i] == key:  # 삭제할 레코드 발견
            table[i] = -1
            return
        if table[i] is None:  # 삭제할 레코드 없음
            return
        i = probing_function(i)
        count -= 1

# 코드 7.15: 이차조사법의 해시 함수 수정 및 연산 추가
def quadratic_probe_insert(key):
    def quadratic_probe(i):
        return (i + 1) % M
    linear_probe_insert(key, quadratic_probe)

def quadratic_probe_search(key):
    def quadratic_probe(i):
        return (i + 1) % M
    return linear_probe_search(key, quadratic_probe)

def quadratic_probe_delete(key):
    def quadratic_probe(i):
        return (i + 1) % M
    linear_probe_delete(key, quadratic_probe)

# 코드 7.17: 이중해싱법의 연산 추가
def double_hashing_probe_insert(key):
    def double_hashing_probe(i):
        return (hashFn2(key, i)) % M
    linear_probe_insert(key, double_hashing_probe)

def double_hashing_probe_search(key):
    def double_hashing_probe(i):
        return (hashFn2(key, i)) % M
    return linear_probe_search(key, double_hashing_probe)

def double_hashing_probe_delete(key):
    def double_hashing_probe(i):
        return (hashFn2(key, i)) % M
    linear_probe_delete(key, double_hashing_probe)

# 코드 7.16: 체이닝을 이용한 오버플로 처리
class Node:
    def __init__(self, data, link=None):
        self.data = data
        self.link = link

def chaining_insert(key):
    k = hashFn(key)  # 해시 주소 계산
    n = Node(key)  # 새로운 노드 생성
    n.link = table[k]  # 노드의 다음 노드로 시작 노드 연결
    table[k] = n  # 새로운 노드가 시작 노드가 됨

def chaining_search(key):
    k = hashFn(key)
    n = table[k]  # 시작 노드
    while n is not None:  # 연결된 모든 노드를 탐색
        if n.data == key:  # 탐색 성공. 노드의 데이터(레코드) 반환
            return n.data
        n = n.link  # 링크를 따라 다음 노드로 진행
    return None  # 탐색 실패. None 반환

def chaining_delete(key):
    k = hashFn(key)
    n = table[k]  # 시작 노드
    before = None  # 이전 노드
    while n is not None:  # n이 None이 아닐때 까지
        if n.data == key:  # 삭제할 레코드 찾음
            if before is None:  # 삭제할 항목이 시작 노드이면, 다음 노드가 시작노드
                table[k] = n.link
            else:  # 두 번째 이후 항목 삭제인 경우
                before.link = n.link
            return
        before = n
        n = n.link