set verify off
accept no prompt '���='
declare
	pname sawon.saname%type;
	ppay sawon.sapay%type;
begin
	select saname,sapay into pname,ppay 
		from sawon where sabun=&no;
	dbms_output.put_line(pname||'�� �޿��� '||ppay);
end;
/


