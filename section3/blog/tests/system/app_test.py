from unittest import TestCase
from unittest.mock import patch
from section3.blog import app
from section3.blog.blog import Blog
from section3.blog.post import Post
class AppTest(TestCase):
    def setUp(self):
        b = Blog('Test Blog Title', 'Test Blog Author')
        app.blogs = {b.title: b}
    def test_menu_calls_ask_create_blog(self):
        with patch('builtins.input') as mocked_input:
            mocked_input.side_effect = ('c', 'Test Blog Title', 'Test Blog Author', 'q')
            with patch('section3.blog.app.ask_create_blog') as mocked_ask_create_blog:
                app.menu()
                mocked_ask_create_blog.assert_called()

    def test_menu_prints_prompt(self):
        with patch('builtins.input', return_value = 'q') as mocked_input:
            app.menu()
            mocked_input.assert_called_with(app.MENU_PROMPT)
    def test_menu_calls_print_blogs(self):
        with patch('section3.blog.app.print_blogs') as mocked_print_blogs:
            with patch('builtins.input', return_value = 'q'): #to have a fake/mock input
                app.menu()
                mocked_print_blogs.assert_called()
    def test_print_blogs(self):
        with patch('builtins.print') as mocked_print:
            app.print_blogs()
            mocked_print.assert_called_with('- Test Blog Title by Test Blog Author (0 post)')

    def test_ask_create_blog(self):
        with patch('builtins.input') as mocked_input:
            mocked_input.side_effect = ('Test', 'Test Author')
            app.ask_create_blog()
            self.assertIsNotNone(app.blogs.get('Test'))

    def test_ask_read_blog(self):
        with patch('builtins.input', return_value='Test Blog Title') as mocked_input:
            with patch('section3.blog.app.print_posts') as mocked_print:
                app.ask_read_blog()
                mocked_print.assert_called_with(app.blogs['Test Blog Title'])

    def test_print_posts(self):
        app.blogs['Test Blog Title'].create_post('Test Post Title', 'Test Post Content')
        with patch('section3.blog.app.print_post') as mocked_print:
            app.print_posts(app.blogs['Test Blog Title'])
            mocked_print.assert_called_with(app.blogs['Test Blog Title'].posts[0])

    def test_print_post(self):
        p = Post('Test Post Title', 'Test Post Content')
        expected = """
--- Test Post Title ---
Test Post Content
"""
        with patch('builtins.print') as mocked_print:
            app.print_post(p)
            mocked_print.assert_called_with(expected)

    def test_ask_create_post(self):
        with patch('builtins.input') as mocked_input:
            mocked_input.side_effect = ('Test Blog Title', 'Test Post Title', 'Test Post Content')
            app.ask_create_post()
            self.assertEqual(app.blogs['Test Blog Title'].posts[0].title, 'Test Post Title')
            self.assertEqual(app.blogs['Test Blog Title'].posts[0].content, 'Test Post Content')