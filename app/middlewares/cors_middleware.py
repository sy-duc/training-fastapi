from fastapi.middleware.cors import CORSMiddleware

# List of domains that you want to allow to send requests
origins = [
    "http://localhost:3000",
]

def add_cors_middleware(app):
    # Add CORS middleware to FastAPI
    app.add_middleware(
        CORSMiddleware,
        allow_origins = origins,   # List of allowed origins
        allow_credentials = True,  # Allow sending cookies (credentials) in CORS requests
        allow_methods = ["*"],     # Allow all HTTP methods (GET, POST, PUT, DELETE, ...)
        allow_headers = ["*"],     # Allow all headers
    )
