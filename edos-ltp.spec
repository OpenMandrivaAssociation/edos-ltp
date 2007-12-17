%define name edos-ltp
%define version 1.0.0
%define release %mkrel 2

Summary:	EDOS XML specification files for LTP tests
Name:		%{name}
Version:	%{version}
Release:	%{release}
URL:		http://www.edos-project.org
License:	GPL
Group:		Development/Other
Source0:	http://www.edos-project.org/releases/%{name}-%{version}.tar.gz
Buildarch:      noarch
Requires:       ltp

%description
EDOS XML specification files for LTP tests

%prep
%setup -q -n %{name}-%{version}

%build
%configure
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%_datadir/edos/tests/LTP

%changelog
* Tue Oct 31 2006 Francois Dechelle <fdechelle@mandriva.com>
- initial package

