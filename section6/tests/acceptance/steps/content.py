from tests.acceptance.page_model.base_page import BasePage
from behave import *

from tests.acceptance.page_model.blog_page import BlogPage

use_step_matcher('re')

@then('There is a title shown on the page')
def step_impl(context):
    page = BasePage(context.browser)
    assert page.title().is_displayed()

@step('The title tag has content "(.*)"')
def step_impl(context, content):
    page = BasePage(context.browser)
    assert page.title().text == content

@then('I can see there is a posts section on the page')
def step_impl(context):
    page = BlogPage(context.browser)
    assert page.posts_section().is_displayed()

@then('I can see there is a post with title "(.*)" in the posts section')
def step_impl(context, title):
    page = BlogPage(context.browser)
    posts = page.posts()
    post = [p for p in posts if p.text==title]
    assert len(post)>0
