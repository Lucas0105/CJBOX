# 영화 추천 알고리즘 기반 커뮤니티 서비스
- [팀원](#팀원)
- [업무분담](#업무분담)
- [목표](#목표)
- [아키텍처](#아키텍처)
- [영화 추천 알고리즘](#영화-추천-알고리즘)
- [서비스의 대표 기능](#서비스의-대표-기능)
- [기타](#기타)


# 팀원
- 정원재
- 최유경


# 전체 일정
<div align="center">

|역할|업무|마감일|진행도|
|:---:|:---:|:---:|:---:|
|| 화면 설계 및 ERD 모델링|2022-11-16|100%|
|프론트 앤드| 메인 페이지 구현 |2022-11-17|100%|
|백앤드| API 구현 |2022-11-18|100%|
|프론트 앤드| 장르페이지 구현 |2022-11-18|100%|
|백앤드| 추천 알고리즘 구현 |2022-11-20|100%|
|프론트 앤드| 로그인, 회원가입, 프로필 구현, 검색 구현 |2022-11-20|100%|
|백앤드| 추가 기능 구현 |2022-11-21|100%|
|프론트 앤드| 영화 상세 페이지 구현, 리뷰 및 댓글 구현 |2022-11-21|100%|
|백앤드| 테스트 |2022-11-22|100%|
|프론트 앤드| 추가 기능 구현 |2022-11-22|100%|
|프론트 앤드| 테스트 |2022-11-23|100%|
|| 통합 테스트 |2022-11-23|100%|
|| 발표 준비 |2022-11-24|100%|

</div>

# 업무분담
<div align="center">

|번호|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;업무&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|담당자|시작일|마감일|완료|
|:---:|:---:|:---:|:---:|:---:|:---:|
|1|ERD 설계|정원재, 최유경|2022-11-16|2022-11-16|O|
|2|화면 설계|정원재, 최유경|2022-11-16|2022-11-16|O|
|3|API 설계|정원재|2022-11-16|2022-11-16|O|
|4|컴포넌트 설계|최유경|2022-11-16|2022-11-16|O|
|5|모델 만들기|정원재|2022-11-16|2022-11-16|O|
|6|fixture 생성하기|정원재|2022-11-17|2022-11-17|O|
|7|로고 만들기|최유경|2022-11-16|2022-11-16|O|
|8|컴포넌트 빈 파일 구현|최유경|2022-11-16|2022-11-16|O|
|9|ROUTER 구현|최유경|2022-11-17|2022-11-17|O|
|10|컴포넌트 배치|최유경|2022-11-17|2022-11-17|O|
|11|인기영화 api|정원재|2022-11-17|2022-11-17|O|
|12|최신영화 api|정원재|2022-11-17|2022-11-17|O|
|13|네비 바|최유경|2022-11-17|2022-11-17|O|
|14|메인페이지|최유경|2022-11-17|2022-11-17|O|
|15|Swagger 적용|정원재|2022-11-17|2022-11-17|O|
|16|영화 검색 api|정원재|2022-11-17|2022-11-17|O|
|17|영화 상세페이지 api|정원재|2022-11-17|2022-11-17|O|
|18|영화 장르 페이지 api|정원재|2022-11-17|2022-11-17|O|
|19|회원가입 api|정원재|2022-11-17|2022-11-17|O|
|20|로그인 api|정원재|2022-11-17|2022-11-17|O|
|21|로그아웃 api|정원재|2022-11-17|2022-11-17|O|
|22|비밀번호 변경 api|정원재|2022-11-17|2022-11-17|O|
|23|프로필 api|정원재|2022-11-17|2022-11-17|O|
|24|팔로우, 팔로잉 api|정원재|2022-11-17|2022-11-17|O|
|25|마이리스트 추가, 제거 api|정원재|2022-11-17|2022-11-17|O|
|26|마이리스트 보여주기 api|정원재|2022-11-17|2022-11-17|O|
|27|CORS 권한 부여하기|정원재|2022-11-18|2022-11-18|O|
|28|내가 쓴 리뷰 보여주기 api|정원재|2022-11-18|2022-11-18|O|
|29|장르 페이지 구현|최유경|2022-11-18|2022-11-18|O|
|30|영화 리뷰 작성|정원재|2022-11-18|2022-11-18|O|
|31|영화 리뷰 리스트 읽기|정원재|2022-11-18|2022-11-18|O|
|32|영화 리뷰 수정|정원재|2022-11-18|2022-11-18|O|
|33|영화 리뷰 상세 페이지|정원재|2022-11-18|2022-11-18|O|
|34|영화 리뷰 삭제|정원재|2022-11-18|2022-11-18|O|
|35|영화 리뷰 댓글 작성|정원재|2022-11-18|2022-11-18|O|
|36|영화 리뷰 댓글 읽기|정원재|2022-11-18|2022-11-18|O|
|37|로그인뷰 구현|최유경|2022-11-19|2022-11-19|O|
|38|영화 장르 추천|정원재|2022-11-19|2022-11-20|O|
|39|영화 추천|정원재|2022-11-19|2022-11-20|O|
|40|사용자 정보 api|정원재|2022-11-20|2022-11-21|O|
|41|검색 기능|최유경|2022-11-21|2022-11-21|O|
|42|리뷰|최유경|2022-11-21|2022-11-21|O|
|43|댓글|최유경|2022-11-21|2022-11-22|O|
|44|마이 페이지, 마이리스트(선호영화), 팔로잉|최유경|2022-11-21|2022-11-21|O|
|45|TMDB에서 fixture 데이터로 저장|정원재|2022-11-21|2022-11-21|O|
|46|TMDB에서 acting, directing, writing 데이터 받아오는 api 설정|정원재|2022-11-21|2022-11-21|O|
|47|TMDB에서 유사한 영화 요청|정원재|2022-11-21|2022-11-21|O|
|48|user 데이터에 사용할 gif 설정|정원재|2022-11-21|2022-11-21|O|
|49|api 테스트|정원재|2022-11-21|2022-11-21|O|
|50|리뷰 페이지네이션|최유경|2022-11-22|2022-11-22|O|
|51|리뷰 최신글로 보여주기|정원재|2022-11-22|2022-11-22|O|
|52|캐스트, 감독에 대한 정보 보여주기|최유경|2022-11-22|2022-11-22|O|
|53|swiper 수정하기|정원재|2022-11-22|2022-11-22|O|
|54|배너 수정하기|정원재|2022-11-22|2022-11-22|O|
|55|카카오 social 로그인|정원재|2022-11-22|2022-11-22|O|
|56|구글 social 로그인|정원재|2022-11-23|2022-11-23|O|
|57|네이버 social 로그인|정원재|2022-11-23|2022-11-23|O|
|58|리뷰 감성분석|정원재|2022-11-23|2022-11-23|O|


</div>

# 이슈
<div align="center">

|날짜|내용|해결방법|해결여부|
|:---:|:---:|:---:|:---:|
|2022-11-18|swiper와 vue의 버전이 맞지 않는 문제|swiper-vue2 패키지를 사용하여 해결|O|
|2022-11-18|TokenAuthentication 기본 폼을 사용할 때 파일이 업로드 되지 않는 문제|CustomSerializer를 정의하여 데이터 저장|O|
|2022-11-19|다큐멘터리, tv 영화 클릭 시 404 에러 발생|데이터가 없을 때 404 오류 발생 get_list_or_404 부분을 movie.objects.all() 명령어로 변경|O|
|2022-11-20|네비바의 사용자 부분의 정보를 알 수 있는 api가 없음|userStatus api 구현|O|
|2022-11-20|사용자의 사진이 필수 요소로 적용|serializer의 required를 False로 설정|O|
|2022-11-21|[API]MovieSearch의 데이터 movie id 필요||O|
|2022-11-21|영화에 참여한 사람들 데이터 요청 |credit api 구현|O|
|2022-11-21|backdrop poster 요청|backdrop이 있는 데이터만 출력|O|
|2022-11-21|유사한 영화 요청|TMDB similar movies 구현|O|
|2022-11-21|장르 id 대신 string으로 요청||O|
|2022-11-21|장르 한페이지당 30개씩 받기||O|
|2022-11-21|페이지 보낼때 끝 번호 주기||O|
|2022-11-21|리뷰&댓글 최신순 요청||O|
|2022-11-22|리뷰&댓글 끝 페이지 요청||O|
|2022-11-22|라우터 이동시 하단이나 중간 부분으로 렌더링 되는 현상 발생|router scrollBehavior 사용|O|
|2022-11-22|라우터 이동시 하단이나 중간 부분으로 렌더링 되는 현상 발생|router scrollBehavior 사용|O|
|2022-11-23|프로필에서 마이 리뷰 페이지당 3개씩 요청|review api 수정|O|
|2022-11-23|마이리스트 전체 목록 요청(페이지카운트)||O|
|2022-11-23|마이리스트 추가 제거 하기 위해 전체 목록 요청 myList api ||O|
|2022-11-23|다른 유저의 마이페이지를 방문했을 때 사진정보, 리뷰 정보 get 불가||O|
|2022-11-23|팔로우 팔로잉 정보 토글할 수 있도록 정보 출력|my_profile할 때 follow 데이터 추가|O|
|2022-11-23|비슷한 영화 추천 오류 발생|.env 파일이 없어서 발생하는 오류|O|
|2022-11-23|리뷰 댓글 삭제|reviews/comment/delete/ api 추가|O|
|2022-11-23|리뷰 좋아요 누르기|reviews/like/ api 추가|O|
|2022-11-23|팔로잉, 팔로우 목록(팔로우, 팔로잉 유저의 이름, 사진, 자기소개 data), 1페이지당 6명|followings, followers api 추가|O|
|2022-11-23| movie detail 데이터를 불러오는 api에 자신의 리뷰를 추가해서 보내주세요 |movies/detail/<int:id>/ api 변경|O|


# 아키텍처

## ERD
<div align="center">

![ERD](./%EC%82%B0%EC%B6%9C%EB%AC%BC/ERD.PNG)

</div>

## 화면설계

- 메인페이지    
<div align="center">

![mainpage](./%EC%82%B0%EC%B6%9C%EB%AC%BC/mockup1.PNG)
     
</div>

- 영화 페이지    

<div align="center">

![movie](./%EC%82%B0%EC%B6%9C%EB%AC%BC/mockup2.PNG)   

</div>

- 로그인, 회원가입 페이지    

<div align="center">

![login](./%EC%82%B0%EC%B6%9C%EB%AC%BC/mockup3.PNG)

</div>

- 프로필    

<div align="center">

![profile](./%EC%82%B0%EC%B6%9C%EB%AC%BC/mockup4.PNG)

</div>

## API 설계

<div align="center">

|앱|설명|method|url|통신|변수|타입|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|accounts|로그인|post|accounts/login/||||
|||||request|username|String|
||||||password|String|
|accounts|사용자 정보|get|accounts/userStatus/||||
|||||response|nickName|String|
||||||my_image|Image|
|accounts|회원가입|post|accounts/signup/||||
|||||request|username|String|
||||||password1|String|
||||||password2|String|
||||||intro|String|
||||||email|String|
||||||nickName|String|
||||||my_image|Image|
|accounts|로그아웃|post|accounts/logout/||||
|accounts|비밀번호 변경|post|accounts/password/change/||||
|||||request|new_password1|String|
||||||new_password2|String|
|accounts|프로필|get|accounts/:nickName/||||
|||||response|nickName|String|
||||||intro|String|
||||||genres|Array(String)|
||||||my_image|Image|
||||||followed_cnt|int|
||||||following_cnt|int|
|accounts|팔로우, 팔로잉|post|accounts/follow/||||
|||||request|nickName|String|
|accounts|마이리스트 추가하기, 제거하기|post|accounts/myList/||||
|||||request|movie_id|int|
|accounts|마이리스트 보여하기|get|accounts/myList/:nickname/:page/||||
|||||response <br/> 15개 list|movie_id|int|
||||||poster_path|String|
||||||title|String|
||||||overview|String|
||||||vote_average|int|
|accounts|내가 쓴 리뷰 보여주기|get|accounts/reviews/:page/||||
|||||response <br/> 3개 list|review_id|String|
||||||review_id|String|
||||||poster_path|String|
||||||title|String|
||||||content|String|
|accounts|로그아웃|post|accounts/logout/||||
|movies|추천 영화|get|movies/recommend/||||
|||||response <br/> 15개 list|movie_id|int|
||||||poster_path|String|
||||||title|String|
||||||overview|String|
||||||vote_average|int|
||||||popularity|int|
|movies|인기 영화|get|movies/popular/||||
|||||response  <br/> 15개 list|movie_id|int|
||||||poster_path|String|
||||||title|String|
||||||overview|String|
||||||vote_average|int|
||||||popularity|int|
|movies|최신 영화|get|movies/newMovie/:page/||||
|||||response  <br/> 9개 list|movie_id|int|
||||||poster_path|String|
||||||title|String|
||||||overview|String|
||||||vote_average|int|
||||||release_date|String|
||||||popularity|int|
|movies|검색 아래 드롭다운|get|movies/search/:title/||||
|||||request|title|String|
|||||response  <br/> 10개 list|movie_id|int|
||||||poster_path|String|
||||||title|String|
|movies|영화 상세 페이지|get|movies/detail/:id/||||
|||||response|movie_id|String|
||||||poster_path|String|
||||||title|String|
||||||overview|String|
||||||release_date|String|
||||||vote_average|int|
||||||backdrop_path|String|
||||||popularity|int|
|movies|영화 참여한 사람들|get|movies/credit/:movie_id/||||
|||||response|id|int|
||||||known_for_department|String|
||||||name|String|
||||||original_name|String|
||||||popularity|int|
||||||profile_path|String|
||||||character|String|
|movies|영화 장르 페이지|get|movies/:genre/:page/||||
|||||response <br/> 9개 list|movie_id|int|
||||||poster_path|String|
||||||title|String|
||||||overview|String|
||||||release_date|String|
||||||vote_average|int|
||||||backdrop_path|String|
|movies|영화 장르 추천|get|movies/recommend/:genre/||||
|||||response  <br/> 15개 list|movie_id|int|
||||||poster_path|String|
||||||title|String|
||||||overview|String|
||||||vote_average|int|
|reviews|영화 리뷰 작성|post|reviews/||||
|||||request|content|String|
||||||movie_id|int|
||||||vote|int|
|reviews|영화 리뷰 수정|put|reviews/||||
|||||request|content|String|
||||||review_id|int|
||||||vote|int|
|reviews|영화 리뷰 읽기|get|reviews/:movie_id/review/:page/||||
|||||response <br/> 5개 list|nickName|String|
||||||review_id|int|
||||||vote_average|int|
||||||content|String|
||||||created_at|String|
|reviews|영화 리뷰 삭제|delete|reviews/||||
|||||request|content|String|
||||||review_id|int|
||||||vote|int|
|reviews|영화 리뷰 상세페이지|get|reviews/:review_id/||||
|||||response|nickName|String|
||||||review_id|int|
||||||vote_average|int|
||||||content|String|
||||||created_at|String|
|reviews|영화 리뷰 댓글 작성|post|reviews/comment/||||
|||||request|content|String|
||||||review_id|String|
|reviews|영화 리뷰 댓글 읽기|get|reviews/:review_id/comment/:page/||||
|||||response <br/> 5개 list|content|String|
||||||created_at|String|

</div>

## 컴포넌트 설계도
<div align="center">

![component_tree](./%EC%82%B0%EC%B6%9C%EB%AC%BC/component_tree.png)

</div>

<div align="left">

# 영화 추천 알고리즘
- 사용자가 마이리스트에 추가한 영화의 장르를 count 합니다.
- 마이리스트에 추가한 영화 장르 중 가장 많은 수의 장르를 3개 선택합니다.
- 3개의 장르 중 랜덤으로 해당하는 영화 15개를 보여줍니다.
- - 이때 랜덤의 기준이 인기도가 높은 순, 개봉일이 빠른 순, 평점이 높은 순, 무작위 랜덤이 될 수 있습니다. 

- 사용자에대한 정보가 없을 시 평점, 인기도, 개봉일 기준으로 내림차순하여 15개의 영화를 랜덤으로 추천해줍니다.

# 영화 장르 추천 알고리즘
- 해당하는 장르 중 랜덤으로 영화 15개를 보여줍니다.
- - 이때 랜덤의 기준이 인기도가 높은 순, 개봉일이 빠른 순, 평점이 높은 순이 될 수 있습니다. 

# 서비스의 대표 기능


# 기타

