# django 연습 프로젝트

이 프로젝트는 django 연습용 프로젝트입니다.

Author: nab5m <br/>

## 환경 (Environments)
<b>OS:</b> Windows 10 <br/>
DB: PostgreSql 12 <br/>
IDE: Pycharm 2019.2.x <br/>
Python: 3.8.0 <br/>
pip: 20.0.2 <br/>

psycopg2-binary가 설치 안될 경우 pip를 최신 버전으로 업그레이드 했는지 확인해주세요. 리눅스의 경우
psycopg2로 대체할 수도 있습니다.

## 프로젝트 fork or clone
```shell script
0. fork and clone this project
1. make your virtualenv directory
2. create file 'config/secret_settings.py'
<config/secret_settings.py>
  SECRET_KEY = 'make your django secret key'

  DB_NAME = 'your database name'
  DB_USERNAME = 'your database user name'
  DB_PASSWORD = 'your database user passwrd'
  DB_HOST = 'localhost'
  DB_PORT = '5432'

3. pip install -r requirements.windows.txt
4. python manage.py migrate
5. python manage.py runserver
6. set your oauth key
7. Open your brower and check if it's operating (http://127.0.0.1:8000)

8. happy coding :)
9. make pull requests for me
```

## OAuth 설정하기
구글에서 Django allauth / Django 소셜로그인 검색해서 자세히 보기
- kakao: Rest api key를 client id로 저장
- naver: 네이버 개발자 센터에서 어플리케이션 생성

admin에서 소셜 어플리케이션 레코드 추가
- provider, client id, secret_key, sites 설정
