set verify off
set serveroutput on
accept no1 prompt '����1='
accept no2 prompt '����2='
declare
hap number :=0;
begin
hap := &no1+&no2;
dbms_output.put_line(hap);
end;
/