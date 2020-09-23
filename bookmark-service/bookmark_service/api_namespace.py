import http.client
from datetime import datetime
from flask_restplus import Namespace, Resource, fields
from bookmark_service import config
from bookmark_service.models import BookmarkModel
from bookmark_service.token_validation import validate_token_header
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

model = {
    'id': fields.Integer(),
    'username': fields.String(),
    'title': fields.String(),
    'summary': fields.String(),
    'timestamp': fields.DateTime(),
}
bookmark_model = api_namespace.model('bookmark', model)


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
        args = search_parser.parse_args()
        search_param = args['search']
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
