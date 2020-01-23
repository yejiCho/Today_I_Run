# SELECT

# [프로그래머스-모든 레코드 조회하기](https://programmers.co.kr/learn/courses/30/lessons/59034?language=oracle)


```sql

# ANIMAL_INS 테이블의 모든 레코드 조회
# ANIMAL_ID 오름차순

SELECT      * 
FROM        ANIMAL_INS
ORDER BY    ANIMAL_ID
;


```

# [프로그래머스-역순 정렬하기](https://programmers.co.kr/learn/courses/30/lessons/59035?language=oracle)


```sql

# ANIMAL_INS 테이블에서 NAME, DATETIME 조회
# ANIMAL_ID를 역순 정렬

SELECT      NAME , DATETIME
FROM        ANIMAL_INS
ORDER BY    ANIMAL_ID   DESC
;


```

# [프로그래머스-아픈 동물 찾기](https://programmers.co.kr/learn/courses/30/lessons/59036?language=oracle)

```sql

# 아픈동물의 animal_id와 name 검색
# animal_id 오름차순 정렬

select      animal_id, name
from        animal_ins
where       intake_condition = 'Sick'
order by    animal_id
;

```

# [프로그래머스 - 어린 동물 찾기](https://programmers.co.kr/learn/courses/30/lessons/59037?language=oracle)

```sql

# INTAKE_CONDITION 이 AGED가 아닌 ANIMAL_ID 와 NAME 조회
# ANIMAL_ID 오름차순 정렬

SELECT      ANIMAL_ID   , NAME
FROM        ANIMAL_INS
WHERE       INTAKE_CONDITION != 'Aged'
ORDER BY    ANIMAL_ID

```

# [프로그래머스 - 동물의 아이디와 이름](https://programmers.co.kr/learn/courses/30/lessons/59403?language=oracle)

```sql

SELECT  ANIMAL_ID , NAME
FROM    ANIMAL_INS
ORDER BY ANIMAL_ID
;

```

# [프로그래머스 - 여러 기준으로 정렬하기](https://programmers.co.kr/learn/courses/30/lessons/59404?language=oracle)

```sql

SELECT      ANIMAL_ID, NAME, DATETIME
FROM        ANIMAL_INS

ORDER BY    NAME ASC, DATETIME DESC

;


```


# [프로그래머스 - 상위 n개 레코드](https://programmers.co.kr/learn/courses/30/lessons/59405)

```sql

# DATETIME 정렬해서 열번호가 1인 것 만 추출

SELECT  NAME
FROM    (SELECT NAME
        FROM    ANIMAL_INS
        order by DATETIME
        )
WHERE ROWNUM = 1
;

```

# SUM, MAX, MIN

# [프로그래머스 - 최댓값 구하기](https://programmers.co.kr/learn/courses/30/lessons/59415)

```sql

SELECT  MAX(DATETIME)
FROM    ANIMAL_INS
;

```

# [프로그래머스 - 최솟값 구하기](https://programmers.co.kr/learn/courses/30/lessons/59038)

```sql

SELECT  MIN(DATETIME)
FROM    ANIMAL_INS
;

```

# [프로그래머스 - 동물 수 구하기](https://programmers.co.kr/learn/courses/30/lessons/59406)

```sql

SELECT  COUNT(*)
FROM    ANIMAL_INS

```


# [프로그래머스 - 중복 제거하기](https://programmers.co.kr/learn/courses/30/lessons/59408?language=oracle)

```sql

SELECT  COUNT(DISTINCT  NAME)
FROM    ANIMAL_INS
WHERE   NAME IS NOT NULL
;

```

# GROUP BY

# [프로그래머스 - 고양이와 개는 몇 마리 있을까](https://programmers.co.kr/learn/courses/30/lessons/59040?language=oracle)

```sql

SELECT  ANIMAL_TYPE, COUNT(ANIMAL_TYPE)  count
FROM    ANIMAL_INS
GROUP   BY  ANIMAL_TYPE
ORDER   BY  ANiMAL_TYPE

```

# [프로그래머스 - 동명 동물 수 찾기](https://programmers.co.kr/learn/courses/30/lessons/59041?language=oracle)

```sql

SELECT      NAME, COUNT( NAME)
FROM        ANIMAL_INS
WHERE       NAME IS NOT NULL
GROUP BY    NAME
HAVING      COUNT(NAME) >= 2
ORDER BY    NAME
;

```

# IS NULL

# [프로그래머스 - 이름이 없는 동물의 아이디](https://programmers.co.kr/learn/courses/30/lessons/59039?language=oracle)

```sql

SELECT  ANIMAL_ID
FROM    ANIMAL_INS
WHERE   NAME IS NULL
ORDER BY    ANIMAL_ID

```

# [프로그래머스 - 이름이 있는 동물의 아이디](https://programmers.co.kr/learn/courses/30/lessons/59407)

```sql

SELECT  ANIMAL_ID
FROM    ANIMAL_INS
WHERE   NAME IS NOT NULL
ORDER BY ANIMAL_ID

```

# [프로그래머스 - NULL 처리하기](https://programmers.co.kr/learn/courses/30/lessons/59410)

```sql

SELECT      ANIMAL_TYPE, NVL(NAME,'No name') NAME, SEX_UPON_INTAKE
FROM        ANIMAL_INS
ORDER BY    ANIMAL_ID

```

# JOIN

# [프로그래머스 - 없어진기록](https://programmers.co.kr/learn/courses/30/lessons/59042?language=oracle)

```sql

SELECT      B.ANIMAL_ID, B.NAME
FROM        ANIMAL_INS  A   
RIGHT OUTER JOIN    ANIMAL_OUTS B
ON          (A.ANIMAL_ID = B.ANIMAL_ID)
WHERE       A.ANIMAL_ID IS NULL
ORDER BY    B.ANIMAL_ID
;

```

# [프로그래머스 - 있었는데요 없었습니다.]()

```sql
-- 보호 시작일 보다 입양일이 더 빠른 동물의 아이디와 이름을 조회하는 QL문 작성
-- 결과는 보호 시작일이 빠른순
-- a쿼리와 b쿼리의 동물아이디는 같지만 a.DATETIME이 더빠른 것 추출

SELECT      a.ANIMAL_ID, a.NAME
FROM        ANIMAL_INS  a, ANIMAL_OUTS  b
WHERE       a.ANIMAL_ID = b.ANIMAL_ID
AND         a.DATETIME  > b.DATETIME
ORDER BY    a.DATETIME
;

```

# []()

```sql

-- SELECT a.name, a.datetime
-- FROM animal_ins a
-- LEFT OUTER JOIN animal_outs b on (a.animal_id = b.animal_id)
-- WHERE b.animal_id is NULL
-- AND    ROWNUM <= 3
-- ORDER BY a.datetime
-- ;

-- SELECT NAME, DATETIME 
-- FROM ANIMAL_INS A 
-- WHERE A.ANIMAL_ID NOT IN (
--                             SELECT B.ANIMAL_ID 
--                             FROM ANIMAL_OUTS B ) 
-- AND ROWNUM <= 3
-- ORDER BY A.DATETIME
-- ;



```