<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
<style type="text/css">
	#first {
		margin:auto;  /* 중앙정렬 */
		width:800px;
		height:100px;
	}

 	#first #aa > li{   	/* id = aa 아래 li  // >를 주면 자식개념 */
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
		position: relative; /* 개인 공간 */
	}

	#first .sub {	/* 서브메뉴를 가지는 ul태그 */
		position: absolute; /* 부모가 relative 니까 그 아래 들어감 */
		border : 1px solid blue;
		padding-left: 0px;  /* 기본 간격 제거 */
		top: 50px;
		width :120px;
	}
	#first .sub li{
		list-style-type: none;		
	}
	#aa .sub2{
		position:absolute;
		border : 1px solid blue;
		padding-left: 0px;
		top:50px;
		width:120px;
	}
	#aa .sub2 li{
		list-style-type: none;
	}
</style>
</head>
<body>
	<!-- 메뉴만드는 태그는 무엇일까요 정답: 모든 태그가 가능하다. (div,ul)-->
	<!-- li태그는 block => 한 행을 차지, inline => 자기 공간만 차지 -->
	<div id="first">
	<ul id="aa">
		<li>수산물
			<ul class="sub">
				<li>돔 류</li>
				<li>조개류</li>
				<li>잡 어</li>
				<li>그 외</li>
			</ul>
		</li>
		
		<li>농산물
			<ul class="sub2">
				<li>잡곡류</li>
				<li>뿌리식물</li>
				<li>양파</li>
				<li>당근</li>
			</ul>
		</li>
		<li>장난감
		<ul class="sub">
				<li>뽀로로</li>
				<li>헬로카봇</li>
				<li>터닝메카드</li>
				<li>슈렉</li>
			</ul>
		</li>
		<li>안주류
		<ul class="sub">
				<li>육</li>
				<li>해</li>
				<li>공</li>
				<li>호프</li>
		</ul>
		</li>
	</ul>
	</div>

	
	

</body>
</html>