from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
#creating a fastapi app 
app = FastAPI()

posts =[
    {
            "id":1,
            "title": "Getting Started with Python",
            "content": "Python is a versatile language that is easy to learn. Here's how you can get started...",
            "published": True
    },
    {
            "id":2,
            "title": "Exploring the Galaxy: Space Facts",
            "content": "The universe is vast and filled with mysteries. In this post, we uncover some amazing space facts...",
            "published": False
        },
    {
        "id":3,
        "title": "Healthy Eating Tips",
        "content": "Maintaining a balanced diet is crucial for a healthy lifestyle. Here are 10 tips to get you started...",
        "published": True
        }
        
]

class Post(BaseModel):
    id : int
    title: str
    content: str
    published : bool

@app.get('/posts')
async def get_all():
    return posts

@app.get('/posts/{post_id}')
async def get_post(post_id: int):
    for post in posts:
        if post["id"] == post_id:
            return post
    raise HTTPException(status_code=404, detail="Post not found")
    
@app.post('/posts/add')
async def add_post(post:Post):
    new_post = post.model_dump()
    new_post["id"] = len(posts) + 1
    posts.append(new_post)
    return new_post

@app.put('/posts/update/{post_id}')
async def update_post(post : Post, post_id : int):
    update_post = post.model_dump()
    for post in posts:
        if post["id"] == post_id:
            post.update(update_post)
            return {"post": post}
        
@app.patch('/posts/update-partial/{post_id}')
async def update_post(post : Post, post_id : int):
    update_post = post.model_dump(exclude_unset=True)
    for post in posts:
        if post["id"] == post_id:
            post.update(update_post)
            return {"post": post}
        
@app.delete('/posts/delete/{post_id}')
async def delete_post(post_id: int):
    for post in posts:
        if post["id"] == post_id:
            posts.remove(post)
            
        
        