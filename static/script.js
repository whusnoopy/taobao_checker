var getRequestsParams = function() {
    var s1 = location.search.substring(1, location.search.length).split('&'),
        r = {}, s2, i;
    for (i = 0; i < s1.length; i += 1) {
        s2 = s1[i].split('=');
        if (s2[0].length <= 0) {
            continue;
        }
        r[decodeURIComponent(s2[0]).toLowerCase()] = decodeURIComponent(s2[1]);
    }
    return r;
};

$(function(){
    var paras = getRequestsParams();
    if (paras.input_url) {
        $('#input_url').val(paras.input_url);
    }
    if (paras.correct_price) {
        $('#correct_price').val(paras.correct_price);
    }
    if (paras.retry_times) {
        $('#retry_times').val(paras.retry_times)
    }
});