from unittest import TestCase
from unittest.mock import patch
import app
from section3.blog.blog import Blog

class AppTest(TestCase):
    def test_print_blogs(self):
        b = Blog('Title', 'Author')
        app.blogs = {b.title:b}
        with patch('builtins.print') as mocked_print:
            app.print_blogs()
            mocked_print.assert_called_with('- Title by Author (0 post)')