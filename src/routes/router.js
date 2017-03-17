'use strict';

/**
 * External imports
 */
var express = require('express');
var pug = require('pug');
var { parse, print, graphql, buildSchema } = require('graphql');

/**
 * Internal imports
 */
var SchemaFactory = require('../gql/schema');
var GQLRouter = require('../gql/root');

/**
 * Pseudo-class container.
 */
var _APIRouter = _APIRouter || {};

/**
 * Constants
 */
const itemsPresetDefault = "{id name description}";
const itemsPresetExtended = "{id name description type members quest_item tradeable stackable weight}"
const itemsPresetStatsDetails = "{stab slash crush range magic}"
const itemsPresetStatsBonusDetails = "{strength range_strength magic_strength prayer}"
const itemsPresetAllStats = "{attack" + itemsPresetStatsDetails + " defence " + itemsPresetStatsDetails + " bonus " + itemsPresetStatsBonusDetails + "}"
const itemsPresetFull = "{id name description type members quest_item tradeable stackable weight stats " + itemsPresetAllStats + "}"

// Construct a schema, using GraphQL schema language
var schema = SchemaFactory.getDefaultSchema();

_APIRouter.generic = {
    getDefault: (req, res) => {
        res.render('public_html/src/index.pug', {
            'page_title': ''
        });
    }
}

_APIRouter.itemsRoute = {
    getDefault: (req, res) => {
        let query = "";

        let g = req.query.g;
        let ids = req.query.ids;
        let preset = req.query.preset;

        if (g) {
            query = g;
        } else if (ids) {
            let p = "";
            switch (preset) {
                case "extended":
                    p = itemsPresetExtended;
                    break;
                case "full":
                    p = itemsPresetFull;
                    break;
                default:
                    p = itemsPresetDefault;
            }
            query = "{ item(ids: [" + ids.split(',') + "])" + p + "}";
        }

        graphql(schema, query, GQLRouter.getRoot()).then((response) => {
            // Only return raw data if the correct header is present.
            if (req.get("X-REQUEST-RAW") === 'true') {
                res.send(response.data);
                return;
            }

            res.render('public_html/src/api_view.pug', {
                'page_title': 'Request browser',
                'api_endpoint': req.path,
                'api_query': print(parse(query)),
                'api_response': JSON.stringify(response.data, null, 4)
            });
        });
    }
}


module.exports = {
    /**
     * Exposes generic routes.
     */
    getGeneric: () => {
        return _APIRouter.generic;
    },

    /**
     * Exposes routes specific to item data.
     */
    getItems: () => {
        return _APIRouter.itemsRoute;
    }
}
