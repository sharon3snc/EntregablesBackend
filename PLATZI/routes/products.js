const express = require('express');
const Product = require('../models/product');

const router = express.Router();

// Obtener todos los productos
router.get('/', async (req, res, next) => {
  try {
    const products = await Product.find();
    res.json(products);
  } catch (error) {
    res.status(500).send({error:error.message});
  }
});

// Crear un nuevo producto
router.post('/', async (req, res, next) => {
  try {
    const product = new Product(req.body);
    const createdProduct = await product.save();
    res.status(201).json(createdProduct);
  } catch (error) {
    res.status(400).send({error: error.message});
  }
});

// Actualizar un producto existente
router.put('/:id', async (req, res, next) => {
  try {
    const { id } = req.params;
    const updatedProduct = await Product.findByIdAndUpdate(id, req.body, {
      new: true,
    });
    res.json(updatedProduct);
  } catch (error) {
    res.status(500).send({error: error.message});
  }
});

// Eliminar un producto existente
router.delete('/:id', async (req, res, next) => {
  try {
    const { id } = req.params;
    await Product.findByIdAndDelete(id);
    res.sendStatus(204);
  } catch (error) {
    res.status(500).send({error: error.message});
  }
});

module.exports = router;
