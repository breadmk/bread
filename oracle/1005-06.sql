--����� ���ʽ��� ����Ͽ� �̸�,�޿�,���ʽ��� ����Ͻÿ�
set serveroutput on
declare
	cursor c3 is select pname,pay from personnel;
	bo number:=0;
begin
for i in c3 loop
	case
		when i.pay<=1000 then
			bo:=i.pay*0.1;
		when i.pay>1000 and i.pay<2000 then
			bo:=i.pay*0.15;			
		when i.pay>2000 and i.pay<3000 then
			bo:=i.pay*0.2;				
		else
			bo:=i.pay*0.25;
	end case;
	dbms_output.put_line(i.pname||' '||i.pay||' '||bo);
end loop;
end;
/


