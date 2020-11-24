<%@page import="com.webjjang.board.dto.BoardDTO"%>
<%@page import="java.util.List"%>
<%@page import="com.webjjang.board.dao.BoardDAO"%>
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
    
<%-- jstl등록 //자바페이지 주석 --%>
<%@taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<% System.out.println("board/list.jsp"); %>
<!-- DB에서 데이터를 가져오는 자바 프로그램 작성 -->

<%
// 여기가 자바 프로그램입니다.
// DAO를 생성하고 호출하고 사용한다. 
BoardDAO dao = new BoardDAO();
List<BoardDTO> list = dao.list();
// java와 jsp 에서 공통으로 사용하는 데이터 영역에 해당되는 데이터객체=>requset를 주요 사용한다.
request.setAttribute("list", list);

// List<BoardDTO> list = dao.list();request.setAttribute("list", list);
// request.setAttribute("list",dao.list()); 해도 들어감;
%>

<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>게시판 리스트</title>
<!-- 라이브러리 등록 - jQuery, Bootstrap : CDN 방식 (인터넷 소스 사용)-->
<meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>

<style type="text/css">
/*  마우스 올라왔을때 */
.dataRow:hover{
/* rgb 3자리 r - 0~15 : 색상을 16단계로 나눈다. 16 * 16 * 16 가지 색상을 나타낸다. 
   rgb 6자리 r - 0~255 : 색상을 256단계로 나눈다. 256 * 256 * 256 가지 색상을 나타낸다.*/
	background: #ddd; /* 회상 */
	cursor: pointer;  /* 손가락 표시 */
}

</style>

<script type="text/javascript">

$(function(){ //onready - html - body 부분의 내용이 다 loading 되면 동작되도록 한다.
// 	데이터 한 줄 클릭하면 글 보기로 이동되는 이벤트 처리 
	$(".dataRow").click(function(){
		var no = $(this).find(".no").text();
// 		location.href = "view.jsp"; <a> 태그랑 같음.
		location = "view.jsp?no="+no;
		
	});
});

</script>

</head>
<body>
<div class="container"> <!-- 오타나면 안됨. 양쪽에 붙은 내용을 띄어줌. -->
<h1>게시판 리스트</h1>
<table class="table">
<tr>
	<th>번호</th>
	<th>제목</th>
	<th>작성자</th>
	<th>작성일</th>
	<th>조회수</th>
</tr>
<%-- ${list } 화면에 찍어줄때--%> 
<c:forEach items="${list }" var="dto">	<!-- $표시나 } 뒤에는 띄어쓰기하면 오류남. -->
<!-- 반복문의 시작 -->
<tr class="dataRow"> <!-- 나중에는 for문으로 처리한다. -->
	<td class="no">${dto.no }</td>
	<td>${dto.title }</td>
	<td>${dto.writer }</td>
	<td>${dto.writeDate }</td>
	<td>${dto.hit }</td>
</tr>
<!-- 반복문의 끝 -->
</c:forEach>
<tr>
	<td colspan="5"> <!-- 5개를 합쳐서 하나의 칸에 버튼으로 적용 -->
	<a href="writeForm.jsp" class="btn btn-default" >글쓰기</a>
	</td>
</tr>
</table>
</div>
</body>
</html>













