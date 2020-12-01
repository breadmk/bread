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
    //req 가져오기
    String id = request.getParameter("id");
    //쿼리 생성
    String sql = "select * from gesipan where id="+id;
    //심부름꾼
    Statement stmt = conn.createStatement();
    //쿼리실행
    ResultSet rs = stmt.executeQuery(sql);
    // 하나의 레코드를 읽어와서 폼태그에 전달
	rs.next();
    
    
    %>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
<script type="text/javascript">
//성별,취미,태어난 해를 적용하여 처음 선택했던 값으로 표현되게 해야한다.
	function init(){
		//성별 (document.폼name.[input]name)
		document.pkc.sung[<%=rs.getInt("sung")%>].checked =true;
		//취미 : 0,2,3 <== split 사용  
		var hob = "<%=rs.getString("hobby")%>"; //var hob = "0,5";
		var hobby=hob.split(",");
		for(i=0; i<hobby.length; i++){
			document.pkc.hobby[hobby[i]].checked=true;
// 			document.pkc.hobby[0].checked=true;
// 			document.pkc.hobby[2].checked=true;
// 			document.pkc.hobby[3].checked=true;
		//태어난해
		document.pkc.birth.value=<%=rs.getString("birth")%>;
		}
	
	}

</script>
</head>
<body onload="init()">
	<form method="post" action="update_ok.jsp" name="pkc">
	<input type="hidden" name="id" value="<%=id%>">
	<table width="600" align="center">
		<tr>
			<td>제목</td>
			<td><input type="text" name="title" size=40" value="<%=rs.getString("title") %>"></td>
		</tr>
		<tr>
			<td>이름</td>
			<td><input type="text" name="name" value="<%=rs.getString("name") %>"></td>
		</tr>
		<tr>
			<td>비밀번호</td>
			<td><input type="password" name="pwd"></td>
		</tr>
		
		<tr>
			<td>내용</td>
			<td><textarea cols="40" rows="5" name="content"><%=rs.getString("content")%></textarea></td>
		</tr>
		<tr>
			<td>성별</td>
			<td> <!-- 라디오는 3개가 존재하지만 requset.gerPameter("sung") 하면 value가 넘어옴 -->
				<input type="radio" name="sung" value="0">남자
				<input type="radio" name="sung" value="1">여자
				<input type="radio" name="sung" value="2">선택안함
			</td>
		</tr>
		<tr>
			<td>취미</td>
			<td>
		<!-- requset.getParameter("hobby") 하면 하나만 넘어옴 -->
				<input type="checkbox" name="hobby" value="0">낚시
				<input type="checkbox" name="hobby" value="1">독서
				<input type="checkbox" name="hobby" value="2">여행
				<input type="checkbox" name="hobby" value="3">음주
				<input type="checkbox" name="hobby" value="4">잠자기
				<input type="checkbox" name="hobby" value="5">게임
			</td>
		</tr>
		<tr>
			<td>출생년도</td>
			<td>
			<!-- requset.getParameter("birth") 하면 value 넘어옴 -->
				<select name="birth">
				<% for (int i=2020; i>=1900; i--){
					
				
				%>
				<option value="<%=i%>"><%=i %></option>
				<%
				}
				%>
<!-- 					<option value="2020">2020</option> -->
<!-- 					<option value="2019">2019</option> -->
<!-- 					<option value="2018">2018</option> -->
<!-- 					<option value="2017">2017</option> -->
<!-- 					<option value="2016">2016</option> -->
				</select>		
			</td>
		</tr>
		 <%
        if(request.getParameter("chk") != null)
        {
      %>
      <tr>
        <td colspan="6" align="center"> 비번이 틀렸네요 </td>
      </tr>
     <%
        }
     %>
		<tr>
		<td colspan="2" align="center">
			<input type="submit" value="수정하기">
		</td>
		</tr>
		</tr>
      
	
	</table>
	</form>
</body>
</html>

<% stmt.close();
	conn.close();
	%>
