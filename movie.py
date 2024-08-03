class Movie:
    def __init__(self, id: int, movie_code: str, movie_title: str, release_date: str, 
                 movie_url: str, image_url: str, thumbnail_url: str, actor_name: str, is_downloaded: bool):
        self.id = id
        self.movie_code = movie_code
        self.movie_title = movie_title
        self.release_date = release_date
        self.movie_url = movie_url
        self.image_url = image_url
        self.thumbnail_url = thumbnail_url
        self.actor_name = actor_name
        self.is_downloaded = is_downloaded

    def __str__(self):
        return f"Movie(movie_code='{self.movie_code}', movie_title='{self.movie_title}', \
                release_date='{self.release_date}', movie_url='{self.movie_url}', \
                image_url='{self.image_url}', thumb_nail_url='{self.thumbnail_url}', \
                actor_name='{self.actor_name}', is_downloaded={int(self.is_downloaded)})"
