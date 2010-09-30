%global _binary_filedigest_algorithm 1
%global _source_filedigest_algorithm 1
%global _binary_payload w9.gzdio
%global _source_payload w9.gzdio

Name: candlepin-deps
Summary: Build dependencies for Candlepin
Group: Internet/Applications
License: Various
Version: 0.0.1
Release: 1
URL: http://fedorahosted.org/candlepin
Source: %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Vendor: Red Hat, Inc
BuildArch: noarch

%description
Candlepin is an open source entitlement management system.

%prep
%setup -q 

%build
buildr clean test=no package

%install
rm -rf $RPM_BUILD_ROOT
# Create the directory structure required to lay down our files
# common
install -d -m 755 $RPM_BUILD_ROOT/%{_sysconfdir}/candlepin/lib/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_sysconfdir}/candlepin/lib/

%changelog
