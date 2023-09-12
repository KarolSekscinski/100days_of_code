import requests

blog_url = "https://api.npoint.io/c790b4d5cab58020d391"


class Post:
    def __init__(self):
        self.posts = self.get_posts()

    def get_posts(self):
        response = requests.get(url=blog_url)
        posts = response.json()
        return posts

    def get_single_post(self, post_id):
        for post in self.posts:
            if post_id == str(post['id']):
                return post
        return None
