'use strict';

/**
 * External imports
 */
var express = require('express');
var pug = require('pug');

/**
 * Internal imports
 */
var APIRouter = require('./src/routes/router')

/**
 * Pseudo-class container.
 */
var _Server = _Server || {};

// Setup express
_Server.ExpressRouter = express();
_Server.ExpressRouter.use(express.static(__dirname + '/public_html'));
_Server.ExpressRouter.engine('.html', require('ejs').__express);
_Server.ExpressRouter.set('views', __dirname);
_Server.ExpressRouter.set('view engine', 'pug');

// Routes
_Server.ExpressRouter.get('/', APIRouter.getGeneric().getDefault);
_Server.ExpressRouter.get('/api', APIRouter.getGeneric().getItemAPI);
_Server.ExpressRouter.get('/api/items', APIRouter.getItems().getDefault);

// Error handling middleware leave at the bottom.
_Server.ExpressRouter.use((req, res, next) => {
  throw new Error('The resource you\'re looking for was not found.');
});
_Server.ExpressRouter.use((err, req, res, next) => {
  console.error(err.stack);

  res.render('public_html/src/includes/error.pug', {
    'code': 'Uh-Oh!',
    'message': err.msg ? '500 ' + err.msg : err.message
  });
});

// Start listening to incoming requests.
_Server.PORT = process.env.OPENSHIFT_NODEJS_PORT || 8080;
_Server.IP = process.env.OPENSHIFT_NODEJS_IP || 'localhost';

_Server.ExpressRouter.listen(_Server.PORT, _Server.IP);
console.log('Server running on http://%s:%s', _Server.IP, _Server.PORT);