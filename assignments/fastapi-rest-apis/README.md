# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn to build modern web APIs using the FastAPI framework. You'll create endpoints that handle HTTP requests, work with route parameters and query strings, and return JSON responses. This assignment teaches you how to design and implement REST APIs that follow web standards.

## 📝 Tasks

### 🛠️ Set Up Your FastAPI Application

#### Description

Create the basic structure of a FastAPI application and verify it runs correctly.

#### Requirements

Your application should:

- Import FastAPI and create an application instance
- Define a root endpoint that returns a welcome message
- Include proper startup information (app title and description)
- Run the application successfully using `uvicorn`

### 🛠️ Create API Endpoints with Route Parameters

#### Description

Build multiple endpoints that accept different types of parameters and return appropriate responses.

#### Requirements

Your API should:

- Create a GET endpoint with a path parameter (e.g., `/items/{item_id}`)
- Handle at least two different resource types with separate endpoints
- Return JSON responses with appropriate data structure
- Include proper HTTP status codes
- Validate input parameters and handle invalid requests

### 🛠️ Implement Query Parameters and Data Models

#### Description

Add query parameters to your endpoints and use data models to structure request/response data.

#### Requirements

Your API should:

- Create endpoints that accept query parameters (optional filtering options)
- Define Python dataclasses or Pydantic models for structured data
- Return consistent JSON responses using your data models
- Handle requests with different combinations of parameters
- Implement basic error handling for invalid queries

