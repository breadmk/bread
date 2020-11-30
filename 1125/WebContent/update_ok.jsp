<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@page import="java.sql.*" %>

<%
	//DB 연결(MariaDB)
	Class.forName("com.mysql.jdbc.Driver");
	String db = "jdbc:mysql://localhost:3306/pkc";
	String userid = "root";
	String pw = "1234";
	Connection conn = DriverManager.getConnection(db,userid,pw);
	
	// update에 필요한 입력값들 가져오기
	request.setCharacterEncoding("utf-8");	//한글처리는 가장 위에 처리.
	String name = request.getParameter("name");	//update.jsp 에서 넘어오는 name 받기
	String age = request.getParameter("age");	//update.jsp 에서 넘어오는 age 받기
	String juso = request.getParameter("juso");	//update.jsp 에서 넘어오는 juso 받기
	String id = request.getParameter("id");//update.jsp 에서 넘어오는 id 받기
// 	String sql = "create table imsi(id int)"; 테이블 만들기
// 	쿼리생성
//     String sql="update member set name='"+name+"',age="+age+",juso='"+juso+"' where id="+id;
	String sql="update member set name='"+name+"',age="+age+",juso='"+juso+"' where id="+id;
// 	update member set name="홍길동",age=22,juso="부산" where id=1;
	//심부름꾼
	Statement stmt = conn.createStatement();
	//쿼리실행
	stmt.executeUpdate(sql);
	
	response.sendRedirect("list.jsp");
	
%>


















    
    
    
