from django.http import JsonResponse
from http import HTTPStatus


def badRequestResponse(data):
    return errorResponse(HTTPStatus.BAD_REQUEST, data)


def unAuthorizedResponse(data):
    return errorResponse(HTTPStatus.FORBIDDEN, data)


def unAuthenticatedResponse(data):
    return errorResponse(HTTPStatus.UNAUTHORIZED, data)


def resourceConflictResponse(data):
    return errorResponse(HTTPStatus.CONFLICT, data)


def resourceNotFoundResponse(data):
    return errorResponse(HTTPStatus.NOT_FOUND, data)


def internalServerErrorResponse(data):
    return errorResponse(HTTPStatus.INTERNAL_SERVER_ERROR, data)


def errorResponse(httpStatusCode, data):
    return JsonResponse(data, status=httpStatusCode, safe=False)


# success responses
def createdResponse(message="", body={}):
    return successResponse(HTTPStatus.CREATED, message=message, body=body)


def paginatedResponse(httpStatusCode=HTTPStatus.OK, message="", body={}, pagination={}, **kwargs):
    return successResponse(httpStatusCode, message, body, pagination, kwargs)


def successResponse(httpStatusCode=HTTPStatus.OK, message="", body={}, pagination=None, kwargs=None):
    responseData = dict()
    responseData['data'] = body
    responseData['metaData'] = kwargs
    responseData['message'] = message

    if pagination:
        responseData['pagination'] = pagination

    response = JsonResponse(responseData, status=httpStatusCode, safe=False)
        
    return response

# helper functions

def getUserIpAddress(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip
