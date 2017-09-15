'use strict';

/**
 * Data imports
 */
var dataItems = require('../../data/raw/items.json');

/**
 * Pseudo-class container.
 */
var _GQLRoot = _GQLRoot || {};

_GQLRoot.root = {
    item: ({ ids }) => {
    if (!ids) 
      return {};

    let output = [];
    for (let i in ids) {
      if (dataItems["item"][ids[i]]) {
        console.log(dataItems["item"][ids[i]])
        output.push(dataItems["item"][ids[i]]);
      }
    }
    return output;
  },

  npc: () => {
    return 'Npc!';
  }
}

module.exports = {
    getRoot: () => {
        if (!_GQLRoot || !_GQLRoot.root)
            throw new Error("GQLRouter not intilaized.")

        return _GQLRoot.root;
    }
}