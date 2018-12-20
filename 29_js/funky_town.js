// Team Whirlpool (Mohtasim Howlader and Soojin Choi)
// SoftDev1 pd8
// K28 -- Sequential Progression
// 2018-12-19

var fibonacci = function(n){
    if (n < 2)
      return n;
    retVal = fibonacci(n - 1) + fibonacci(n - 2);
    //console.log(retVal)
    return retVal;
};

var gcd = function(a,b){
    if (a == 0)
	return b;
    if (b == 0)
	return a;
    if (a < b)
	return gcd(a, b % a);
    else
	return gcd(b, a % b)
};

var list = ["mohtasim", "soojin", "bob", "sam", "emily"];

var randomStudent = function(){
    randVal = Math.floor(Math.random() * 3);
    console.log(list[randVal]);
    return list[randVal];
};

var eventOne = function(){
    randVal = Math.floor(Math.random() * 10);
    retVal = fibonacci(randVal);
    console.log(retVal);
    return retVal;
};

var b = document.getElementById('button');
console.log(b);
var c = b.addEventListener('click', eventOne);
