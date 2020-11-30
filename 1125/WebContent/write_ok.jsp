<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@page import="java.sql.*" %>

<%
	//DB 연결(MariaDB) db정보,아이디,비밀번호
	Class.forName("com.mysql.jdbc.Driver");
	String db = "jdbc:mysql://localhost:3306/pkc";
	String userid = "root";
	String pw = "1234";
	Connection conn = DriverManager.getConnection(db,userid,pw);
	
	// 한글처리(request 값)
	request.setCharacterEncoding("utf-8");	//한글처리는 가장 위에 처리.
	String name = request.getParameter("name");	//write.jsp 에서 넘어오는 name 받기
	String age = request.getParameter("age");	//write.jsp 에서 넘어오는 age 받기
	String juso = request.getParameter("juso");	//write.jsp 에서 넘어오는 juso 받기
	
	Statement stmt = conn.createStatement();
// 	String sql = "create table imsi(id int)"; 테이블 만들기
// 	입력받아 데이터 삽입
	String sql = "insert into member (name,age,juso) values('"+name+"',"+age+",'"+juso+"')";
	stmt.executeUpdate(sql);
	//list로 이동
	response.sendRedirect("list.jsp");
	
%>


















    
    
    
