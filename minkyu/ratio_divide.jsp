<%@page import="www.html.nav.Nav"%>
<%@page import="www.html.header.Header"%>
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
			
	//페이징 처리 변수 생성
	int index;
	int pager;
	if(request.getParameter("pager")==null){
		pager=1;
	}else{
		pager=Integer.parseInt(request.getParameter("pager"));
	}
	
	index = (pager-1)*10;
	
	//쿼리 생성
	String sql = "select * from stock1 order by suik desc limit "+index+",20";
	//심부름꾼 생성
	Statement stmt = conn.createStatement();
	//쿼리 실행
	ResultSet rs = stmt.executeQuery(sql);
	
%>
<%

Header header = new Header();
String css = header.getCss();
String js = header.getJs();

Nav nav = new Nav();
String menu = nav.getMenu();

request.setAttribute("importCss", css);
request.setAttribute("importJs", js);
request.setAttribute("menuHtml", menu);
%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
<title>Doogle</title>
${importCss}
${importJs}
<style type="text/css">

	h2{ text-align: center;}
	#first li{
		list-style-type: none;
		display: inline-block;
		margin-left: 30px;
		padding-left:15px;
		padding-top: 10px;
		text-align: center;
		}
/* --------------------------------------------- */
	#second{
	
		width:100%;
		height:600px;
	}
	#table{
		padding-left: 20px;
		border: 1px solid blue;
		margin: auto;
	}
	#table #tr1 td{
		padding: 20px;
		border: 1px solid blue;
		
		}
		
	#table #tr2 td{
	text-align: center;
	border: 1px solid blue;
		
		}
</style>
<script type="text/javascript">
$(function() {

});
</script>
</head>
<body>
	<div id="wrap">
		<header class="minkyu">
			<h2 id="logo"><a href="/">Doogle</a></h2>
		</header>
		<nav class="minkyu">
			${menuHtml}
		</nav>
		<div class="container">
			<main>
				<h2>주린이도 쉽게 할 수 있는 배당투자</h2>
				<div id="first">
					<ul>
						<li><a href="stock_fund.jsp">주식과 펀드의 차이점</a></li>
						<li><a href="basic_divide.jsp">배당주와 기본용어</a></li>
						<li><a href="good_divide.jsp">어떤 배당주가 좋은 배당주일까?</a></li>
						<li><a href="ratio_divide.jsp">상위 배당수익률</a></li>
						<li><a href="finance_state.jsp">재무제표보는법</a></li>
					</ul>
				</div>
			<div id="second">
			<table id="table">
				<tr id="tr1">
					<td>종목명</td>
					<td>현재가(월)</td>
					<td>기준월(년.월)</td>
					<td>배당금(원)</td>
					<td>수익률(%)</td>
					<td>배당성향(%)</td>
				</tr>
				<% while(rs.next()){
				
				%>
				
				<tr id="tr2">
					<td><%=rs.getString("title") %></td>
					<td><%=rs.getString("siga") %></td>
					<td><%=rs.getString("gijun") %></td>
					<td><%=rs.getString("beadang") %></td>
					<td><%=rs.getString("suik")%></td>
					<td><%=rs.getString("beadang1") %></td>
				</tr>
				
				<%
				}
				%>
				<tr>
					<td colspan="6" align="center">
					<%
					sql = "select count(*) as cnt from stock1";
					rs = stmt.executeQuery(sql);
					rs.next();
					int page_cnt = rs.getInt("cnt")/10+1;
					if(rs.getInt("cnt")%10==0)
						page_cnt--;
					
					int pstart;
					pstart = pager/10;
					if(pager%10==0){
						pstart=pstart-1;}
					pstart=Integer.parseInt(pstart+"1");
					
					int pend=pstart+9; //251 +9 =>260 총 페이지 : 255
							
					if(page_cnt <pend){
						pend = page_cnt;
					}
					%>
					
					<%
					if(pstart != 1){
						
					%>
					<a href = "ratio_divide.jsp?pager=<%=pstart-1 %>">◀◀</a>
					<%}else{ %>
					
					◀◀
					<%} %>
					
					<% if(pager != 1){   //if(현재페이지가 1페이지 아니면){
		
					%>
					<a href="ratio_divide.jsp?pager=<%=pager-1 %>">◀</a>
					<%
					}else{
					%>
					◀
					<%
					}
					for (int i=pstart; i<=pend; i++){
						String str = "";
						if(pager==i){
							str="style='color:red'";
						}
					
					%>
						<a href="ratio_divide.jsp?pager=<%=i %>" <%=str%>><%=i %></a>
					<% 
					}
					%>
					
					<%
				  if(pager != page_cnt){//if(현재페이지가 마지막페이지가 아니면 )
		
					%>
						<a href="ratio_divide.jsp?pager=<%=pager-1 %>">▶</a>
					<%}else{
					
					%>
					▶
					<%
					}
					%>
					
					<%
						if(page_cnt != pend){
					%>
					<a href="ratio_divide.jsp?pager=<%=pend+1%>">▶▶</a>	
					<%
						}else{
					%>
					▶▶
					<%
					}
					%>
					</td>
				</tr>
				
			
			</table>
			
			
			</div>		
		
				
				
			</main>
		</div>
		<footer class="minkyu">
			<p id="copyright">Copyright 2020 1team.</p>
		</footer>
	</div>
</body>
</html>

















