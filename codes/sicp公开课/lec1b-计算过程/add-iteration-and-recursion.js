"use strict"

//time  o(n)
//space o(1)
function add_iteration(a, b) {
    if(a === 0) {
        return b;
    } else {
        return add_iteration(a - 1, b + 1);
    }
}


//time  o(n)
//space o(n)
function add_recursion(a, b) {
    if(a === 0) {
        return b;
    } else {
        return 1 + (add_recursion(a - 1, b));
    }
}

function time_log(fn, ...args) {
    let t1 = new Date();
    let value =  fn(...args);
    let t2 = new Date();
    console.log(`经过时间: ${t2 - t1}ms, value: ${value}`);
}

time_log(add_iteration, 5000, 10000000000);
time_log(add_recursion, 5000, 10000000000);
