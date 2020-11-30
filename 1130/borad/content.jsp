<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@page import="java.sql.*" %>    
<%
    // DB 연결
    Class.forName("com.mysql.jdbc.Driver");
    String db="jdbc:mysql://localhost:3306/pkc";
    String userid="root";
    String pw="1234";
    Connection conn=DriverManager.getConnection(db,userid,pw); // db정보,아이디,비번
   
    // request값 읽어오기
    String id=request.getParameter("id");
    
// 조회수 증가 (readnum.jsp) 에서 처리함.
//     String sql = "update board set readnum=readnum+1 where id="+id;
//     Statement stmt=conn.createStatement();
//     stmt.executeUpdate(sql);
    // 쿼리 생성
    String sql="select * from board where id="+id;
    
    // 심부름꾼생성
    Statement stmt =conn.createStatement();

    // 쿼리 실행 => ResultSet 이동
    ResultSet rs=stmt.executeQuery(sql);
    rs.next();
%>    
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
<style>
  td {
    border:1px solid #cccccc;
  }
  #del{ 
  	visibility: hidden;
  	position: absolute; /* 독립된 공간으로 띄우기 웹페이지가 고정된 상태에서 움직이는거 */
  }
</style>

<script type="text/javascript">

	function view_del(){
// 		alert(event.clientX+" "+event.clientY); //  좌표알아오기
		var x = event.clientX; //top
		var y = event.clientY; //left
		document.getElementById("del").style.visibility="visible";
		document.getElementById("del").style.left=(x-30)+"px";//좌표주기
		document.getElementById("del").style.top=(y+30)+"px";//좌표주기
	}
// 	function preventLord(){  //readnum.jsp 가 있어서 새로고침 안 막아도됌.
// 		if( (event.ctrlKey == true && (event.keyCode == 78 || event.keyCode == 82)) || (event.keyCode == 116) ) {
// 	        event.keyCode = 0;
// 	        event.cancelBubble = true;
// 	        event.returnValue = false;
// 	    } 
// 	}
// 	document.onkeydown = preventLord;
</script>
</head>
<body>
    <!-- ResultSet의 내용을 출력  : name,title,content,readnum,writeday-->
    <table width="500" align="center">
      <tr align="center">
       <td> 작성자 </td>
       <td> <%=rs.getString("name")%> </td>
       <td> 조회수 </td>
       <td> <%=rs.getString("readnum")%> </td>
       <td> 작성일 </td>
       <td> <%=rs.getString("writeday")%> </td>
      </tr>
      <tr>
       <td align="center"> 제목 </td>
       <td colspan="5"> <%=rs.getString("title")%> </td>
      </tr>
      <tr height="200">
       <td align="center"> 내용 </td>
       <td colspan="5"> <%=rs.getString("content")%> </td>
      </tr>
      <tr>
      	<td colspan="6" align="center">
      		<a href = "update.jsp?id=<%=id%>">수정</a>
      		<a href = "#" onclick="view_del()">삭제</a>
      		<a href ="list.jsp">목록</a>
      	</td>
      	</tr>
      	
      	<% if( request.getParameter("chk") != null){ //올때는 1을 가지고옴 
      	
      	%>
      	
      	<tr>
      		<td colspan="6" align="center"> 비밀번호가 틀렸습니다 </td>
      	</tr>
      	<%
      	}
      	%>
      	
    </table>
    
    <form method="post" action="delete.jsp" id="del">
    		<input type="hidden" name="id" value="<%= id%>">
    	비밀번호<input type="password" name = "pwd" size="4">
			<input type="submit" value="삭제">   
    </form>
</body>
</html>

<% stmt.close();
	conn.close();
	%>









