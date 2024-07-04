class Article:
    all = []

    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        Article.all.append(self)

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        if isinstance(value, Author):
            self._author = value
        else:
            raise ValueError("Author must be an instance of Author class")

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, value):
        if isinstance(value, Magazine):
            self._magazine = value
        else:
            raise ValueError("Magazine must be an instance of Magazine class")

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if isinstance(value, str) and 5 <= len(value) <= 50:
            self._title = value
        else:
            raise ValueError("Title must be a string between 5 and 50 characters")
    def __repr__(self):
        return f"Article(title='{self.title}', author='{self.author.name}', magazine='{self.magazine.name}')"


class Author:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not hasattr(self, '_name'):
            if isinstance(value, str) and len(value) > 0:
                self._name = value
            else:
                raise ValueError("Name must be a string longer than 0 characters")
        else:
            raise AttributeError("Cannot change the name once set")

    def articles(self):
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        return list(set(article.magazine for article in self.articles()))

    def add_article(self, magazine, title):
        new_article = Article(self, magazine, title)
        return new_article

    def topic_areas(self):
        if not self.articles():
            return None
        return list(set(magazine.category for magazine in self.magazines()))
    def __repr__(self):
        return f"Author(name='{self.name}')"

class Magazine:
    all = []

    def __init__(self, name, category):
        self.name = name
        self.category = category
        self._articles = []
        Magazine.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and 2 <= len(value) <= 16:
            self._name = value
        else:
            raise ValueError("Name must be a string between 2 and 16 characters")

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._category = value
        else:
            raise ValueError("Category must be a string longer than 0 characters")

    def articles(self):
        return [article for article in Article.all if article.magazine == self]

    def add_article(self, article):
        self._articles.append(article)

    def contributors(self):
        return list(set(article.author for article in self.articles()))

    def article_titles(self):
        titles = [article.title for article in self.articles()]
        return titles if titles else None

    def contributing_authors(self):
        author_counts = {}
        for article in self.articles():
            author = article.author
            if author in author_counts:
                author_counts[author] += 1
            else:
                author_counts[author] = 1
        return [author for author, count in author_counts.items() if count > 2] or None

    @classmethod
    def top_publisher(cls):
        if not cls.all:
            return None
        return max(cls.all, key=lambda magazine: len(magazine.articles()))
    def __repr__(self):
        return f"Magazine(name='{self.name}', category='{self.category}')"
   
   
   
author = Author("Carry Bradshaw")
magazine = Magazine("Vogue", "Fashion")
article = Article(author, magazine, "How to wear a tutu with style")




print(author.articles())
print(author.magazines() )
author.add_article(magazine, "Dating life in NYC")
print(magazine.articles())
print(magazine.contributors())
print(Magazine.top_publisher())