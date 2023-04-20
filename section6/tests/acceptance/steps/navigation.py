from behave import *
from selenium import webdriver

from tests.acceptance.page_model.blog_page import BlogPage
from tests.acceptance.page_model.home_page import HomePage

use_step_matcher('re')

@given('I am on the homepage')
def step_impl(context):
    context.browser = webdriver.Chrome()
    page = HomePage(context.browser)
    context.browser.get(page.url())

@given('I am on the blog page')
def step_impl(context):
    context.browser = webdriver.Chrome()
    page = BlogPage(context.browser)
    context.browser.get(page.url())

@then('I am on the blog page')
def step_impl(context):
    page = BlogPage(context.browser)
    expected_url = page.url()
    assert context.browser.current_url == expected_url

@then('I am on the homepage')
def step_impl(context):
    page = HomePage(context.browser)
    expected_url = page.url()
    assert context.browser.current_url == expected_url