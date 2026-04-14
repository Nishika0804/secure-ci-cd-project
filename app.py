# Simple demo application
AWS_SECRET_ACCESS_KEY = "AKIAIOSFODNN7EXAMPLE" # fake secret for detection

def greet(name):
    return f"Hello, {name}! Welcome to Secure Pipeline"

if __name__ == "__main__":
    print(greet("DevOps"))