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
			<td colspan="2"><%=rs.getString("birth") %></td>
			<td>작성일</td>
			<td colspan="2"><%=rs.getString("writeday") %>
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
			<a href="update.jsp">수정</a>
			<a href="delete.jsp">삭제</a>
			</td>
		</tr>
	
	
	</table>









</body>
</html>


















