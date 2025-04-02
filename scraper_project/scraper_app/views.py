import requests
from bs4 import BeautifulSoup
from .models import Article
from .serializers import ArticleSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status



 
def scrape_ai_news():
    url = "https://www.khaleejtimes.com/search?q=AI"  # AI-related news search
    response = requests.get(url)
        
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        articles = soup.find_all("article", class_="listing-normal-teasers")
        for article in articles:
            title = article.get_text(strip=True)
            link = article.find("a", href=True)["href"]
            actual_link = "https://www.khaleejtimes.com"+link # need to move to models.py to append base Url on creating new record

            # Save only new AI-related articles
            if not Article.objects.filter(link=actual_link).exists():
                Article.objects.create(title=title, link=actual_link)
        print("News Scraping Completed Succesfully")
    else:
        print("Scraping News Failed")

@api_view(['GET', 'POST'])
def search_articles(request):
    query = request.GET.get('q', '')
    data = []
    if query:
        articles = Article.objects.filter(title__icontains=query)
    else:
        articles = Article.objects.all()
    if articles:
        data = [{"title": article.title, "link": article.link} for article in articles]
    serializer = ArticleSerializer(articles, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
    
            