<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
<script type="text/javascript">

	function update() {	//폼태그의 성격을 수정으로 바꾼다.
		//폼태그의 action 값을 => dat_update_ok.jsp로 변경
		document.getElementById("pkc").action="dat_update_ok.jsp";
		document.getElementById("submit").value="댓글수정";
		// 댓글 달기 버튼의 text를 '댓글 수정'으로 변경
		
	}
	function del() {	//폼태그의 성격을 삭제로 바꾼다.
		document.getElementById("pkc").action="dat_delete.jsp";
		document.getElementById("submit").value="댓글삭제";
	}

</script>
</head>
<body>
<form id="pkc" name = "dat" method="post" action="dat_write_ok2.jsp">
		<input type="hidden" name="id"><!-- 댓글테이블의 id값 -->
		<input type="text" name = "name" size="5" placeholder="작성자">
		<input type="text" name = "content" size="50" placeholder="댓글 내용">
		<input type="text" name = "pwd" size="5" placeholder="비밀번호">
		<input id="submit" type="submit" value="댓글달기">
	</form>
	<table width="600">
	<tr>
		<td width="100"><a href="javascript:update()"> 이름 </a></td>
		<td> 내용 </td>
		<td> <a href="javascript:del()"> 작성일 </a> </td>
	</tr>
	</table>
</body>
</html>