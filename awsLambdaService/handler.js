'use strict';

'use strict';

const bookmarksCreate = require('./crud/bookmarks-create.js');
const bookmarksReadAll = require('./crud/bookmarks-read-all.js');
const bookmarksReadOne = require('./crud/bookmarks-read-one.js');
const bookmarksUpdate = require('./crud/bookmarks-update.js');
const bookmarksDelete = require('./crud/bookmarks-delete.js');

module.exports.create = (event, context, callback) => {
  bookmarksCreate(event, (error, result) => {
    const response = {
      statusCode: 200,
      headers: {
        "Access-Control-Allow-Origin" : "*"
      },
      body: JSON.stringify(result),
    };

    context.succeed(response);
  });
};

module.exports.readAll = (event, context, callback) => {
  bookmarksReadAll(event, (error, result) => {
    const response = {
      statusCode: 200,
      headers: {
        "Access-Control-Allow-Origin" : "*"
      },
      body: JSON.stringify(result),
    };

    context.succeed(response);
  });
};

module.exports.readOne = (event, context, callback) => {
  bookmarksReadOne(event, (error, result) => {
    const response = {
      statusCode: 200,
      headers: {
        "Access-Control-Allow-Origin" : "*"
      },
      body: JSON.stringify(result),
    };

    context.succeed(response);
  });
};

module.exports.update = (event, context, callback) => {
  bookmarksUpdate(event, (error, result) => {
    const response = {
      statusCode: 200,
      headers: {
        "Access-Control-Allow-Origin" : "*"
      },
      body: JSON.stringify(result),
    };

    context.succeed(response);
  });
};

module.exports.delete = (event, context, callback) => {
  bookmarksDelete(event, (error, result) => {
    const response = {
      statusCode: 200,
      headers: {
        "Access-Control-Allow-Origin" : "*"
      },
      body: JSON.stringify(result),
    };



    context.succeed(response);
  });
};