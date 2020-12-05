<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
<style type="text/css">

 	#aa li{   	/* id = aa 아래 li */
 		list-style-type:none;
		display: inline-block; /* inline을 주면 block형이 가지고 있는 가로,세로 같은 값을 부여하지 못 한다 */
		/* inline-block 은 inline 성능도 가지면서 크기 조절도 됨 */
		border: 1px solid red;
		width: 120px;
		height:35px;
		text-align: center;
		padding-top:10px; /* 글자와 top 과의 간격 */
		/* margin은 태그끼리와의 간격 */
		margin-left: 20px;
		
	}

	#bb li{
	list-style-type:none;
	float:left;
	border: 1px solid red;
	}

</style>
</head>
<body>
	<!-- 메뉴만드는 태그는 무엇일까요 정답: 모든 태그가 가능하다. (div,ul)-->
	<!-- li태그는 block => 한 행을 차지, inline => 자기 공간만 차지 -->
	<ul id="aa">
		<li>수산물</li>
		<li>농산물</li>
		<li>장난감</li>
		<li>안주류</li>
	</ul>
	<hr>
	<ul id="bb">
		<li>수산물</li>
		<li>농산물</li>
		<li>장난감</li>
		<li>안주류</li>
	</ul>
	<br>
	<hr>
	<h1>하하</h1>
	<h2>허허</h2>
	<span>span</span>
	<a>a</a>
	<div>div1</div>
</body>
</html>