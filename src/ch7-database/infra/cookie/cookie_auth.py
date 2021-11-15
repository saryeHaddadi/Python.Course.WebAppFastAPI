import hashlib
from typing import Optional
from starlette.responses import Response
from starlette.requests import Request
from infra.cookie.num_convert import try_int

AUTH_KEY = 'pypi_account'

def set_auth(response: Response, user_id: int):
    """Log in the user by setting the auth cookie.

    Args:
        response (Response): [description]
        user_id (int): [description]
    """
    hash_val = __hash_text(str(user_id))
    val = "{}:{}".format(user_id, hash_val)
    response.set_cookie(AUTH_KEY, val, secure=False, httponly=True, samesite='Lax')


def __hash_text(text: str) -> str:
    text = 'salty__' + text + '__text'
    return hashlib.sha512(text.encode('utf-8')).hexdigest()


def get_user_id_from_auth_cookie(request: Request) -> Optional[int]:
    if AUTH_KEY not in request.cookies:
        return None

    val = request.cookies[AUTH_KEY]
    parts = val.split(':')
    if len(parts) != 2:
        return None

    user_id = parts[0]
    hash_val = parts[1]
    hash_val_check = __hash_text(user_id)
    if hash_val != hash_val_check:
        print("Warning: Hash mismatch, invalid cookie value")
        return None

    return try_int(user_id)


def logout(response: Response):
    """Log out the user by removing the auth cookie.

    Args:
        response (Response): [description]
    """
    response.delete_cookie(AUTH_KEY)


