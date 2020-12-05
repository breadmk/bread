<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
<style type="text/css">
	ul{
		position: absolute;
		left:10px;
		top:10px;
		visibility: hidden;		/* 숨기는 법 */
	}
	#first{
	width:800px;
	height:30px;
	margin:auto;
	position: relative;		/* 자식들이 다 묶여서 움직이게끔 해주는거 */
	background: red;
	}
	#second{
	width:800px;
	height:30px;
	margin:auto;
	position: relative;		/* 자식들이 다 묶여서 움직이게끔 해주는거 */
	background: blue;
	}
</style>

<script type="text/javascript">

function view() {
	document.getElementById("sub").style.visibility="visible"
}
function hide() {
	document.getElementById("sub").style.visibility="hidden"
}
function view1() {
	document.getElementById("sub1").style.visibility="visible"
}
function hide1() {
	document.getElementById("sub1").style.visibility="hidden"
}

</script>

</head>
<body>

<div id="first" onmouseenter="view()" onmouseleave="hide()"> 수산물  <!-- 마우스가 올라가면 함수 호출 -->
	<ul id="sub">	
		<li>횟감</li>
		<li>어패류</li>
		<li>두족류</li>
		<li>기타 등등</li>
	</ul>
</div>
<hr>
<div id="second" onmouseenter="view1()" onmouseleave="hide1()">횟감
	<ul id="sub1">
		<li>광어</li>
		<li>우럭</li>
		<li>농어</li>
		<li>방어</li>
		<li>참돔</li>
	</ul>
	
</div>
</body>
</html>