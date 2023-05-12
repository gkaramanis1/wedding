from wedding import create_app
from dotenv import load_dotenv

# Load environment variables.
load_dotenv()

# Create app.
app = create_app()

if __name__ == '__main__':
    app.run()
