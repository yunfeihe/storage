function isCloseEnough(a, b) {
    const tolerance = 0.0001;
    let value =Math.abs(a - b);
    if(value < tolerance) {
        return true;
    } else {
        return false;
    }
}

function sqrt(x) {
    return fixedPoint(function(y){
        return ((x / y) + y) / 2;
    }, 1);
}


function fixedPoint(f, guess) {
    let newValue = f(guess);
    if(isCloseEnough(guess, newValue)) {
        return newValue;
    } else {
        return fixedPoint(f, newValue);
    }
}

function averageDamp(f) {
    return function(y) {
        return (y + f(y)) / 2;
    }
}

function newSqrt(x) {
    return fixedPoint(averageDamp(function(y){
        return x / y;
    }), 1);
}

console.log("sqrt(4): ", sqrt(4));
console.log("newSqrt(2): ", newSqrt(4));