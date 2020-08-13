from django.core.exceptions import MultipleObjectsReturned, ObjectDoesNotExist
from .exceptions import *
from .models import *

def getMenu():
    try:
        menu = MainMenuElementModel.objects.all()
    except ObjectDoesNotExist:
        raise CantGetMenu()
    except BaseException:
        raise Shit()
    else:
        return menu


def getFooter():
    try:
        result = {}
        footerBlocks = FooterBlockModel.objects.all()
        allFooterContent = FooterContentModel.objects.all()
        size = footerBlocks.count()
        i = 0
        while i < size:
            footerContent = allFooterContent.filter(footerBlock=footerBlocks[i])
            footerElement = {'name': footerBlocks[i].name,
                             'content': footerContent}
            result[i] = footerElement
            i += 1
        return result
    except NameError:
        raise MyBad()
    except IndexError:
        raise NoFooter()
    except ObjectDoesNotExist:
        raise NoFooter()


def getSingleArticlesByNames(*articleNames):
    singleArticles = {}
    try:
        for name in articleNames:
            singleArticles[str(name)] = getSingleArticleByName(name)
    except MultipleObjectsReturned:
        raise ManySingleArticles()
    except ObjectDoesNotExist:
        raise NoSingleArticles()
    except:
        raise Shit()

def getSingleArticleByName(name):
    try:
        singleArticle = SingleArticleModel.objects.get(name=name)
    except MultipleObjectsReturned:
        raise ManySingleArticles()
    except ObjectDoesNotExist:
        raise NoSingleArticles()
    except:
        raise Shit()
    return singleArticle


def getAllArticles():
    try:
        outArticles = ArticleModel.objects.all()
    except ObjectDoesNotExist:
        return outArticles
    except:
        raise Shit()
    return outArticles


def getArticleByTitle(articleTitle):
    try:
        article = ArticleModel.objects.get(title=articleTitle)
    except ObjectDoesNotExist:
        raise NoArticle()
    except MultipleObjectsReturned:
        raise ManyArticles()
    except:
        raise Shit()
    else:
        return article


def getArticleById(articleId):
    try:
        article = ArticleModel.objects.get(id=articleId)
    except ObjectDoesNotExist:
        raise NoArticle()
    except MultipleObjectsReturned:
        raise ManyArticles()
    except:
        raise Shit()
    else:
        return article


def getCommentsByArticle(article):
    try:
        comments = CommentModel.objects.filter(article=article)
    except ObjectDoesNotExist:
        raise NoComments()
    except:
        raise Shit()
    else:
        return comments


def getCommentById(commentId):
    try:
        comment = CommentModel.objects.get(id=commentId)
    except ObjectDoesNotExist:
        raise NoComments()
    except MultipleObjectsReturned:
        raise ManyComments()
    except:
        raise Shit()
    else:
        return comment

#return dictionary of pairs {footerBlock, footerContent} where footerContent might be also dictionary


