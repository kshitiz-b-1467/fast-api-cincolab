class HttpStatus:
    HTTP_200_OK = {
        "status_code": 200,
        "message": "OK",
        "detail": "The request has succeeded.",
    }
    HTTP_201_CREATED = {
        "status_code": 201,
        "message": "Created",
        "detail": "The request has been fulfilled and a new resource has been created.",
    }
    HTTP_204_NO_CONTENT = {
        "status_code": 204,
        "message": "No Content",
        "detail": "The server has successfully fulfilled the request, but there is no content to send back.",
    }
    HTTP_400_BAD_REQUEST = {
        "status_code": 400,
        "message": "Bad Request",
        "detail": "The server cannot process the request due to a client error.",
    }
    HTTP_401_UNAUTHORIZED = {
        "status_code": 401,
        "message": "Unauthorized",
        "detail": "The request requires user authentication.",
    }
    HTTP_403_FORBIDDEN = {
        "status_code": 403,
        "message": "Forbidden",
        "detail": "The server understood the request, but refuses to authorize it.",
    }
    HTTP_404_NOT_FOUND = {
        "status_code": 404,
        "message": "Not Found",
        "detail": "The requested resource could not be found on the server.",
    }
    HTTP_500_INTERNAL_SERVER_ERROR = {
        "status_code": 500,
        "message": "Internal Server Error",
        "detail": "An unexpected condition was encountered by the server.",
    }
    HTTP_503_SERVICE_UNAVAILABLE = {
        "status_code": 503,
        "message": "Service Unavailable",
        "detail": "The server is currently unable to handle the request.",
    }


def health_check_response(status, timestamp):
    return {
        "timestamp": timestamp,
        "status": status,
    }
