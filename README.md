# Project

## 설정

### 일본어 번역

```shell
shop 앱

상품보러가기 -> アイテム詳細を見る
상품상세 -> 商品詳細 / 후기 *개 -> レビュー*件 / *점 -> *点 / *원 -> *円  / 장바구니 -> 買い物かご
구매후기 -> 購入レビュー / 후기를 남겨주세요. -> レビューを残してください。/ 평점 -> 評価
상품문의 -> 商品お問い合わせ / 문의를 남겨주세요. -> お問い合わせください/ 미답변 상태입니다. -> 未回答の状態です。
 
faq 앱
자주 묻는 질문/문의 よくあるご質問・お問い合わせ一覧
https://www.rakuten.co.jp/sitemap/inquiry.html 참조
https://eimyistoire.com/shop/pages/pc_static_faq.aspx 참조

account 앱
https://grp03.id.rakuten.co.jp/rms/nid/registfwdi 참조


about 페이지

환영합니다! -> ウエルカム! 
쇼핑몰에 오신 것을 환영합니다. ショッピングモールへようこそ。
영업시간-> 営業時間, 주소-> 住所, 전화번호 -> 電話番号 이메일 -> メール


```

### 패키지 설치

```shell
pip install django
pip install pillow
pip install django-crispy-forms
```

### 실행

```shell
python manage.py makemigrations account
python manage.py makemigrations faq
python manage.py makemigrations shop
python manage.py makemigrations single_pages
python manage.py migrate
python manage.py createsuperuser 
```

## 아래 git 사용법 꼭 참조해주세요!
* [git 사용법 정 교수님 노션 링크](https://sung2ne.notion.site/git-290980c8f16244e8ae435da55d942da2)
* [참고할 만한 도서 : Visual studio 사용자를 위한 git](https://wikidocs.net/book/7060)

    * [Git for Windows 다운로드](https://github.com/git-for-windows/git/releases/download/v2.39.0.windows.1/Git-2.39.0-64-bit.exe)
    * [Tortoise 다운로드](https://tortoisegit.org/download/)
    * 로컬 저장소 내 원하는 위치에 새 폴더 생성 후 현 repository 다운로드 해주세요! 
        * git clone https://git.4this.kr/Japan/Project.git

    * git config user.name **작성자 이름** : 작성자 이름 설정
    * git config user.email **이메일** : 작성자 이메일 설정
    * git config --list : repository 설정 전체 출력
    * git help **커맨드 이름** : 도움말

    ![git 동작 개념](https://wikidocs.net/images/page/149672/01.02.04.jpg)

    * git add **파일명** : working directory 파일을 staging area에 올림
    * git add . : working directory 내 변경 된 모든 파일들을 staging area에 올림
    * git reset **파일명** : staging area에 올렸던 파일 내림
    * git commit -m "**메시지**" : 간단한 메시지를 넣어 staging area 파일을 repository에 올림(commit)
    * git commit -a : add와 commit을 동시 진행
    * git status : 상태 정보 출력

    * 이력 관리와 관련 없는 파일이나 경로들은 .gitignore 파일에 기록!
