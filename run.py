from wedding import create_app
from dotenv import load_env

# Load environment variables.
load_env()

# Create app.
app = create_app()

if __name__ == '__main__':
    app.run()
