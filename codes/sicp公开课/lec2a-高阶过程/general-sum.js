

function add(a, b) {
    return a + b;
}

function dec(value) {
    return value - 1;
}

function inc(value) {
    return value + 1;
}

function square(x) {
    return x * x;
}

//求和 1 2 3 .... n;
function sum_int(a, b) {
    if(a > b) {
        return 0;
    } else {
        return add(a, sum_int(inc(a), b));
    }
}

console.log("sum-int: ", sum_int(1, 3));   // => 6

//求和 1*1 + 2*2 + .... + n * n
function sum_square(a, b) {
    if(a > b) {
        return 0;
    } else {
        return add(square(a), sum_square(inc(a), b));
    }
}

console.log("sum-square: ", sum_square(1, 3));  //=>14

function sum(term, start, next_start, end) {
    if(start > end) {
        return 0;
    } else {
        return add(term(start), sum(term, next_start(start), next_start, end));
    }
}

function int_term(x) {
    return x;
}

function int_next(x) {
    return x + 1;
}

//求和 1 2 3 .... n;
console.log("general-sum-int: ", sum(int_term, 1, int_next, 3));   // => 6

function square_term(x) {
    return x * x;
}

function square_next(x) {
    return x + 1;
}

//求和 1*1 + 2*2 + .... + n * n
console.log("general-sum-square: ", sum(square_term, 1, square_next, 3));   // => 14
