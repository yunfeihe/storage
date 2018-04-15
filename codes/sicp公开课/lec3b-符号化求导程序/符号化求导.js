function log(...args) {
    return console.log(...args);
}

function make_exp(operator, operand1, operand2) {
    return [operator, operand1, operand1];
}

function optor(exp) {
    return exp[0];
}

function opand1(exp) {
    return exp[1];
}

function opand2(exp) {
    return exp[2];
}

let e = [
    '+', 
    ['*', 'a', ['*', 'x', 'x']], 
    [
        '+', 
        ['*', 'b', 'x'],
        'c',
    ],
];

// a * x^2 + b * x + c
// let e = make_exp('+', 
//                  make_exp('*', 'a', make_exp('*', 'x', 'x')),
//                  make_exp('+', 
//                         make_exp('*', 'b', 'x'),
//                         'c'     
//                 )
//         )



function logexp(exp) {
    let str;
    if(exp.constructor !== Array) {
        return exp;
    } else {
        str = `(${optor(exp)} ${logexp(opand1(exp))} ${logexp(opand2(exp))})`;
        return str;
    }
}


function dreiv(exp, var_token) {
    // console.log("row exp: " + logexp(exp));
    if(isConstant(exp, var_token)) {
        // log("应用isConstant: " + logexp(exp));
        return '0';
    } else if (isSameVar(exp, var_token)) {
        // log("应用isSameVar " + logexp(exp));
        return '1';
    } else if (isSum(exp)) {
        // log("应用isSum: " + logexp(exp));
        return makeSum(
            dreiv(opand1(exp), var_token), 
            dreiv(opand2(exp), var_token)
        );
    } else if (isProduct(exp)) {
        // log("应用isProduct: " + logexp(exp));
        //干，开始这里忘了对返回的乘积求导，导致debug了半天
        //干干，根本不是上面的问题，而是返回操作数求导之和，而不是之积，我要爆炸了
        let product = makeSum(
            makeProduct(dreiv(
                opand1(exp), var_token), 
                opand2(exp)
            ),
            makeProduct(
                dreiv(opand2(exp), var_token),
                opand1(exp)
            )
        );
        return product;
    }
}

function isConstant(exp, var_token) {
    if(isAtom(exp) && exp !== var_token) {
        return true;
    } else {
        return false;
    }
}

function isAtom(item) {
    if(item.constructor !== Array) {
        return true;
    } else {
        return false;
    }
}

function isSameVar(exp, var_token) {
    if(isAtom(exp) && exp === var_token) {
        return true;
    } else {
        return false;
    }
}

function isSum(exp) {
    if(optor(exp) === '+') {
        return true;
    } else {
        return false;
    }
}

function makeSum(a, b) {
    if(a === '0'){
        return b;
    } else if (b === '0') {
        return a;
    } else {
        return ['+', a, b];
    }
    return ['+', a, b];

}

function isProduct(exp) {
    if(optor(exp) === '*') {
        return true;
    } else {
        return false;
    }
}

function makeProduct(a, b) {
    if(a === '0') {
        return '0';
    } else if (b === '0') {
        return '0';
    } else if (a === '1') {
        return b;
    } else if (b === '1') {
        return a;
    } else {
        return ['*', a, b];
    }
}
console.log("normal: " + 'a * x^2 + b * x + c\n');

console.log("o exp:", logexp(e), '对x求导');
console.log("reuslt:", logexp(dreiv(e, 'x')));

log("\n");

console.log("o exp:", logexp(e), '对c求导');
console.log("reuslt:", logexp(dreiv(e, 'c')));