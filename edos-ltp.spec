%define name edos-ltp
%define version 1.0.0
%define release %mkrel 6

Summary:	EDOS XML specification files for LTP tests
Name:		%{name}
Version:	%{version}
Release:	%{release}
URL:		https://www.edos-project.org
License:	GPL
Group:		Development/Other
Source0:	http://www.edos-project.org/releases/%{name}-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
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
* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0.0-6mdv2011.0
+ Revision: 618029
- the mass rebuild of 2010.0 packages

* Thu Sep 03 2009 Thierry Vignaud <tv@mandriva.org> 1.0.0-5mdv2010.0
+ Revision: 428529
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 1.0.0-4mdv2009.0
+ Revision: 244626
- rebuild

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 1.0.0-2mdv2008.1
+ Revision: 140728
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Jun 11 2007 François Déchelle <fdechelle@mandriva.org> 1.0.0-2mdv2008.0
+ Revision: 38044
- Fixed bug 31283 "fix software group in spec"

* Tue May 15 2007 François Déchelle <fdechelle@mandriva.org> 1.0.0-1mdv2008.0
+ Revision: 26959
- Adding package edos-ltp (LTP test suites xml specs)
- Create edos-ltp

