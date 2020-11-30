<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
<script type="text/javascript">

function init(){
	
	//db에 age value=2;
	var age = 4;
	// 폼은 자체 객체를 가지고 있음.
	document.pkc.age[age].checked=true;
}

</script>
</head>
<body onload="init()">
	<form name="pkc">
		<input type="radio" name="age" value="0">10이하
		<input type="radio" name="age" value="1">10대
		<input type="radio" name="age" value="2">20대
		<input type="radio" name="age" value="3">30대
		<input type="radio" name="age" value="4">40대
		<input type="radio" name="age" value="5">50대
	</form>
</body>
</html>