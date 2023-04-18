from unittest import TestCase
from section3.blog.post import Post
class PostTest(TestCase):
    def test_create_post(self):
        p = Post('Title','Content')
        self.assertEqual('Title',p.title)
    def test_json(self):
        p = Post('Title', 'Content')
        expected = {'title':'Title', 'content':'Content'}
        self.assertDictEqual(p.json(), expected)