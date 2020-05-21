from django.test import TestCase
from .models import Editor,Article,tags
import datetime as dt

# Create your tests here.
class EditorTestClass(TestCase):

    # Set up method
    def setUp(self):
        '''
        Method to create an instance of the Editor class before every test
        '''
        self.james= Editor(first_name = 'James', last_name ='Muriuki', email ='james@moringaschool.com')

    # Testing  instance
    def test_instance(self):
        '''
        Method to confirm that the object is being instantiated correctly
        '''
        self.assertTrue(isinstance(self.james,Editor))
    
    # Testing Save Method
    def test_save_method(self):
        '''
        Method to save editor methods
        '''
        self.james.save_editor()
        editors = Editor.objects.all()
        self.assertTrue(len(editors) > 0)

class ArticleTestClass(TestCase):

    def setUp(self):
        '''
        Method to  define a new Editor and tag instance.
        '''
        # Creating a new editor and saving it
        self.james= Editor(first_name = 'James', last_name ='Muriuki', email ='james@moringaschool.com')
        self.james.save_editor()

        # Creating a new tag and saving it
        self.new_tag = tags(name = 'testing')
        self.new_tag.save()

        self.new_article= Article(title = 'Test Article',post = 'This is a random test Post',editor = self.james)
        self.new_article.save()

        self.new_article.tags.add(self.new_tag)

    def tearDown(self):
        '''
        Method to delete all instances of our models from the database after each test
        '''
        Editor.objects.all().delete()
        tags.objects.all().delete()
        Article.objects.all().delete()
    
    def test_get_news_today(self):
        '''
        Method to get the news for that particular day
        '''
        today_news = Article.todays_news()
        self.assertTrue(len(today_news)>0)
    
    def test_get_news_by_date(self):
        '''
        Method to confirm getting news according to a given date
        '''
        test_date = '2017-03-17'
        date = dt.datetime.strptime(test_date, '%Y-%m-%d').date()
        news_by_date = Article.days_news(date)
        self.assertTrue(len(news_by_date) == 0)