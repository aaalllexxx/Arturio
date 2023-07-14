from models.user import User


def get_user(request):
    session_id = request.cookies.get("session_id")
    user = User.query.filter_by(session_id=session_id)
    if user:
        return user.first()
    return False
