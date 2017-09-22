Summary: Network Performance Testing Tool for ARM64
Name: netperf
Version: 2.4.5
Release: 1
Group: System Environment/Base
License:BSD
URL: http://www.netperf.org/
Packager: Martin A. Brown
Source: ftp://ftp.netperf.org/netperf/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-root
Prefix: /usr

%description
Many different network benchmarking tools are collected in this package,
maintained by Rick Jones of HP.

%prep
%setup -q

%build
./configure \
  --build=aarch64-unknown-linux-gnu \
  --prefix=%{_prefix} \
  --mandir=%{_mandir} \
  --infodir=%{_infodir} 
make

%install
test "$RPM_BUILD_ROOT" = "/"    || rm -rf $RPM_BUILD_ROOT
make DESTDIR=${RPM_BUILD_ROOT} install

%clean
test "$RPM_BUILD_ROOT" = "/"    || rm -rf $RPM_BUILD_ROOT

# %post

%files
%defattr(-,root,root)
%doc README AUTHORS ChangeLog INSTALL COPYING
%doc README.* Release_Notes
%doc doc/examples
%{_mandir}/man1/*
%{_infodir}/*
%{_bindir}/netperf
%{_bindir}/netserver


%changelog
* Sat Jun 17 2006 Martin A. Brown <martin@linux-ip.net>
* initial contributed specfile for netperf package (v2.4.2)
- Sep 22 2017 yu.wang <wy200885@163.com> :make rpm package for ARM64
