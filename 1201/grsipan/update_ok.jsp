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
  //request 값 가져오기
  	request.setCharacterEncoding("utf-8");
  	String id = request.getParameter("id");
  	String name = request.getParameter("name");
  	String title = request.getParameter("title");
  	String pwd = request.getParameter("pwd");
  	String content = request.getParameter("content");
  	String sung = request.getParameter("sung");
  	String hobby = String.join(",", request.getParameterValues("hobby"));
  	String birth = request.getParameter("birth");
  	
  
  // db안에 있는 비밀번호 가지고 오기
  	String sql = "select pwd from gesipan where id="+id;
  //심부름꾼
	Statement stmt = conn.createStatement();
  //쿼리실행
	ResultSet rs = stmt.executeQuery(sql);
  	rs.next();
  	PreparedStatement pstmt =null;
  	
  // 입력한 비밀번호, db에 있는 비밀번호가 같으냐?
  	if(pwd.equals(rs.getString("pwd"))){
  		sql = "update gesipan set name=?,title=?,content=?,sung=?,hobby=?,birth=? ";
		sql = sql+" where id="+id;
		
	pstmt = conn.prepareStatement(sql);
	pstmt.setString(1, name);
	pstmt.setString(2, title);
	pstmt.setString(3, content);
	pstmt.setString(4, sung);
	pstmt.setString(5, hobby);
	pstmt.setString(6, birth);
	
	pstmt.executeUpdate();
  	
	response.sendRedirect("content.jsp?id="+id);
  	}else{
  		response.sendRedirect("update.jsp?id="+id+"&chk=1");
  	}
  
  	conn.close();
  	
  %>