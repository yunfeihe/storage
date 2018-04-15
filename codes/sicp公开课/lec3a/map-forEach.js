function cons(a, b) {
    return [a, b];
}

function car(pairs) {
    // console.log("car", pairs[0]);
    return pairs[0];
}

function cdr(pairs) {
    // console.log("cdr", pairs[1]);

    return pairs[1];
}

function LIST(first, ...args) {
    function recursion(first, rest) {
        if(rest.length === 0) {
            return null;
        } else {
            return cons(first, recursion(rest[0], rest.slice(1)));
        }
    }
    return recursion(first, args);
}


function MAP(p, LIST) {
    if (LIST === null) {
        return null;
    } else {
        return cons(p(car(LIST)), MAP(p, cdr(LIST)));
    }
}


function forEach(p, LIST) {
    if(LIST === null) {
        console.log("done");
    } else {
        // console.log("LIST", LIST, "\n");
        p(car(LIST));
        // console.log("cdr LIST", cdr(LIST), "\n");
        forEach(p, cdr(LIST));
    }
}

let ls = LIST(1, 2, 3, 4, 5, 6, "hello, world");
let doublels = MAP((item) => {return item * 2}, ls);
forEach(function(item){
        console.log("item:", item);
    }, doublels)

//能力不济，只能实现倒序版迭代形式的map
function MAP_iteration(p, LIST) {
    // let result = null;
    function iterator(p, LIST, result) {
        if(LIST === null) {
            return result;
        } else {
            result = cons(p(car(LIST)), result);
            let rest = cdr(LIST);
            return iterator(p, rest, result);
        }
    }
    return iterator(p, LIST, null);
}


let doublels2 = MAP_iteration((item) => {return item * 2}, ls);
console.log("doublels2", doublels2);
forEach(function(item){
        console.log("item:", item);
    }, doublels2)