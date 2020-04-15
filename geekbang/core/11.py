class Document:
    WELCOME_STR = 'Welcome! The context for this book is {}.'

    def __init__(self, title, author, context):
        print('init function called')
        self.title = title
        self.author = author
        self.__context = context

    # 类函数,类函数的第一个参数一般为 cls，表示必须传一个类进来
    @classmethod
    def create_empty_book(cls, title, author):
        return cls(title=title, author=author, context='nothing')

    # 成员函数
    def get_context_length(self):
        return len(self.__context)

    # 静态函数 ,与类没有什 么关联，最明显的特征便是，静态函数的第一个参数没有任何特殊性
    # 静态函数可以用来做一些简单独立的任务
    @staticmethod
    def get_welcome(context):
        return Document.WELCOME_STR.format(context)


empty_book = Document.create_empty_book("hello", "world")
print(empty_book.get_context_length())
print(empty_book.get_welcome('indeed nothing'))

from abc import ABCMeta, abstractmethod


class Entity(metaclass=ABCMeta):
    @abstractmethod
    def get_title(self):
        pass

    @abstractmethod
    def set_title(self, title):
        pass


class Document(Entity):
    def get_title(self):
        return self.title

    def set_title(self, title):
        self.title = title


document = Document()
document.set_title('Harry Potter')
print(document.get_title())
# 这行会报错，不能实例化抽象类
entity = Entity()
