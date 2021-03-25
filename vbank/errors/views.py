from enum import Enum, IntEnum
from .models import Error
from django.db import IntegrityError


class ErrorCodes(IntEnum):
    GENERIC_ERROR = 0
    UNAUTHENTICATED_REQUEST = 1
    UNAUTHORIZED_REQUEST = 2
    COULD_NOT_PROCESS_UPLOAD = 3
    USER_CREATION_FAILED = 4
    USER_UPDATE_FAILED = 5
    USER_DELETION_FAILED = 6
    USER_ALREADY_EXISTS = 7
    USER_DOES_NOT_EXIST = 8
    USER_WITH_PHONE_ALREADY_EXIST = 9
    USER_WITH_EMAIL_ALREADY_EXIST = 10
    USER_WITH_USERNAME_ALREADY_EXIST = 11
    FILE_FORMAT_INVALID = 12
    FILE_UPLOAD_FAILED = 13
    ACCOUNT_CREATE_FAILED = 14





# base error
def getError(code, defaultMessage):
    try:
        _, _ = Error.objects.get_or_create(
            code=code, description=defaultMessage)

        return {'errorCode': code, 'message': defaultMessage}

    except IntegrityError:
        return {'errorCode': code, 'message': defaultMessage}

