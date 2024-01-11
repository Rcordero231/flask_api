from flask import request
from app import app, db
from fake_data.posts import post_data
from app.models import User, Post
from app.auth import basic_auth, token_auth


@app.route('/')
def index():
    first_name = 'Ricardo'
    last_name = 'Cordero'
    return f'Hello World!! - From {first_name} {last_name}'

# USER ENDPOINTS
@app.route("/token")
@basic_auth.login_required
def get_token():
    user = basic_auth.current_user()
    token = user.get_token()
    return {"token":token,
            "tokenExpiration":user.token_expiration}


# Creat new user
@app.route('/users', methods=['POST'])
def create_user():
    # Check to see if the request body is JSON
    if not request.is_json:
        return {'Error': 'Yout content-type must be application/json'}, 400
    
    # Get the data from the request body
    data= request.json
    
    # Validate that the data has all of the required fields
    required_fields = ['firstName', 'lastName', 'username', 'email', 'password']
    missing_fields = []
    for field in required_fields:
        if field not in data:
            missing_fields.append(field)
        if missing_fields:
            return {'error': f"{', '.join(missing_fields)} must be in the body"}, 400
        

    first_name = data.get('firstName')
    last_name = data.get('lastName')
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    # Check to see if user is already in database (will be different when we use db)
    #  ---------------------------NOT USED ANYMORE---------------------------------
    # for user in users:
    #     if user['username'] == username or user['email'] == email:
    #         return {'error': 'A user with that username and/or email already exists'}, 400
    ##  ---------------------------NOT USED ANYMORE---------------------------------

    # New User with the db
    check_users = db.session.execute(db.select(User).where((User.username==username), (User.email==email))).scalars().all()
    if check_users:
        return {'Error': 'A user with that username or email already exists'}, 400
    

    # ------------NOT USED ANYMORE---------------
    # Create new user dict and append to users list
    # new_user = {
    #     "id": len(users)+1,
    #     "firstName": first_name,
    #     "lastName": last_name,
    #     "username": username,
    #     "email": email,
    #     "password": password
    # }
    # users.append(new_user)
    # ------------NOT USED ANYMORE---------------

    new_user = User(first_name=first_name, last_name=last_name, username=username, email=email, password=password)
    return new_user, 201

# POST ENDPOINTS

# Get all posts
@app.route('/posts')
def get_posts():
    # Get the posts from storage (fake data, will setup db tomorrow)
    posts = db.session.execute(db.select(Post)).scalars().all()
    return [p.to_dict() for p in posts]

# Get single post by ID
@app.route('/posts/<int:post_id>')
def get_post(post_id):
    # Get the posts from storage
    post = db.session.get(Post, post_id)
    # For each dictionary in the list of post dictionaries
    if post:
        return post.to_dict()
    else:
        return {'error': f'Post with an ID of {post_id} does not exist'}, 404

# Create new Post route
@app.route('/posts', methods=['POST'])
def create_post():
    # Check to see that the request body is JSON
    if not request.is_json:
        return {'error': 'You content-type must be application/json'}, 400
    # Get the data from the request body
    data = request.json
    # Validate the incoming data
    required_fields = ['title', 'body']
    missing_fields = []
    for field in required_fields:
        if field not in data:
            missing_fields.append(field)
    if missing_fields:
        return {'error': f"{', '.join(missing_fields)} must be in the request body"}, 400
    
    # Get data from the body
    title = data.get('title')
    body = data.get('body')

    # Create a new post with data
    new_post = {
        "id": len(post_data) + 1,
        "title": title,
        "body": body,
        "userId": 1,
        "dateCreated": "2024-01-09T11:25:45",
        "likes": 0
    }
    # Add the new post to the list of posts
    post_data.append(new_post)
    return new_post, 201
