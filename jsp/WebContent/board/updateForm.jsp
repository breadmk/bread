<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<% System.out.println("board/updateForm.jsp"); %>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>게시판 글수정</title>

<meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>
<script type="text/javascript">
$(function(){
	$("#cancelBtn").click(function(){
		
		history.back();
	});
	
});

</script>

</head>
<body>
<div class="container">
<h1>게시판 글수정</h1>
<form action="update.jsp" method="post">
<div class="form-group">
<!-- 	for / name / (title)을 모두 맞춰줘야함. -->
  <label for="no">번호:</label>
  <input type="text" class="form-control" id="no" name="no"
  readonly="readonly" value="10"> <!-- readonly 처럼 글씨만 있으면 true 라는 뜻 -->
 <!-- 번호 칸은 수정이 안 되게 끔 막아놓음. readonly -->
</div>

<div class="form-group">
  <label for="title">제목:</label>
  <input type="text" class="form-control" id="title" name="title"
   title="제목을 입력하셔야 합니다." required="required" 
  placeholder="제목을 5글자 이상으로 입력하세요.">
  
</div>
<div class="form-group">
<!-- 	for / name / (title)을 모두 맞춰줘야함. 자바단에서는 set/get 맞춰야함 -->
  <label for="content">내용:</label>
  <textarea class="form-control" rows="5" id="content" name="content">
 자바기반의 웹프로그램개발 입니다.</textarea>
  <label for="writer">작성자:</label>
  <input type="text" class="form-control" id="writer" name="writer"
  value="이영환">
</div>
<button class="btn btn-default">수정</button> 
<button class="btn btn-default" type="reset">다시입력</button> 
<button class="btn btn-default" type="button" id="cancelBtn">취소</button> 
<!-- button 기본 타입은 submit -->
</form>
</div>
</body>
</html>












