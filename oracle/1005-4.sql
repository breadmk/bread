--�۽������̺��� �̸�,�޿�,�Ի���, �ٹ��Ⱓ,�޿������� ���Ͽ� personnel_r���̺� ����
declare
cursor c2 is select pname,pay,startdate from personnel;
cpname personnel.pname%type;
cpay personnel.pay%type;
cstartdate personnel.startdate%type;
cgigan personnel_r.gigan%type;
crank personnel_r.rank%type;
begin
delete from personnel_r;
open c2;
loop
	fetch c2 into cpname,cpay,cstartdate;
--		if c2%notfound then
--			exit;
--		end if;		
		exit when(c2%notfound);
		cgigan:=floor(months_between(sysdate,cstartdate)/12)||'��'||
			floor(mod(months_between(sysdate,cstartdate),12))||'����';
		select count(*) into crank from personnel where pay>cpay;
		crank := crank+1;
		insert into personnel_r 
			values (cpname,cpay,cstartdate,cgigan,crank);
end loop;
close c2;
commit;
end;
/




