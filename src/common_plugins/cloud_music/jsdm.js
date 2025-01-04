function hash33(t) {
    for (var e = 0, i = 0, n = t.length; i < n; ++i)
        e += (e << 5) + t.charCodeAt(i);
    return 2147483647 & e
}

function getToken(p_skey) {
    var str = p_skey || '',
        hash = 5381;
    for (var i = 0, len = str.length; i < len; ++i) {
        hash += (hash << 5) + str.charCodeAt(i);
    }
    return hash & 0x7fffffff;
}

function guid() {
    return 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function(c) {
        var r = Math.random() * 16 | 0, v = c == 'x' ? r : (r & 0x3 | 0x8);
        return v.toString(16);
    }).toUpperCase();
};


function S() {
    var e = (new Date).getTime();
    return "xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx".replace(/[xy]/g, function(t) {
        var n = (e + 16 * Math.random()) % 16 | 0;
        return e = Math.floor(e / 16),
            ("x" === t ? n : 7 & n | 8).toString(16)
    })
}


function a(a) {
    var d, e, b = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", c = "";
    for (d = 0; a > d; d += 1)
        e = Math.random() * b.length,
            e = Math.floor(e),
            c += b.charAt(e);
    return c
}

