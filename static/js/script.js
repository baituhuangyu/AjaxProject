

//$(document).ready(function() {
//    var keyword = "";
//    var result = new Array();
//
//    var data_key = new Array();
//    var str_data_key= "";
//
//    for (var i = 0; i < result.length; i++) {
//        data_key[i] = "<li data-key='" + result[i] + "class='bdsug-overflow'>" + keyword + "<b>" + result[i].slice(keyword.length) + "</b>";
//        str_data_key = str_data_key + data_key[i];
//    }
//
//    var listdiv = "<div class='bdsug' style='height: auto; display: none;'><ul>";
//    var fouces = "<i class='c-icon c-icon-bear-round'></i>";
//    var alllistdiv = listdiv + str_data_key;
//
//
//
//});










///**
// * Created by hy on 2015/7/13.
// */
//function ajaxFunction()
//{
//    var the_request_url='../test';
//    var xmlHttp;
//
//    try {
//        xmlHttp = new XMLHttpRequest() ;
//    }
//    catch(e) {
//        try {
//            xmlHttp = new ActiveXObject("Msxml2.XMLHTTP");
//        }
//        catch(e) {
//            try {
//                xmlHttp = new ActiveXObject("Microsoft.XMLHTTP");
//            }
//            catch(e) {
//                alert("您的浏览器不支持ajax") ;
//                return false;
//            }
//        }
//    }
//
//    if (xmlHttp) {
//        xmlHttp.open('GET', the_request_url, true);
//        xmlHttp.onreadystatechange = function() {
//            if (xmlHttp.readyState ==4 ) {
//                if (xmlHttp.status == 200 ) {
//                    document.getElementById('vv').innerHTML = xmlHttp.responseText;
//                }
//            }
//        };
//        xmlHttp.send(null);
//    } else {
//        alert('error');
//    }
//}
//
