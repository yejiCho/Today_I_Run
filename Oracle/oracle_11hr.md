# [oracle 11g hr](https://kwanhwi0123.tistory.com/1)

```
--REGIONS			:	region_id, region_name
--LOCATIONS		    :	location_id, street_address, postal_code, city, state_province, country_id
--DEPARTMENTS	    :	department_id, department_name, manager_id, location_id
--JOBS				:	job_id, job_title, min_salary, max_salary
--EMPLOYEES		    :   employee_id, First_name, Last_name, Phone_number, Hire_date, Job_id, Salary, Commission_pct,  Manager_id, Department_id
--JOB_HISTORY	    :   employee_id, start_Date, End_date, Job_id, Department_id
--COUNTRIES		    :	Country_id, country_name, region_id
```

```sql

1.  직책(job title)이 Sales Manager인 사원들의 입사년도와 입사년도(hire_date)별 평균급여를 출력하시오. 출력시 년도를 기준으로 오름차순 정렬

SELECT  TO_CHAR(HIRE_DATE 'YYYY') , AVG(SALARY)
FROM    EMPLOYEES   A, JOBS B
WHERE   A.JOB_ID = B.JOB_ID
AND     B.JOB_TITLE = 'Sales Manager'
GROUP BY    HIRE_DATE
ORDER BY    HIRE_DATE

SELECT  TO_CAHR(E.HIRE_DATE, 'YYYY'), AVG(E.SALARY)
FROM    EMPLOYEES   E, JOBS J
WHERE   E.JOB_ID = J.JOB_ID
AND     J.JOB_TITLE = 'Sales Manager'
GROUP BY    TO_CHAR(E.HIRE_DATE, 'YYYY')
ORDER BY    TO_CHAR(E.HIRE_DATE, 'YYYY')

```

```sql

2. 각 도시(CITY)에 있는 모든 부서 직원들의 평균급여를 조회하고자 한다. 평균급여가 가장 낮은 도시부터 도시명(CITY)과 평균연봉, 해당 도시의 직원수 출력
단, 도시에 근무하는 직원이 10명 이상인 곳인 제외하고 조회


SELECT  TABLE_NAME  FROM    TABS;

SELECT  COUNT(A.EMPLOYEE_ID)    AS  COUNT_EMPLOYEE, AVG(A.SALARY)
FROM    EMPLOYEES   A, DEPARTMENT   B
WHERE   A.DEPARTMENT_ID = B.DEPARTMENT_ID
GROUP BY A.DEPARTMENT_ID
HAVING   COUNT(A.EMPLOYEE_ID) <= 10
ORDER BY AVG(A.SALARY)

SELECT  L.CITY, AVG(E.SALART), COUNT(*)
FROM    EMPLOYEES E , LOCATIONS L, DEPARTMENTS D
WHERE   E.DEPARTMENT_ID = D.DEPARTMENT_ID 
AND     D.LOCATION_ID   =   L.LOCATION_ID
GROUP BY    L.CITY
HAVING  COUNT(*)    < 10
ORDER BY    AVG(E.SALARY) ASC


```