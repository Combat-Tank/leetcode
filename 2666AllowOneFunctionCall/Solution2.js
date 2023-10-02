/**
 * @param {Function} fn
 * @return {Function}
 */
var once = function(fn) {
    let called = false;
    return (...args) => {
        if(called == false){
            called = true;
            return fn(...args);
        }
    }
};