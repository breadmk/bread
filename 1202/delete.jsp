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
   //requet
   String id = request.getParameter("id");
   String pwd = request.getParameter("pwd");
   
   //쿼리생성
   String sql = "select * from gesipan where id="+id;
   //심부름꾼
   Statement stmt = conn.createStatement();
   ResultSet rs = stmt.executeQuery(sql);   
   rs.next();
   //쿼리 실행
   if(pwd.equals(rs.getString("pwd"))){
      sql="delete from gesipan where id="+id;
      stmt = conn.createStatement();
      stmt.executeUpdate(sql);
      response.sendRedirect("list.jsp");
   }else{
      response.sendRedirect("content.jsp?id="+id+"&chk=1");
   }
   conn.close();
   %>