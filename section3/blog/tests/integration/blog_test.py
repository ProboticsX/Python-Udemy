from unittest import TestCase
from section3.blog.blog import Blog

class BlogTest(TestCase):
    def test_create_post_in_blog(self):
        b = Blog('Title', 'Author')
        b.create_post('Post Title', 'Post Content')
        self.assertEqual(len(b.posts), 1)
        self.assertEqual(b.posts[0].title, 'Post Title')

    def test_json(self):
        b = Blog('Title', 'Author')
        b.create_post('Post Title', 'Post Content')
        expected = {
            'title':'Title',
            'author':'Author',
            'posts':[
                {
                'title':'Post Title',
                'content': 'Post Content'
                }
            ]
        }
        self.assertDictEqual(b.json(), expected)