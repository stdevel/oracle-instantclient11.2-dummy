# oracle-instantclient11.2-dummy
This repository offers a spec file for creating a RPM dummy package requiring the official Oracle Instantclient 11.2. It also pretends to provide **libocci** and **libclnth** required by many Oracle drivers like **perl-DBD-Oracle**. Unfortunately Oracle's official RPM does not have valid RPM **provides** tags resulting in dependency problems when installing software requiring the libraries mentioned above:
```
# yum install perl-DBD-Oracle
...
--> Finished Dependency Resolution
Error: Package: perl-DBD-Oracle-1.74-1.el6.x86_64
           Requires: libocci.so.11.1()(64bit)
Error: Package: perl-DBD-Oracle-1.74-1.el6.x86_64
           Requires: libclntsh.so.11.1()(64bit)
 You could try using --skip-broken to work around the problem
```

Using this workaround, it is possible to install the packages:
```
# yum localinstall perl-DBD-Oracle*.rpm oracle-instantclient*.rpm
...
Installed:
  oracle-instantclient11.2-basic.x86_64 0:11.2.0.4.0-1
  oracle-instantclient11.2-dummy.x86_64 0:1.0-1.el6
  perl-DBD-Oracle.x86_64 0:1.74-1.el6
```

See [my blog](http://st-devel.net/blodp) for further detail about this dilemma.
