<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
<style type="text/css">
	#layer{
	position:absolute;
	left:200px;
	top:100px;
	background: yellow;
	width: 200px;
	height: 200px;
	}

</style>
<script type="text/javascript">
	var chk=0;
	function hide() {
		if(chk%2==0){
		document.getElementById("layer").style.visibility="hidden";
		}else{
		document.getElementById("layer").style.visibility="visible";
		}
		chk++;
	}
// 	setTimeout(hide,3000);
	setInterval(hide,1000);
</script>
</head>
<body>
<div id="layer">
	광고입니다.
</div>

</body>
</html>