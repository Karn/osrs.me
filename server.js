var express = require('express');
var { parse, print, graphql, buildSchema } = require('graphql');

var pug = require('pug');

var dataItems = require('./data/items.json');

// Construct a schema, using GraphQL schema language
var schema = buildSchema(`
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
  }
`);

// The root provides a resolver function for each API endpoint
var root = {
  item: ({ ids }) => {
    if (ids) {
      let output = [];
      for (let i in ids) {
        if (dataItems["item"][ids[i]]) {
          console.log(dataItems["item"][ids[i]])
          output.push(dataItems["item"][ids[i]]);
        }
      }
      return output;
    }

    return dataItems["item"];
  },

  npc: () => {
    return 'Npc!';
  }
};

var app = express();
app.use(express.static(__dirname + '/public_html'));
app.engine('.html', require('ejs').__express);
app.set('views', __dirname);
app.set('view engine', 'pug');

app.get('/', (req, res) => {
  res.render('public_html/src/index.pug', {
    'page_title': ''
  });
});

const itemsPresetDefault = "{id name description}";
const itemsPresetExtended = "{id name description type members quest_item tradeable stackable weight}"
const itemsPresetStatsDetails = "{stab slash crush range magic}"
const itemsPresetStatsBonusDetails = "{strength range_strength magic_strength prayer}"
const itemsPresetAllStats = "{attack" + itemsPresetStatsDetails + " defence " + itemsPresetStatsDetails + " bonus " + itemsPresetStatsBonusDetails + "}"
const itemsPresetFull = "{id name description type members quest_item tradeable stackable weight stats " + itemsPresetAllStats + "}"

app.get('/api/items', (req, res) => {
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

  graphql(schema, query, root).then((response) => {
    res.render('public_html/src/api_view.pug', {
      'page_title': 'Request browser',
      'api_endpoint': req.path,
      'api_query': print(parse(query)),
      'api_response': JSON.stringify(response.data, null, 4)
    });
  });
});

// Error handling middleware leave at the bottom.
app.use((req, res, next) => {
  res.render('public_html/src/includes/error.pug', {
    'code': '404',
    'message': 'The resource you\'re looking for was not found.'
  });
});

app.use((err, req, res, next) => {
  console.error(err.stack);

  res.render('public_html/src/includes/error.pug', {
    'code': '500',
    'message': err.msg
  });
});

var port = process.env.OPENSHIFT_NODEJS_PORT || 8080,
  ip = process.env.OPENSHIFT_NODEJS_IP || 'localhost';

app.listen(port, ip);
console.log('Server running on http://%s:%s', ip, port);