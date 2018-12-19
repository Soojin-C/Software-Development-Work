// Team Whirlpool (Mohtasim Howlader and Soojin Choi)
// SoftDev1 pd8
// K28 -- Sequential Progression
// 2018-12-19

var fibonacci = function(n){
    if (n == 0)
	return 0;
    if (n == 1)
	return 1;
    return fibonacci(n - 1) + fibonacci(n - 2);
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
    return list[randVal];
};
