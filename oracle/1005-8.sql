set verify off
set serveroutput on
accept no prompt '�����ȣ='
declare
ppname personnel.pname%type;
ppay personnel.pay%type;
begin
select pname,pay into ppname,ppay from personnel where pno=&no;
dbms_output.put_line(ppname||' '||ppay);
exception
	when no_data_found then
		dbms_output.put_line('�ش� ����� �����ϴ�.');
	when too_many_rows then
		dbms_output.put_line('����� �θ� �̻� �Դϴ�.');
	when others then
		dbms_output.put_line('�����ڿ��� �����ϼ���.');	
		
end;
/






