1. Clone the git repo
2. Install the requirements via "pip install -r requirements.txt"
3. Run the database migrations
   a. python manage.py makemigrations
   b. python manage.py migrate
4. Run the server
   a. python manage.py runserver
5. Visit http://localhost:8000/news/search -> Retrieve all AI related news
6. Visit http://localhost:8000/news/search/?q="search-keyword") -> Search with keyword
