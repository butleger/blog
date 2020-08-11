from django.core import exceptions


class CustomException(Exception):
    message = None
    errorBlock = None
    specialMessage = ""

    def __init__(self, message="No message"):
        specialMessage = message

class CantGetMenu(exceptions.ObjectDoesNotExist, CustomException):
    message = "database have not menu"
    errorBlock = "menu"

    def __str__(self):
        return self.message


class CantGetFooter(exceptions.ObjectDoesNotExist, CustomException):
    message = "I dont get footer"
    errorBlock = "footer"

    def __str__(self):
        return self.message

class ManyArticles(exceptions.MultipleObjectsReturned, CustomException):
    message = "in database more than 1 article with this title"
    errorBlock = "article"

    def __str__(self):
        return self.message


class NoArticle(exceptions.ObjectDoesNotExist, CustomException):
    message = "in database no article with this title"
    errorBlock = "article"

    def __str__(self):
        return self.message


class NoComments(exceptions.ObjectDoesNotExist, CustomException):
    message = 'Cant get comments from database'
    errorBlock = 'comments'

    def __str__(self):
        return self.message


class NoComment(exceptions.ObjectDoesNotExist, CustomException):
    message = 'Cant get comment from database'
    errorBlock = 'comment id'

    def __str__(self):
        return self.message


class ManyComments(exceptions.MultipleObjectsReturned, CustomException):
    message = 'Get more than 1 comment'
    errorBlock = 'comment id'

    def __str__(self):
        return self.message


class NoFooter(exceptions.ObjectDoesNotExist, CustomException):
    message = 'No Footer Content'
    errorBlock = 'Footer'

    def __str__(self):
        return self.message


class Shit(CustomException):
    message = "catch base exception"
    errorBlock = "your ass"

    def __str__(self):
        return self.message


class MyBad(NameError, CustomException):
    message = "Use wrong name of functions or properties"
    errorBlock = "Your code"

    def __str__(self):
        return self.message


def getAllFuckedContent(ex):
    return {'arg': ex.message,
            'errorBlock': ex.errorBlock,
            'specialMessage': ex.specialMessage}
