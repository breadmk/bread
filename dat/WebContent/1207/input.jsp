<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
<form method="post" action="input_ok.jsp">
	<table width="250" align="center" border="1">
		<tr>
		<td>이름</td>
			<td> <input type="text" name="name"> </td>
		</tr>
		  <tr>
       		 <td> 국어 </td>
       		 <td> <input type="text" name="kor"> </td>
     	 </tr>
		  <tr>
       		 <td> 영어 </td>
       		 <td> <input type="text" name="eng"> </td>
     	 </tr>
		  <tr>
       		 <td> 수학 </td>
       		 <td> <input type="text" name="math"> </td>
     	 </tr>
		  <tr>
       		 <td> 과학 </td>
       		 <td> <input type="text" name="scie"> </td>
     	 </tr>
     	  <tr>
        <td colspan="2" align="center">
         <button id="btn"> 입력하기 </button>
        </td>
      </tr>	
     	 
	
	</table>




</form>

</body>
</html>