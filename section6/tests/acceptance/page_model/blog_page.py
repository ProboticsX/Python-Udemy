from tests.acceptance.locators.blog_page import BlogPageLocators
from tests.acceptance.page_model.base_page import BasePage


class BlogPage(BasePage):
    def url(self):
        return super(BlogPage, self).url()+"/blog"

    def posts_section(self):
        return self.driver.find_element(*BlogPageLocators.POSTS_SECTION)

    def posts(self):
        return self.driver.find_elements(*BlogPageLocators.POST)

    def add_post_link(self):
        return self.driver.find_element(*BlogPageLocators.ADD_POST_LINK)