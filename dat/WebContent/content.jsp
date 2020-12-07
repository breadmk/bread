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
   
    //request 값 읽어오기
    String id = request.getParameter("id");
    //쿼리생성
	String sql = "select * from gesipan where id="+id;
    //심부름꾼생성
    Statement stmt = conn.createStatement();
    //쿼리실행
	ResultSet rs = stmt.executeQuery(sql);
    rs.next();
    %>
    
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
<style type="text/css">
   #del{ visibility: hidden;
         position: absolute;
   }
</style>

<script type="text/javascript">

function view_del(){
   var x=event.clientX;
   var y=event.clientY;
   document.getElementById("del").style.visibility="visible";
   document.getElementById("del").style.left=(x-30)+"px";//좌표주기
   document.getElementById("del").style.top=(y+30)+"px";//좌표주기
}
   
</script>

</head>
<body>
	<table width="600" align="center" border="1">
		<tr align="center">
<%
		// 성별
	String sung=null;
	if(rs.getInt("sung")==0){
		sung="남자";
	}else if(rs.getInt("sung")==1){
		sung="여자";
	}else{
		sung="선택안함";
	}
	// 취미 구하기 0:낚시, 1:독서, 2:여행, 3:음주, 4:잠자기, 5:게임
	// 1) , 로 구분된 필드의 값을 나눠야 된다. split()사용해서 , 빼고 배열에 담아줌
	String[] hobby = rs.getString("hobby").split(","); //리턴값 [] 2,3,4
		String hob="";
	for(int i=0; i<hobby.length; i++){
		switch(hobby[i]){
		case "0": hob=hob+" 낚시"; break;  //누적개념으로 붙여줘야함 
		case "1": hob=hob+" 독서"; break;
		case "2": hob=hob+" 여행"; break;
		case "3": hob=hob+" 음주"; break;
		case "4": hob=hob+" 잠자기"; break;
		case "5": hob=hob+" 게임"; break;
		}
	}


%>

			<td>이름</td>
			<td><%=rs.getString("name") %></td>
			<td>성별</td>
			<td><%=sung%></td>
			<td>취미</td>
			<td><%=hob%></td>
		</tr>
		<tr>
			<td>출생년도</td>
			<td><%=rs.getString("birth") %></td>
			<td>작성일</td>
			<td><%=rs.getString("writeday") %>
			<td>조회수</td>
			<td><%=rs.getString("readnum") %></td>
		</tr>	
			<tr>
				<td>제 목</td>
				<td colspan="5"><%=rs.getString("title") %></td>
			</tr>
		<tr>
			<td>내용</td>
			<td colspan="5"><%=rs.getString("content") %></td>
		</tr>
		<tr>
		<td colspan="6" align="center">
			<a href="list.jsp">목록</a>
			<a href="update.jsp?id=<%=rs.getInt("id")%>">수정</a>
			<a href="#" onclick="view_del()">삭제</a>
			</td>
		</tr>
		 <% 
         if(request.getParameter("chk")!=null){
            
         
      %>
         <tr>
         <td colspan="6" align="center">비밀번호가 틀렸습니다.</td>
         </tr>
      <%
         }
      %>
   
		
	
	
	</table>

   <form action="delete.jsp" method="post" id="del">
      <input type="hidden" name="id" value="<%=id %>">
      비밀번호<input type="password" name="pwd" size="4">
      <input type="submit" value="삭제">
   </form>
   <script type="text/javascript">
   
   function update() {
	//폼태그의 action="dat_update_ok.jsp", submit의 value를 '댓글수정'으로 변경
	 document.getElementById("pkc").action="dat_update_ok.jsp";
	 document.getElementById("submit").value="댓글 수정";
	 document.getElementById("name").style.visibility="visible";
	 document.getElementById("content").style.visibility="visible";
	}
   function del(id) {
	 //폼태그의 action="dat_update_ok.jsp", submit의 value를 '댓글삭제'으로 변경
	 document.getElementById("pkc").action = "dat_delete.jsp";
	 document.getElementById("submit").value = "댓글 삭제";
	 document.getElementById("name").style.visibility="hidden";
	 document.getElementById("content").style.visibility="hidden";
	 document.dat.id.value=id; //dat 테이블의 id 값을 전달.
	}
   
   </script>

	<!-- 댓글 관련 작업 -->
	<!-- 댓글을 입력 폼 => 작성자, 내용, 비밀번호 -->
	<div align="center">
	<form id="pkc" name = "dat" method="post" action="dat_write_ok.jsp">
		<input type="hidden" name="gid" value="<%=id%>"> <!-- gesipan 테이블의 id -->
		<input type="hidden" name="id"> <!--  dat테이블의 id -->
		<input id="name" type="text" name = "name" size="5" placeholder="작성자">
		<input id="content" type="text" name = "content" size="50" placeholder="댓글 내용" >
		<input type="text" name = "pwd" size="5" placeholder="비밀번호">
		<input id="submit" type="submit" value="댓글달기">
	</form>
</div>
<!-- 댓글 출력 -->
<%		//모두 다 재사용
	//db연결 => 위에 있음.
	
	//쿼리 생성
	sql = "select * from dat where gid="+id;
	//심부름꾼
	stmt = conn.createStatement();
	//쿼리실행후 => ResultSet
	rs = stmt.executeQuery(sql);
	
%>
 <div align="center">
 	<table align="center" width="600" border="1">
 	<!-- 레코드를 출력 -->
 	<%
 		while(rs.next())	//rs는 dat테이블
 		{	//하나의 tr에 하나의 레코드가 출력
 	%>
 		<tr>
 		
 			<td width="100"><a href="javascript:update()"><%=rs.getString("name")%></a> </td> <!-- 작성자-->
 			<td><%=rs.getString("content")%> </td> <!-- 내용 -->
 			<td width="100"><a href="javascript:del(<%=rs.getInt("id")%>)"><%=rs.getString("writeday")%></a></td> <!-- 작성일 -->
 		</tr>
 		<%
 		}
 		%>
 	</table>
 </div>

<%
	conn.close();
%>


</body>
</html>


















