<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
<style type="text/css">
#aa,#bb{
	position: absolute;
	left:100px;
	top:100px;
	background: red;
	width:100px;
	height: 100px;
}
	#main{
	position: relative;
	border: 1px solid blue;
	margin-left: 300px;
	width:400px;
	height:400px;
	}
</style>
</head>
<body>
 <div id="aa">
 </div>
 
 <div id="main">
 	<div id="bb"></div>
 </div>
</body>
</html>