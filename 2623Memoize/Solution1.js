/**
 * @param {Function} fn
 */
function memoize(fn) {
    let cacheObject = {};
    return function(...args) {
        const key = JSON.stringify(args);
        if (key in cacheObject) {
            return cacheObject[key];
        }else{
            cacheObject[key] = fn(...args);
            return cacheObject[key];
        }
    }
}