function sqrt(x) {
    //f(y) = y * y - x 的根就是x的平方根，在此我们
    //可以利用牛顿迭代法来求此根
    return newtonMethod(function(y){
        return Math.abs(y * y - x);
    }, 1);
}

function newtonMethod(f, guess) {
    //牛顿迭代法的基本原理也是一个函数，但此函数的根并不是我们要求的x的平方根
    //在这里此函数的根无意义，有意义的是此函数的不动点，这才是我们要求的x的平方根
    //因此将此函数传给fixedpoint求不动点
    df = derive(f);
    return fixedPoint(function(y){
        return y - (f(y) / df(y));
    }, guess);    
}

function derive(procudure) {
    //求给定函数导数的不精确求法
    const deltaX = 0.0001;
    return function(x) {
        return (procudure(x + deltaX) - procudure(x)) / deltaX; 
    } 
}

function fixedPoint(f, guess) {
    //注意此时f是个可以通过不断迭代自身来减少与目标值的差距，类似的还有海伦求平方根中应用的平均阻尼法
    //不断迭代直到所得新数值与旧数值差距足够小，返回新数值，也就是x的平方根
    let newValue = f(guess);
    if(isCloseEnough(newValue, guess)) {
        return newValue;
    } else {
        return fixedPoint(f,newValue);
    }
}

function isCloseEnough(newValue, oldValue) {
    const tolerance = 0.0001;
    let diff = Math.abs(newValue - oldValue);
    if(diff < tolerance) {
        return  true;
    } else {
        return false;
    }
}

console.log("sqrt(4)", sqrt(9));