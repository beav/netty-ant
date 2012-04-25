%global _binary_filedigest_algorithm 1
%global _source_filedigest_algorithm 1
%global _binary_payload w9.gzdio
%global _source_payload w9.gzdio

Name: netty
Summary: netty lib
Group: Internet/Applications
License: Apache
Version: 3.3.1
Release: 2%{?dist}
URL: http://netty.io/
Source: %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch: noarch

BuildRequires: java >= 0:1.6.0
BuildRequires: ant >= 0:1.7.0
BuildRequires: tomcat6-servlet-2.5-api
BuildRequires: jakarta-commons-httpclient >= 3.1
BuildRequires: log4j
Requires: java >= 0:1.6.0
%define __jar_repack %{nil}

%description
netty

%prep
%setup -q

%build
ant -Dlibdir=/usr/share/java -Dversion=%{version} clean package

%install
rm -rf $RPM_BUILD_ROOT
# Create the directory structure required to lay down our files
# common
install -d -m 755 $RPM_BUILD_ROOT/usr/share/java/
ln -s /usr/share/java/netty-%{version}.jar $RPM_BUILD_ROOT/usr/share/java/netty.jar
install -m 644 dist/lib/netty-%{version}.jar $RPM_BUILD_ROOT/usr/share/java/

%clean
rm -rf $RPM_BUILD_ROOT

%files
/usr/share/java/netty-%{version}.jar
/usr/share/java/netty.jar


%changelog
* Mon Mar 19 2012 Chris Duryee (beav) <cduryee@redhat.com>
- new package built with tito

* Fri Mar 16 2012 Chris Duryee (beav) <cduryee@redhat.com>
- initial commit
