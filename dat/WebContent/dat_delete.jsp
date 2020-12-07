<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
 <%@page import="java.sql.*" %>
<!-- gesipan에 있던 delete.jsp => dat_delete.jsp로 변경 -->
<% 

   //db연결
   Class.forName("com.mysql.jdbc.Driver");
   String db = "jdbc:mysql://localhost:3306/pkc";
   String userid = "root";
   String pw = "1234";
   Connection conn = DriverManager.getConnection(db,userid,pw);
   //requet
   String id = request.getParameter("id"); 	//dat 테이블의 id
   String pwd = request.getParameter("pwd"); //사용자가 입력한 비밀번호
   
   //쿼리생성
   String sql = "select pwd,gid from dat where id="+id;
   //심부름꾼
   Statement stmt = conn.createStatement();
   ResultSet rs = stmt.executeQuery(sql);   
   rs.next();
   //쿼리 실행
   if(pwd.equals(rs.getString("pwd"))){
      sql="delete from dat where id="+id;
      stmt = conn.createStatement();
      stmt.executeUpdate(sql);
   }
      response.sendRedirect("content.jsp?id="+rs.getString("gid"));
      //gesipan 테이블의 아이디값을 넘겨줘야 content가 그대로 유지됨. 
      // 그냥 id는 dat테이블의 id임.
   conn.close();
   %>