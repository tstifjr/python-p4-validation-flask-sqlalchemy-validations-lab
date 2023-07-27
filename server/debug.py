#!/usr/bin/env python3

from app import app
from models import db, Author, Post



if __name__ == '__main__':
    
    with app.app_context():
        from models import db, Author, Post
        a1 = Author(name = 'ben', phone_number = '1234567890')

        import ipdb; ipdb.set_trace()
