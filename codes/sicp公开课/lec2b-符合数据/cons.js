"use strict"


function makeRat(numer, denom) {
    let gcd_value = gcd(numer, denom);
    return cons(numer / gcd_value, denom / gcd_value);
}

function numer(rat) {
    return car(rat);
}

function denom(rat) {
    return cdr(rat);
}

function add(ratA, ratB) {
    return makeRat(
        numer(ratA) * denom(ratB) + numer(ratB) * denom(ratA)
        ,
        denom(ratA) * denom(ratB)
    );
}

function mul(ratA, ratB) {
    return makeRat(
        numer(ratA) * numer(ratB)
        ,
        denom(ratA) * denom(ratB)
    );
}

function cons(a, b) {
    return function(pick) {
        if(pick === 1) {
            return a;
        } else if (pick === 2) {
            return b;
        }
    }
} 

function car(pair) {
    return pair(1);
}

function cdr(pair) {
    return pair(2);
}

function gcd(a, b) {
    let min = a <= b ? a : b;
    let max = b > a ? b : a;
    if(min === max) {
        return min;
    } else {
        let result = 1;
        for(let i = 2; i <= min; i++) {
            if(min % i === 0 && max % i === 0) {
                result = i;
            }
        }  
        return result;
    }
}

console.log(`gcd(15, 9): ${gcd(15, 9)}`);

let r1 = makeRat(1, 3);
let r2 = makeRat(5, 3);

let r3 = add(r1, r2);

console.log("r3: " +typeof r3, r3.constructor);
console.log(`r3: ${numer(r3)} / ${denom(r3)}`);
console.log(car(r3));