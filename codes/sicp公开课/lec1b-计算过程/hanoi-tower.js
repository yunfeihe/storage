
//recursivc version
function move(n, from, to, spare) {
    // console.log(arguments);
    if(n === 1) {
        console.log('Move',n,'from',from,'to',to);
        return;
    } else {
        move(n-1, from, spare, to);
        move(1, from, to, spare);
        move(n-1, spare, to, from);
    }
}

//recursive version
function move_(n, from, to, spare) {
    // console.log(arguments);
    if(n === 1) {
        let disk = from.pop();
        to.push(disk);
        console.log('Move',disk,'from',from,'to',to,"\n\n");
        return;
    } else {
        move_(n-1, from, spare, to);
        move_(1, from, to, spare);
        move_(n-1, spare, to, from);
    }
}

let start = ["NO.1", 3, 2, 1];

let to = ["NO.2"];

let spare = ["NO.3"];

// move(5, 1, 2, 3);
move_(start.length - 1, start, to, spare);