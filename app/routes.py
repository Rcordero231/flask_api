from app import app
from fake_data.posts import post_data

@app.route('/')
def index():
    first = 'Ricardo'
    last = 'Cordero'
    age = '24'
    return f'Hello World -{first} {last} {age}'

# POST ENDPOINTS

# Get all posts
@app.route('/posts')
def get_posts():
    posts = post_data
    return posts

# get single post by id
@app.route('/posts/<int:post_id>')
def get_post_id(post_id):
    # print(f'The post ID is {post_id} and the type is {type(post_id)}')
    # return str(post_id)
    posts = post_data
    #for each dictionary in the list of post dictionaries
    for post in posts:
        # If the key of 'id' on the post dictionary matches the post_id from URL
        if post['id'] == post_id:
            #return the post of the matching 'id'
            return post
    return {'ERROR': f'Post with an ID of {post_id} does NOT exist'}
        
