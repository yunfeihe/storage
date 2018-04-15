"use strict"

//time o(fib_recursion(n))
//space o(n)
function fib_recursion(n) {
    if(n <= 2) {
        return 1;
    } else {
        return fib_recursion(n - 1) + fib_recursion(n - 2);
    }
}


//time o(n)
//space o(1)
function fib_iteration(n) {
    function fib_iter(a, b, count) {
        if(count === 1) {
            return b;
        } else {
            return fib_iter(b, a + b, count - 1);
        }
    }
    let result = fib_iter(0, 1, n);

    return result;
}

//time  o(n)
//space o(n)
function better_fib_recursion(n) {
    let memory = [null, 1, 1];  //基1，所以0为null
    function fib_recursion_base(n) {
        let result = memory[n];
        if(typeof result === "undefined") {
            memory[n] = fib_recursion_base(n - 1) + fib_recursion_base(n - 2);
            result = memory[n];
        }
        return result;
    }
    return fib_recursion_base(n);
}



console.log("fib-iter:", fib_iteration(1400));
console.log("fib-recu:", fib_recursion(1400));
console.log("better-fib-recu:", better_fib_recursion(1400));
