<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
<style type="text/css">
	#layer{
	
		position: absolute;
		left:10px;
		top:100px;
		width:80px;
		heighet:40px;
		background: red;
	}
</style>
<script type="text/javascript">
	var n=10;
function move() {
	n++;
	document.getElementById("layer").style.left=n+"px";  /* 숫자라서 "px" 줘야함 */
	 if(n>=500)
		   clearInterval(ss);
}

function start() { //나는 left의 값이 500px이 되면 멈추고 싶다.  => clearInterval(객체명)
	ss = setInterval(move,10);  // 무한반복임. 누르면 >>>>>>>저세상까지감;
	//var을 함수에서 사용하면 다른 함수에서 사용을 못 함. 그래서 다른 곳에서 ss를 사용할때는 var를 뺴고 사용해야한다. //전역변수
}
</script>

</head>
<body>

<input type="button" onclick="move()" value="클릭">
<input type="button" onclick="start()" value="계속이동">
<div id="layer">
	광고 !! ~~~
</div>
</body>
</html>