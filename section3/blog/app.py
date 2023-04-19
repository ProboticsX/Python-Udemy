from section3.blog.blog import Blog

MENU_PROMPT = 'Enter "c" to create a blog, "l" to list them, "r" to read one, "p" to write a post, or "q" to quit:'
blogs = dict() #blog name : blog Object
def menu():
    print_blogs()
    selection = input(MENU_PROMPT)
    while selection != 'q':
        if selection == 'c':
            ask_create_blog()
        elif selection == 'l':
            print_blogs()
        elif selection == 'r':
            ask_read_blog()
        elif selection == 'p':
            ask_create_post()
        selection = input(MENU_PROMPT)

def print_blogs():
    for key, blog in blogs.items():
        print('- {}'.format(blog))

def ask_create_blog():
    title = input('Enter Title for Blog: ')
    author = input('Enter Author for Blog: ')
    blogs[title] = Blog(title, author)

def ask_read_blog():
    pass

def ask_create_post():
    pass