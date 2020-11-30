<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@page import="java.sql.*" %>
<% 

	//db연결
	Class.forName("com.mysql.jdbc.Driver");
	String db = "jdbc:mysql://localhost:3306/pkc";
	String userid = "root";
	String pw = "1234";
	Connection conn = DriverManager.getConnection(db,userid,pw);
    
	String id = request.getParameter("id");
    //쿼리 생성
    String sql = "select * from gesipan order by id desc";
    //심부름꾼생성
    Statement stmt = conn.createStatement();
    //쿼리실행 => ResultSet 
    ResultSet rs = stmt.executeQuery(sql);
    
    %>
    
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
 <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>
<body>
<!-- 레코드 내용 출력 -->
<table width="600" align="center" id="table">
	
	<tr>
		<td>이름</td>
		<td>제목</td>
		<td>성별</td>
		<td>작성일</td>
	</tr>
	
	<%
	while(rs.next()){
		// 숫자로 작성된 성별을 문자로 변환
		String sung = null;
		switch(rs.getInt("sung")){
			case 0: sung="남자"; break;
			case 1:	sung="여자"; break;
			case 2: sung="선택안함"; break;
		}
	%>
	<tr>
		<td><%=rs.getString("name") %></td>
		<td><a href="content.jsp?id=<%=rs.getInt("id")%>"><%=rs.getString("title") %></a></td>
		<td><%=sung%></td>
		<td><%=rs.getString("writeday") %></td>
	</tr>
	<%
	}
	%>
	<tr>
		<td colspan="2"><a href="write.jsp">글 쓰기</a></td>
	</tr>

</table>

</body>
</html>

















