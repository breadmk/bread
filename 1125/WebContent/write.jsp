<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head> <!-- write.jsp -->
<meta charset="UTF-8">
<title>Insert title here</title>
<script src="https://code.jquery.com/jquery-3.5.1.min.js"></script>
<script type="text/javascript">

	function check(my){
		//form 태그 => form객체 접근, body에 있는 태그 id(단수),class(복수)
		if(my.name.value.length <3 || my.name.value.length > 5){
			alert("이름은3자이상 5자 이하입니다");
			return false;
			}else if(isNaN(my.age.value)||my.age.value.length==0){
				alert("나이는 숫자만 입력가능합니다");
				return false;
				}else if(my.juso.value.length<2){
					alert("주소는 2글자 이상입니다.");
					return false;
					}else{
						return true;
					}
	}



// $(function (){
	
// 	$('#frm').submit(function(){
		
//      var length = $('#name').val().length;
//      var jusolength = $('#juso').val().length;
     
    
//          if(length>5 | length<3){
//          alert('아이디는 3자이상 5자 이하 입니다.')
//          return false;
//          }
         
//       	if(!$.isNumeric($('#age').val())){
//       		alert("숫자만 넣으세요")
//       		return false;
//       	}
      		
//          if(jusolength<2){
//         	 alert('주소는 2글자 이상입니다.')
//         	 return false;
//          }
            
//  	  })
//     })



</script>
</head>
<body>
	<!--  이름은 3자이상 5자이하, 나이는 숫자인가, 주소는 2자 이상 되면 전송하기 -->
	<form method="post" id="frm" action="write_ok.jsp" name="member" onsubmit="return check(this)">
	이름<input type="text" name="name" id="name"> <p>
	나이<input type="text" name="age" id="age"> <p>
	주소<input type="text" name="juso" id="juso"> <p>
	   <input type="submit" value="저장">
	</form>
</body>
</html>