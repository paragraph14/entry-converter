import datetime

def make_blog_post(text):
    text = str(text)
    title = text[0:text.find('\n')]
    body = text[text.find('\n'):]
    matter = str(front_matter(title))
    post = matter + body
    return post

class front_matter:
    def set_title(self, post_title):
        self.title = self.title + post_title

    def set_date(self):
        time = datetime.datetime.today()
        nowtime = time.isoformat() + ' +0900'
        self.date = self.date + nowtime

    def make_matter(self):
        self.matter = self.line + '\n' + self.title + '\n' + self.pub + '\n' + self.date + '\n' + self.line + '\n'

    def __init__(self, post_title):
        self.title = 'title: '
        self.line = '---'
        self.pub = 'published: true'
        self.date = 'date: '

        self.set_title(post_title)
        self.set_date()
        self.make_matter()

    def __str__(self):
        return self.matter