from unittest import TestCase
from unittest.mock import patch
from section3.blog import app
from section3.blog.blog import Blog

class AppTest(TestCase):
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
        b = Blog('Title', 'Author')
        app.blogs = {b.title:b}
        with patch('builtins.print') as mocked_print:
            app.print_blogs()
            mocked_print.assert_called_with('- Title by Author (0 post)')