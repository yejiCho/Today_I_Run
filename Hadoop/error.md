# error

- 문제점
1. Exhausted available authentication methods


## 1. Exhausted available authentication methods 인증하지 못했습니다.

```
클러스터를 설치하는 중에 Exhausted available authentication methods 에러 발생

```

### try1. sshd_config 내용 변경

```
sshd_config 파일에서 PermitRootLogin을 yes로 설정

$sudo vi /etc/ssh/sshd_config

#아래와 같이 수정
PermitRootLogin yes


$ sudo service ssh restart

$ systemctl restart sshd.service #Centos7인 경우
```

## 2. No route to host

- curl http://localhost:7180/
- curl: (7) Failed connect to localhost:7180; No route to host

```
iptables -F
iptables -L
```