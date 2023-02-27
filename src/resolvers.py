from ariadne import QueryType, MutationType
from app import db
from app.models import UserModel
from app.schemas import UserSchema


query = QueryType()
mutation = MutationType()
user_schema = UserSchema()


@query.field("users")
def resolve_users(_, info):
    users = UserModel.query.all()
    return user_schema.dump(users, many=True)


@query.field("user")
def resolve_user(_, info, id):
    user = UserModel.query.get(id)
    return user_schema.dump(user)


@mutation.field("createUser")
def resolve_create_user(_, info, name, email, password):
    new_user = UserModel(name=name, email=email, password=password)
    db.session.add(new_user)
    db.session.commit()
    return user_schema.dump(new_user)


@mutation.field("updateUser")
def resolve_update_user(_, info, id, **kwargs):
    user = UserModel.query.get(id)
    for key, value in kwargs.items():
        setattr(user, key, value)
    db.session.commit()
    return user_schema.dump(user)


@mutation.field("deleteUser")
def resolve_delete_user(_, info, id):
    user = UserModel.query.get(id)
    db.session.delete(user)
    db.session.commit()
    return id