<!--
	1) 문서를 읽을때 부메뉴는 숨긴다. 
	2) 마우스가 주메뉴에 올라가면 부메뉴가 보인다
	3) 마우스가 주메뉴에서 나가면 부메뉴를 숨긴다.
-->
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
		visibility: hidden; /* 1)  부메뉴를 숨겨라 */ 
	}
	#first .sub li{
		list-style-type: none;		
	}

</style>
<script type="text/javascript">


function sub_view(n) { // 2))) 부메뉴를 보여라 
	//현재 문서의 모든 뷰 메뉴는 class="sub"로 되어있다...=>동일한 이름의 클래스는 배열로 처리.
	//수산물 = sub[0] , 농산물 = sub[1], 장난감 = sub[2], 안주류 = sub[3]
	document.getElementsByClassName("sub")[n].style.visibility="visible"; 
	//  getElements  s 주의하자
}

function sub_hide(n) { // 3))) 부메류를 숨겨라
	document.getElementsByClassName("sub")[n].style.visibility="hidden";
}

</script>
</head>
<body>
	<!-- 메뉴만드는 태그는 무엇일까요 정답: 모든 태그가 가능하다. (div,ul)-->
	<!-- li태그는 block => 한 행을 차지, inline => 자기 공간만 차지 -->
	<div id="first">
	<ul id="aa">		  <!-- 인덱스 값을 넣어준다. -->
		<li onmouseenter="sub_view(0)" onmouseleave="sub_hide(0)">수산물
			<ul class="sub">
				<li>돔 류</li>
				<li>조개류</li>
				<li>잡 어</li>
				<li>그 외</li>
			</ul>
		</li>
							 <!-- 인덱스 값을 넣어준다. -->
		<li onmouseenter="sub_view(1)" onmouseleave="sub_hide(1)">농산물
			<ul class="sub">  <!-- 인덱스 값을 넣어준다. -->
				<li>잡곡류</li>
				<li>뿌리식물</li>
				<li>양파</li>
				<li>당근</li>
			</ul>
		</li>				 <!-- 인덱스 값을 넣어준다. -->
		<li onmouseenter="sub_view(2)" onmouseleave="sub_hide(2)">장난감
		<ul class="sub">
				<li>뽀로로</li>
				<li>헬로카봇</li>
				<li>터닝메카드</li>
				<li>슈렉</li>
			</ul>
		</li>				 <!-- 인덱스 값을 넣어준다. -->
		<li onmouseenter="sub_view(3)" onmouseleave="sub_hide(3)">안주류
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