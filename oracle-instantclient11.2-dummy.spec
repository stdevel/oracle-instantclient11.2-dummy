Summary: Dummy package for dumb oracle-instantclient package
Name: oracle-instantclient11.2-dummy
Version: 1.0
Release: 1%{?dist}
License:  GPL
Group: Development/Libraries
Source0: foo.bar
Url: http://www.stankowic-development.net
Requires: oracle-instantclient11.2-basic
Provides: libocci.so.11.1()(64bit) libclntsh.so.11.1()(64bit)

%description
Dummy package for dumb oracle-instantclient package missing provides tags.
This package requires the Oracle Instantclient basic package to provide libocci and libclntsh.

%setup

%build

%clean

%install

%files

%changelog
* Tue Jul 22 2015 Christian Stankowic <info@stankowic-development.net> 1.0-1
- initial release
