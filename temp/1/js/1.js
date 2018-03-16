var main = function(){
    log("start 1 main");
    // displaySlideShowByIndex(0);

    setTimeout(displaySlideShowByIndex(1), 5000);
};

var displaySlideShowByIndex = function(index){
    //索引从零开始
    log("changeTo", index);
    var images = sa("#slide-show li");
    for(var i=0; i<images.length; i++){
        images[i].style.transform ="translate(-" +  100 * index + "%)" ;
    }
    
};

main();