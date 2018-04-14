"use strict"

function sqrt(x) {
    return try_sqrt(1, x);
}

function try_sqrt(guess, x) {
    if(isGoodEnough(guess, x)) {
        return guess;
    } else {
        console.log("improved guess: ", improve(guess, x));
        return try_sqrt(improve(guess, x), x);
    }
}

function isGoodEnough(guess, x) {
    const MIN_DIFF = 0.001;
    let real_diff = guess * guess - x;
    real_diff = real_diff < 0 ? -real_diff : real_diff;
    if(real_diff < MIN_DIFF) {
        return true;
    } else {
        return false
    }
}

function improve(guess, x) {
    let improved_value = (x / guess + guess) / 2;
    return improved_value;
}

console.log("value:", sqrt(2));