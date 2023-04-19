MENU_PROMPT = 'Enter "c" to create a blog, "l" to list them, "r" to read one, "p" to write a post, or "q" to quit:'
blogs = dict() #blog name : blog Object
def menu():
    print_blogs()
    selection = input(MENU_PROMPT)

def print_blogs():
    for key, blog in blogs.items():
        print('- {}'.format(blog))