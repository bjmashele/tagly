import http.client
from datetime import datetime
from flask_restplus import Namespace, Resource, fields
from bookmark_service import config
from bookmark_service.models import BookmarkModel
from bookmark_service.models import TagModel
from bookmark_service.models import UserModel
from bookmark_service.token_validation import validate_token_header
from bookmark_service.token_validation import generate_token_header
from bookmark_service.db import db
from flask import abort

api_namespace = Namespace('api', description='API operations')


def authentication_header_parser(value):
    username = validate_token_header(value, config.PUBLIC_KEY)
    if username is None:
        abort(401)
    return username


# Input and output formats for bookmark

authentication_parser = api_namespace.parser()
authentication_parser.add_argument('Authorization', location='headers',
                                   type=str,
                                   help='Bearer Access Token')

bookmark_parser = authentication_parser.copy()
bookmark_parser.add_argument('title', type=str, required=True,
                             help='Title of the bookmark')

tag_parser = authentication_parser.copy()
tag_parser.add_argument('name', type=str, required=True,
                             help='Name of the tag')

login_parser = authentication_parser.copy()
login_parser.add_argument('username', type=str, required=True,
                             help='Must have username')
login_parser.add_argument('password', type=str, required=True,
                             help='Must have password')

bookmarkModelSchema = {
    'id': fields.Integer(),
    'username': fields.String(),
    'title': fields.String(),
    'summary': fields.String(),
    'tags': fields.String(),
    'timestamp': fields.DateTime(),
}

tagModelSchema = {
    'id': fields.Integer(),
    'username': fields.String(),
    'name':fields.String(),  
}

userModelSchema = {
    'id': fields.Integer(),
    'username': fields.String(),
    'password': fields.String(),
}

bookmark_model = api_namespace.model('bookmark', bookmarkModelSchema)
tag_model = api_namespace.model('tag', tagModelSchema)
user_mode = api_namespace.model('user', userModelSchema)


@api_namespace.route('/me/bookmarks/')
class MeBookmarkListCreate(Resource):

    @api_namespace.doc('list_bookmarks')
    @api_namespace.expect(authentication_parser)
    @api_namespace.marshal_with(bookmark_model, as_list=True)
    def get(self):
        '''
        Retrieves all the bookmarks
        '''
        args = authentication_parser.parse_args()
        username = authentication_header_parser(args['Authorization'])

        bookmarks = (BookmarkModel
                     .query
                     .filter(BookmarkModel.username == username)
                     .order_by('id')
                     .all())
        return bookmarks

    @api_namespace.doc('create_bookmark')
    @api_namespace.expect(bookmark_parser)
    @api_namespace.marshal_with(bookmark_model, code=http.client.CREATED)
    def post(self):
        '''
        Create a new bookmark
        '''
        args = bookmark_parser.parse_args()
        username = authentication_header_parser(args['Authorization'])

        new_bookmark = BookmarkModel(username=username,
                                     text=args['text'],
                                     timestamp=datetime.utcnow())
        db.session.add(new_bookmark)
        db.session.commit()

        result = api_namespace.marshal(new_bookmark, bookmark_model)

        return result, http.client.CREATED


@api_namespace.route('/bookmarks/')
class BookmarkList(Resource):

    @api_namespace.doc('list_bookmarks')
    @api_namespace.marshal_with(bookmark_model, as_list=True)
    def get(self):
        '''
        Retrieves all the bookmarks
        '''
        
        
        query = BookmarkModel.query

        # Old code, that it's not case insensitive in postgreSQL
        # query = (query.filter(bookmarkModel.text.contains(search_param)))

        query = query.order_by('id')
        bookmarks = query.all()

        return bookmarks


@api_namespace.route('/bookmarks/<int:bookmark_id>/')
class BookmarksRetrieve(Resource):

    @api_namespace.doc('retrieve_bookmark')
    @api_namespace.marshal_with(bookmark_model)
    def get(self, bookmark_id):
        '''
        Retrieve a bookmark
        '''
        bookmark = BookmarkModel.query.get(bookmark_id)
        if not bookmark:
            # The bookmark is not present
            return '', http.client.NOT_FOUND

        return bookmark

#Tags
@api_namespace.route('/me/tags/')
class MeTagListCreate(Resource):

    @api_namespace.doc('list_tags')
    @api_namespace.expect(authentication_parser)
    @api_namespace.marshal_with(tag_model, as_list=True)
    def get(self):
        '''
        Retrieves all the tags
        '''
        args = authentication_parser.parse_args()
        username = authentication_header_parser(args['Authorization'])

        tags = (TagModel
                     .query
                     .filter(TagModel.username == username)
                     .order_by('id')
                     .all())
        return tags

    @api_namespace.doc('create_tag')
    @api_namespace.expect(tag_parser)
    @api_namespace.marshal_with(tag_model, code=http.client.CREATED)
    def post(self):
        '''
        Create a new tag
        '''
        args = bookmark_parser.parse_args()
        username = authentication_header_parser(args['Authorization'])

        new_tag = TagModel(username=username,
                                     name=args['name'],
                                     timestamp=datetime.utcnow())
        db.session.add(new_tag)
        db.session.commit()

        result = api_namespace.marshal(new_tag, tag_model)

        return result, http.client.CREATED@api_namespace.route('/me/tags/')

#User Login
@api_namespace.route('/login/')
class UserLogin(Resource):

    @api_namespace.doc('login')
    @api_namespace.expect(login_parser)
   
    def post(self):
        '''
        Login and return Authorization header
        '''
        args = login_parser.parse_args()
        

        user = (UserModel
                     .query
                     .filter(UserModel.username == args['username'])
                     .first())
        # validate user creds
        if not user:
            return ' ', http.client.UNAUTHORIZED
        
        if user.password != args['password']:
            return ' ',http.client.UNAUTHORIZED

        # if user creds are valid
        header = generate_token_header(user.name, config.PRIVATE_KEY)
        return {'Authorized': header}, http.client.OK
