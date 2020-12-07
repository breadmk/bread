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
	//쿼리생성
	String sql = "select * from sung order by id desc";
	//심부름꾼
	Statement stmt = conn.createStatement();
	//쿼리실행
	ResultSet rs = stmt.executeQuery(sql);
	%>
    
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
	<table width="500" align="center" border="1">
	
		<tr>
			<td>번호</td>
			<td>이름</td>
			<td>국어</td>
			<td>영어</td>
			<td>수학</td>
			<td>과학</td>
			<td>작성일</td>
		</tr>
		<%
			while(rs.next()){
				
			
		%>
		<tr>
			<td><%=rs.getString("id") %></td>
			<td><%=rs.getString("name") %></td>
			<td><%=rs.getString("kor") %></td>
			<td><%=rs.getString("eng") %></td>
			<td><%=rs.getString("math") %></td>
			<td><%=rs.getString("scie") %></td>
			<td><%=rs.getString("writeday") %></td>
		</tr>
		<%
			}
		
		%>
		<tr>
		<td colspan="7" align="center"><a href = "input.jsp">성적 작성</a></td>
	</tr>
	
	</table>

</body>
</html>

<% stmt.close();
	conn.close();
	%>
