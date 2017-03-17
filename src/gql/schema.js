'use strict';

/**
 * External imports
 */
var { parse, print, graphql, buildSchema } = require('graphql');

/**
 * Pseudo-class container.
 */
var _GQLSchema = _GQLSchema || {};

_GQLSchema.schema = buildSchema(`
    type Stats {
        stab: Int
        slash: Int
        crush: Int
        magic: Int
        range: Int
    }

    type Bonus {
        strength: Int
        range_strength: Int
        magic_strength: Int
        prayer: Int
    }

    type CombinedStats {
        attack: Stats
        defence: Stats
        bonus: Bonus
    }

    type Item {
        id: Int
        type: String
        name: String
        description: String
        members: Boolean
        quest_item: Boolean
        tradeable: Boolean
        stackable: Boolean
        weight: Int
        stats: CombinedStats
    }

    type Query {
        item(ids: [Int]!): [Item]
        npc: String
    }`);

module.exports = {
    getDefaultSchema: () => {
        return _GQLSchema.schema;
    }
}