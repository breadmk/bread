<%@page import="www.html.nav.Nav"%>
<%@page import="www.html.header.Header"%>
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
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
		background: red;
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
			가나다라 마바사
			
			
			</div>		
		
				
				
			</main>
		</div>
		<footer class="minkyu">
			<p id="copyright">Copyright 2020 1team.</p>
		</footer>
	</div>
</body>
</html>

















