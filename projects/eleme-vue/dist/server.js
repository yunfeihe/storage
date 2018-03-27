const express = require("express");
const fs = require("fs");
var jsonData =  JSON.parse(fs.readFileSync("./data.json"));
// console.log("json: " + jsonData.toString());
let app = express();

let apiRouter = express.Router();

app.use("/api", apiRouter);
app.use("/static", express.static("./static"));

apiRouter.get("/", function(req, res){
    res.json({msg: "hello, world."});
    
});

apiRouter.get("/goods", function(req, res, err){
    res.setHeader("Access-Control-Allow-Origin", "*");

    console.log("goods");
    res.json({
        code: 0,
        data: jsonData.goods,
    });

});

apiRouter.get("/seller", function(req, res, err){
    if(false) {
        console.log("err: " + err);
    } else {
        res.setHeader("Access-Control-Allow-Origin", "*");

        res.json({
            code: 0,
            data: jsonData.seller,
        });
    }
});

apiRouter.get("/ratings", function(req, res, err){
    if(false) {
        console.log("err: " + err);
    } else {
        res.setHeader("Access-Control-Allow-Origin", "*");

        res.json({
            code: 0,
            data: jsonData.ratings,
        });
    }
});

app.get("/", function(req, res, err){
    res.sendfile("./index.html");
});

let server = app.listen(8000, "localhost",function(){
    console.log("server start at", server.address());
});