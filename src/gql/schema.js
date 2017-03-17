'use strict';

module.exports = {
    getDefaultSchema: () => {
        return `
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
            }`;
    }
}