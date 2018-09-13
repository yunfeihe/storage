---
title: 《javascript高级程序设计》小记
date: 2018-07-21 11:41:12
categories: 
- 编程
tags: 
- javascript
- 编程笔记
---
本文的目的旨在记录js红宝书重要但不经常使用的知识要点。

---

## script元素相关
* 对于 **带有src属性的script元素**，浏览器解析的时候会忽略script内部的js代码。也就是说只会下载执行外部脚本文件，忽略嵌入script元素内部的代码。
* script的 **defer** 属性，如果一个script元素其defer属性被指定，脚本会被 **立即下载** 但是 **延迟** 到页面加载完成后再执行。
* html5中script元素定义了 **async** 属性，效果类似defer属性，只适用于外部脚本文件，且不保证脚本的执行顺序遵顼其出现的顺序。

```javascript
//ps:defer和async属性的用法
<script type="text/javascript" async src="./foo.js"></script>       
//出现即为真值
<script type="text/javascript" defer src="./foo.js"></script> 
//同上
```

## 文档模式
文档模式也就是html文件第一行的\<!DOCTYPE>。文档模式早期由IE引入，用来规范浏览器的行为(主要时解析css方面的)。分为 **混杂模式(怪异模式)** 和 **标准模式**，后来其他浏览器也引入了文档模式的特性。重点在于如果 **html文件如果开头没有声明文档类型，则默认启用混杂模式** 所以写网页时一定要带着\<!DOCTYPE>，不然会碰到一些怪异的错误。

## 带名字的匿名函数
请思考以下代码
```javascript
let test = function foo() {console.log(foo)};
foo(); // => 找不到变量名
(function foo(){console.log(foo)});
foo(); // => 结果同上
```
以上两个语句都是函数表达式而非函数声明，当使用函数表达式对函数进行命名时，这个名字无法被外部访问到只存在与函数内部，与 **arguments.callee** 的作用类似。但是在strict模式下，callee属性被禁用，因此函数表达式这个特性就有用武之处了。此外，对于递归函数，采用此种方法调用自身，永远不用担心自身的函数名被覆盖或删除导致出错。
```javascript
function recurtion() {
    recurtion();
}
let foo1 = recurtion;
delete recurtion;
foo1(); //=>报错 recurtion未定义

let foo2 = function recurtion() {
    recurtion();
};
delete recurtion;
foo2(); // =>可以正常调用

```

## Object.defineProperty()
```javascript
let foo = {};
//为foo对象添加一个名为name值为1的属性
Object.defineProperty(foo, name, {
    configurable: false, // 此属性无法被删除，且不可以再被配置 
    enumerable: false ,  // 此属性不可枚举, 无法用for in读到
    writable: false ,    // 此属性变为只读，无法修改其值
    value: "1",      // 所对应的值
    //访问器属性
    get: function() {   //读取属性时调用的函数
        return this.name;   //this指向foo，而非本对象
    },
    set: function(newValue) {   //为属性赋值时调用的函数
        this.name = newValue    //
    }
});
```
Vue的双向绑定功能的基础就是此方法。此外还有个 **Object.defineProperties**方法，用于批量定义配置属性，用法类似，这就不多做介绍了。

