# GCP에 cloudera-manager setting

## 1.GCP project 만들기
## 2.GCE(google compute engine)설정
## 3.cloudera manager 설치

- GCE (환경설정)

```
OS : centos 7
region : asia-northeast3-a
machine : n1-highmem-16
엑세스 범위 : 모든 Cloud API에 대한 전체 엑세스 허용
방화벽 : HTTP 트래픽 허용, HTTPS 트래픽 허용
```

- cloudera manager 설치전 수행

```
sudo yum update && sudo yum install wget

sudo yum groupinstall "Development Tools"

To disable selinux,
 simply do a sudo vi /etc/sysconfig/selinux and set selinux=disabled 
 and reboot the machine.

sudo vim /etc/sysconfig/selinux

selinux=disabled

reboot


```


- cloudera manager 설치

```
관리자 모드에서 수행
sudo su root -

sudo wget http://archive.cloudera.com/cm5/installer/5.9.0/cloudera-manager-installer.bin

권한 설정(755): 소유자는 모든 것(쓰기,읽기,실행)이 가능하다.
chmod 755 cloudera-manager-installer.bin
chmod u+x cloudera-manager-installer.bin

sudo ./cloudera-manager-installer.bin

```

- Firewall rules

```
GCP : VPC network -> Firewall rules

ip : 0.0.0.0/0
tcp: 7180

http://<your public ip>:7180

```

### cloudera manager 설치완료!