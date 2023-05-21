const express = require("express");
const app = express();
const mongoose = require("mongoose");
const http= require("http");
const productsRoutes= require('./routes/products');
require('./database');

const PORT = 3000;

app.use('/api/v1/products', productsRoutes);

app.use((err,req,res,next) => {
    console.error(err);
    res.status(500).json({error:'Error interno del servidor'});
});

app.use(express.json());
app.use(express.urlencoded({extended:false}));

app.listen(
    PORT,
    () => console.log(`servidor escuchando en el puerto ${PORT}`)
);
