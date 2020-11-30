<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
 <%@page import="java.sql.*" %> 
<%

	//DB연결
	Class.forName("com.mysql.jdbc.Driver");
	String db = "jdbc:mysql://localhost:3306/pkc";
	String userid = "root";
	String pw = "1234";
	Connection conn = DriverManager.getConnection(db,userid,pw);
	
	//request값 가져오기
	String pwd = request.getParameter("pwd");
	String id = request.getParameter("id");

	// DB에 있는 비밀번호 가지고 오기
	//쿼리생성.
		String sql="select pwd from board where id="+id;
	//심부름꾼.
		Statement stmt = conn.createStatement();
	//실행후 ResultSet;
		ResultSet rs = stmt.executeQuery(sql);
		rs.next();
	//유효성 검사
	if( pwd.equals( rs.getString("pwd")) ){
	sql = "delete from board where id="+id;
	stmt = conn.createStatement();
	stmt.executeUpdate(sql);
	response.sendRedirect("list.jsp");
	}else{
		response.sendRedirect("content.jsp?id="+id+"&chk=1"); 
		//변수 달아서 비밀번호 틀렸을때 나타내주기
	}
%>












