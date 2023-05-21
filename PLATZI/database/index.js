const mongoose = require("mongoose");

mongoose.connect("mongodb://localhost:27017/platzi")
.then(()=> console.log("La conexion ha sido exitosa"))
.catch((err)=> console.log(err))
