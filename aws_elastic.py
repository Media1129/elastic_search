curl -XGET -u 'Media1129:Miulab524$' 'https://search-recipe-tnx35rcz5nydy2h2hry2qqqmvy.us-east-1.es.amazonaws.com/recipe/_search?q=mars'


# create
curl -XPUT -u 'Media1129:Miulab524$' 'https://search-recipe-tnx35rcz5nydy2h2hry2qqqmvy.us-east-1.es.amazonaws.com/veggies/_doc/1' -d '{"name":"beet", "color":"red", "classification":"root"}' -H 'Content-Type: application/json'

# create with json file
curl -XPOST -u 'Media1129:Miulab524$' 'https://search-recipe-tnx35rcz5nydy2h2hry2qqqmvy.us-east-1.es.amazonaws.com/_bulk' --data-binary @recipe_data.json -H 'Content-Type: application/json'

# search with json file
curl -XGET -u 'Media1129:Miulab524$' 'https://search-recipe-tnx35rcz5nydy2h2hry2qqqmvy.us-east-1.es.amazonaws.com/veggies/_search?q=color:yellow'