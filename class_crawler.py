class Episode:
    def __init__(self):
        self.webtoon_id = webtoon_id
        self.no = no
        self.url_thumbnail = url.thumbnail
        self.title = title
        self.rating = rating
        self.created_date = created_date

    @property
    def url(self):
        pass


class Webtoon:
    def __ini__(self):
        self.webtoon_id = webtoon_id
        self.title = title
        self.author = author
        self.description = description
        self.episode_list = episode_list

    def update(self):
        pass

# 4. 에피소드를 클래스로 구현
#   class Episode
#       attrs:
#           webtoon_id:     웹툰의 고유번호
#           no:             에피소드의 고유번호
#           url_thumbnail
#           title
#           rating
#           created_date
#       property:
#           url (실제 에피소드 페이지의 URL을 리턴)
#               파이썬 내장 urllib에 탑재되어있는 함수를 사용해서 생성
#               ex) http://comic.naver.com/webtoon/detail.nhn?titleId=703845&no=18
# 4-1. 위에서 dict형태로 만들던 로직을 클래스 인스턴스 생성방식으로 변경
#  episode_list리스트는 Episode인스턴스들을 자신의 요소로 가짐
# 숙제 1. 웹툰, 에피소드 이미지 클래스 작성, 에피소드 클래스 인스턴스를 내부에 가짐
# class Webtoon
#       attrs:
#           webtoon_id
#           title
#           author
#           description
#           episode_list
#       methods:
#           update: 웹에서 가져온 데이터를 사용해 Episode인스턴스들을 생성, 자신의 episode_list에 추가
#
#
# >>> yumi = Webtoon(651673)
# >>> yumi.title
# 유미와 세포들

# >>> yumi.author
# 이동건

# >>> yumi.update() <- update() 호출 안하고 yumi.episode_list에도 접근할 수 있도록 한다면?
# >>> for episode in yumi.episode_list:
# >>>    print(episode.title)
# 306화 ...
# 305화 ...

# 숙제 1. extra1) 에피소드 이미지 클래스 추가
# class EpisodeImage (각 에피소드가 가진 이미지들 중 하나를 나타냄)
#       attrs:
#           episode
#           url
#
# Episode클래스에 image_list 속성 추가
#  상세페이지 크롤링 시 image_list를 EpisodeImage의 인스턴스로 채움