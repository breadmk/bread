<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
<style type="text/css">
li{list-style:none;}
</style>
<script type="text/javascript">

 function view(){
	 //none, inline, block, inline-block <--속성은 4가지.
	 document.getElementById("aa").style.display="block";
	 
 }	
 function view2(){
	 //hidden,visible <- 속성은 2가지
	 document.getElementById("bb").style.visibility="visible";
	 
 }	

</script>
</head>
<body>
<a href="javascript:view()">보이기</a>

<ul>
	<li>대방어</li>
	<li style="display: none;" id="aa">참돔</li> <!-- 자기 공간 없이 숨는거 -->
	<li>감성돔</li>
	<li>갈치</li>
</ul>
	<hr>
	<a href="javascript:view2()">보이기</a>
<ul>
	<li>삼겹살</li>
	<li style="visibility: hidden;" id="bb">항정살</li> <!-- 자기공간을 가지고 숨는거 -->
	<li>목살</li>
	<li>갈매기살</li>
</ul>
</body>
</html>