<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
<style type="text/css">
	.alcol{
		border: 1px solid #dddddd;
		width: 200px;
		height: 30px;
		text-align: center;
		}
	.sulzip {
		list-style-type: none;
		padding-left: 40px;
		display: none;
		}
	.sulzip li{
	 list-style-type:none;
     margin-top:10px;
     width:120px;
     height:30px;
     padding-top:5px;
     background:#dddddd;
     color:black;
     text-align: center;
     
	}
	
	#first {
      width:800px;
      height:50px;
      margin:auto;
   }
   
    #first #aa > li{
     list-style-type:none;
     display:inline-block;  
     border:1px solid #dddddd;
     width:120px;
     height:35px;
     text-align:center;
     padding-top:8px;
     margin-left:20px;
     position:relative;
   }
   #first .sub {  
     position:absolute;
     padding-left:0px;
     width:120px;
     height:120px;
     top:40px;
     visibility:hidden; 
   }
   #first .sub li {
     list-style-type:none;
     margin-top:10px;
     width:120px;
     height:30px;
     padding-top:5px;
     border:1px solid #dddddd;
     background:#dddddd;
     color:black;
   }

</style>

<script type="text/javascript">

	function sulzip_view(n){
		
		for(i=0; i<document.getElementsByClassName("sulzip").length; i++)
		document.getElementsByClassName("sulzip")[i].style.display="none"
		document.getElementsByClassName("sulzip")[n].style.display="block";
		
	}

	 function sub_view(n){ 
        document.getElementsByClassName("sub")[n].style.visibility="visible";
     }
     function sub_hide(n){
    	document.getElementsByClassName("sub")[n].style.visibility="hidden";
     }
</script>
</head>
<body>
<h1>술집 고르기</h1>
	<div class="alcol" onclick="sulzip_view(0)">--1차--</div>
		<ul class="sulzip">
			<li>고깃집</li>
			<li>족발집</li>
			<li>국밥집</li>
			<li>전집</li>
		</ul>
	<div class="alcol" onclick="sulzip_view(1)">--2차--</div>
		<ul class="sulzip">
			<li>횟집</li>
			<li>이자카야</li>
			<li>꼬치집</li>
			<li>맥주집</li>
		</ul>	
	<div class="alcol" onclick="sulzip_view(2)">--3차--</div>
		<ul class="sulzip">
			<li>편의점</li>
			<li>친구네집</li>
			<li>우리집</li>
			<li>공원</li>
		</ul>	
	<div class="alcol" onclick="sulzip_view(3)">--4차--</div>
		<ul class="sulzip">
			<li>생존자</li>
			<li>대리기사</li>
			<li>버려진친구</li>
			<li>택시</li>
		</ul>	
	<div class="alcol" onclick="sulzip_view(4)">--해장--</div>
		<ul class="sulzip">
			<li>감자탕</li>
			<li>라면</li>
			<li>짬뽕</li>
			<li>파워에이드</li>
		</ul>	
	<hr>
	<h1 style="text-align: center;">크리스마스 준비</h1>
<div id="first">  
   <ul id="aa">
    <li onmouseenter="sub_view(0)" onmouseleave="sub_hide(0)"> 캐롤
       <ul class="sub">
         <li> I wish~ </li>
         <li> 종소리 </li>
         <li> 크리스마스 </li>
         <li> All i Want~ </li>
       </ul> 
    </li>
    <li onmouseenter="sub_view(1)" onmouseleave="sub_hide(1)"> 선물 
      <ul class="sub">
         <li> 주방류 </li>
         <li> 보석류 </li>
         <li> 옷 </li>
         <li> 가방 </li>
       </ul>
    </li>
    <li onmouseenter="sub_view(2)" onmouseleave="sub_hide(2)"> 장난감 
      <ul class="sub">
         <li> 트리 </li>
         <li> 산타인형 </li>
         <li> 오르골 </li>
         <li> 루돌프 </li>
       </ul>
    </li>
    <li onmouseenter="sub_view(3)" onmouseleave="sub_hide(3)"> 여행지 
      <ul class="sub">
         <li> 코로나 </li>
         <li> 사회적거리두기 </li>
         <li> 스페셜플레이스 </li>
         <li> 이시국에 </li>
       </ul>
    </li>
   </ul>
  </div>	
	


</body>
</html>