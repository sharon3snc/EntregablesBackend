const http = require('http');
const fs = require('fs');

const fetchanimalData = async () => {
    return new Promise ((resolve,reject) => {
        fs.readFile('pokemon.json', 'utf8', (err,data)=> {
            if (err){
                reject(err);
            } else {
                resolve(JSON.parse(data));
            }
        });
    });
};

const handleRequest = async (req,res) => {
    const pokemonName = decodeURI(req.url.substring(1));
    const animalData = await fetchanimalData();

    const pokemonData = animalData.find(pokemon => (pokemon.id == pokemonName)|| (Object.values(pokemon.name).includes(pokemonName)));

    if (pokemonData) {
        const response = {
            'Tipo': pokemonData.type,
            'HP': pokemonData.base.HP,
            'Attack': pokemonData.base.Attack,
            'Defense': pokemonData.base.Defense,
            'Sp. Attack': pokemonData.base["Sp. Attack"],
            'Sp. Defense': pokemonData.base["Sp. Defense"],
            'Speed': pokemonData.base.Speed,
        };
        res.writeHead(200, {'Content-Type': 'application/json'});
        res.end(JSON.stringify(response, null, 2));
    } else {
        res.writeHead(404, {'Content-Type': 'text/plain'});
        res.end('Pokemon no encontrado');
    }
};

const server = http.createServer(handleRequest);

server.listen(3000, () => {
    console.log('servidor escuchando en el puerto 3000');
});
