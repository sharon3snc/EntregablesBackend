const mongoose = require('mongoose');

const productSchema = new mongoose.Schema({
    id: String,
    title: String,
    price: Number,
    description: String,
    category: {
        id: Number,
        name: String,
        image: String,
    },
    images: [String],
});

const Product = mongoose.model('Product', productSchema);

module.exports = Product;
