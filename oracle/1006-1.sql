set serveroutput on
set verify off
accept no prompt '���=>'
accept sal prompt '�޿�=>'
declare
vpno personnel.pno%type;
vpay personnel.pay%type;
vpname personnel.pname%type;
minpay exception;
begin
	if &sal<2000 then
		raise minpay;
	end if;
	select pno,pay,pname into vpno,vpay,vpname 
		from personnel where pno=&no;
	update personnel set pay=&sal where pno=&no;
	dbms_output.put_line(vpname||'�� �޿��� '||&sal||'�� ������');
	exception
		when no_data_found then
			dbms_output.put_line('�ش� �������');		
		when too_many_rows then
			dbms_output.put_line('����� �θ��̻�');	
		when minpay then
			dbms_output.put_line('�޿��� Ȯ���ϼ���');					
end;
/

