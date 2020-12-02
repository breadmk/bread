<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
<script src="https://code.jquery.com/jquery-3.5.1.min.js"></script>
<script type="text/javascript">

	var a=100;
		b=100;
		function aa(){
// 			var a=99;
// 			var b=77;

			a=99;
			b=77;
		}
		function bb(){
			var c= 90;
		}
	aa();
	alert(a+" "+b);
	bb();
	alert(c);
	
// 	var 은 변수 만들때 앞에 적는 키워드
// 	함수밖에서는 있으나 없으나 동일하게 인식
// 	함수내에서 var이 있으면 함수내에서만 인식하는 지역변수,
//  var이 없이 생성되면 전역변수
	
	
// 	function test(){
// 		document.getElementById("pkc").style.color="blue";
// 	}
// 	window.onload=function(){
// 		document.getElementById("pkc").style.color="blue";
// 	}
	$(function(){
		$('#pkc').css('color','red');
// 		document.getElementById("pkc").style.color="blue";
	})
</script>
</head>
<body> <!--  문서를 읽을때 하하하하 라는 글자를 파란색으로  -->
	<span id="pkc">하하하하</span>
</body>
</html>
