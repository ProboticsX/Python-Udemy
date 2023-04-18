from unittest import TestCase
from section3.blog.blog import Blog

class BlogTest(TestCase):
    def test_create_blog(self):
        b = Blog('Title', 'Author')
        self.assertListEqual(b.posts, [])

    def test_repr(self):
        b1 = Blog('Book1', 'Shubham')
        self.assertEqual(b1.__repr__(), 'Book1 by Shubham (0 post)')
        b2 = Blog('Book2', 'Aman')
        b2.posts = ['post21', 'post22']
        self.assertEqual(b2.__repr__(), 'Book2 by Aman (2 posts)')