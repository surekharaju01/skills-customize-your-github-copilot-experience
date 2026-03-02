"""
Building REST APIs with FastAPI

Description: A starter template for building a REST API using FastAPI.

Author: [Student Name]
Date: [Submission Date]
"""

from fastapi import FastAPI
from pydantic import BaseModel

# TODO: Create a Pydantic model for Item data structure
class Item(BaseModel):
    """
    Model for an item with basic properties.
    """
    name: str
    description: str = None
    price: float
    in_stock: bool = True


# Initialize the FastAPI application
app = FastAPI(
    title="My REST API",
    description="A simple REST API built with FastAPI",
    version="1.0.0"
)


# TODO: Create a root endpoint that returns a welcome message
@app.get("/")
def read_root():
    """
    Welcome endpoint that returns a greeting message.
    
    Returns:
        dict: A welcome message
    """
    return {
        "message": "Welcome to My REST API",
        "version": "1.0.0"
    }


# TODO: Create an endpoint that accepts a path parameter
@app.get("/items/{item_id}")
def get_item(item_id: int):
    """
    Get an item by its ID.
    
    Args:
        item_id (int): The unique identifier for the item
        
    Returns:
        dict: Item details including the requested ID
    """
    return {
        "item_id": item_id,
        "name": f"Sample Item {item_id}",
        "price": 19.99
    }


# TODO: Create an endpoint that accepts query parameters
@app.get("/items/")
def list_items(skip: int = 0, limit: int = 10):
    """
    List items with optional pagination parameters.
    
    Args:
        skip (int): Number of items to skip (default: 0)
        limit (int): Maximum number of items to return (default: 10)
        
    Returns:
        dict: A list of items
    """
    return {
        "items": [
            {"id": i, "name": f"Item {i}"} 
            for i in range(skip, skip + limit)
        ],
        "total": 100
    }


# TODO: Create a POST endpoint that accepts request body data
@app.post("/items/")
def create_item(item: Item):
    """
    Create a new item.
    
    Args:
        item (Item): Item data from request body
        
    Returns:
        dict: The created item with additional metadata
    """
    return {
        "message": "Item created successfully",
        "item": item,
        "id": 1
    }


# Run the application with: uvicorn starter-code:app --reload
