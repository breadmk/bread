<%@page import="com.sun.xml.internal.bind.v2.runtime.unmarshaller.XsiNilLoader.Array"%>
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
	
	//request 값
	request.setCharacterEncoding("utf-8");
	String name = request.getParameter("name");
	String title = request.getParameter("title");
	String pwd = request.getParameter("pwd");
	String content = request.getParameter("content");
	String sung = request.getParameter("sung");
// 	getParameterValues (return 값은 배열 [])
// 	String[] hobby = request.getParameterValues("hobby");
// 	String test = String.join(",",hobby);  2줄을 아래 한 줄로 변경.
	String hobby = String.join(",",request.getParameterValues("hobby")); 
// 	join함수는 배열을 특정구분자로 나눠서 주는것 (","컴마로 구분해서 줌) 1,2,3 
//  나중에 spilt 로 잘라서 값만 뽑아낼 수 있음.
	String birth = request.getParameter("birth");
// 	out.print(sung+" "+hobby+" "+ birth);
	
	//쿼리 생성
	String sql = "insert into gesipan (name,title,pwd,content,sung,hobby,birth,writeday) ";
			sql = sql+ " values(?,?,?,?,?,?,?,now())";
	
	//심부름꾼 생성
	PreparedStatement pstmt = conn.prepareStatement(sql);
	pstmt.setString(1, name);
	pstmt.setString(2, title);
	pstmt.setString(3, pwd);
	pstmt.setString(4, content);
	pstmt.setString(5, sung);
	pstmt.setString(6, hobby);
	pstmt.setString(7, birth);
	//쿼리 실행
	pstmt.executeUpdate();
	//이동
	response.sendRedirect("list.jsp");
	
	pstmt.close();
	conn.close();


%>