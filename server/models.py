from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
db = SQLAlchemy()

class Author(db.Model):
    __tablename__ = 'authors'
    # Add validations and constraints 

    id = db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String, unique=True, nullable=False)
    phone_number = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    def __repr__(self):
        return f'Author(id={self.id}, name={self.name})'

    @validates('name')
    def validate_name(self, key, input_name):
        if input_name == '': 
            raise ValueError ('Failed')
        
        return input_name

    @validates('phone_number')
    def validate_number(self, key, p_num):
        if not 10 == len(p_num): 
            raise ValueError ('Failed')
        
        return p_num


class Post(db.Model):
    __tablename__ = 'posts'
    # Add validations and constraints 

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    content = db.Column(db.String)
    category = db.Column(db.String)
    summary = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    @validates('title')
    def validate_title(self, key, input_title):
        if not 1 <= len(input_title) or not isinstance(input_title, str): 
            raise ValueError ('title Failed')

        return input_title
    
    @validates('summary', 'content')
    def validate_length(self,key,input):
        if key == 'summary':
            if len(input) >= 250:
                raise ValueError ('summary Failed')
        elif key == 'content':
            if len(input) < 250:
                raise ValueError ('content Failed')
        
        return input
    
    @validates('category')
    def validate_category(self, key, input):
        if not (input == 'Ficton' or input == 'Non-Fiction'):
            raise ValueError ('category Failed')

        return input

    def __repr__(self):
        return f'Post(id={self.id}, title={self.title} content={self.content}, summary={self.summary})'
