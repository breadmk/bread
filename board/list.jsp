<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
       <%@page import="java.sql.*" %>
    
    <%
    
    //DB 연결
    Class.forName("com.mysql.jdbc.Driver");
	String db = "jdbc:mysql://localhost:3306/pkc";
	String userid = "root";
	String pw = "1234";
	Connection conn = DriverManager.getConnection(db,userid,pw);
    
    //request는 필요없음
    
    //쿼리 생성
    
    String sql = "select * from board order by id desc";
    //심부름꾼
	Statement stmt = conn.createStatement();
    //쿼리실행후 결과를 ResultSet 으로
    ResultSet rs = stmt.executeQuery(sql);
    
    %>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
<div class="container">
 <!-- 제목, 내용, 작성자, 비밀번호, 조회수 , 날짜 -->
    <table width="600" align="center" border = "1">
     <tr align="center">
       <td> 작성자 </td>
       <td> 제목 </td>
       <td> 조회수 </td>
       <td> 작성일 </td>
     </tr>
	
	<%
		while(rs.next()){
		
	%>
	<tr>
		<td align="center"><%= rs.getString("name") %></td>
		<td align="center"><%= rs.getString("title") %></td>
		<td align="center"><%= rs.getString("readnum") %></td>
		<td align="center"><%= rs.getString("writeday") %></td>
	</tr>
	<%
		}
	
	%>
	
	
	</table>
</div>
</body>
</html>























