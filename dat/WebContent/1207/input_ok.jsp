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
   
	//request 값 가져오기
	request.setCharacterEncoding("UTF-8");
	String name = request.getParameter("name");
	String kor = request.getParameter("kor");
	String eng = request.getParameter("eng");
	String math = request.getParameter("math");
	String scie = request.getParameter("scie");
	//쿼리생성
	String sql = "insert into sung (name,kor,eng,math,scie,writeday)";
	sql = sql + " values(?,?,?,?,?,now())";
	//심부름꾼
	PreparedStatement pstmt = conn.prepareStatement(sql);
	pstmt.setString(1, name);
	pstmt.setString(2, kor);
	pstmt.setString(3, eng);
	pstmt.setString(4, math);
	pstmt.setString(5, scie);
	//쿼리실행
	pstmt.executeUpdate();
	//이동
	response.sendRedirect("sung_view.jsp");
   	pstmt.close();
   	conn.close();
   %>