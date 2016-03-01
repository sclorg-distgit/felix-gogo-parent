%global project   felix-gogo
%global pkgname   parent

%{!?scl:%global pkg_name %{name}}
%{?scl:%scl_package %{project}-%{pkgname}}

Name:             %{?scl_prefix}%{project}-%{pkgname}
Version:          0.6.0
Release:          5%{?dist}
Summary:          Parent package for Felix Gogo
Group:            Development/Tools
License:          ASL 2.0
URL:              http://felix.apache.org/site/apache-felix-gogo.html

Source0:          http://apache.mirror.rbftpnetworks.com//felix/gogo-parent-0.6.0-project.tar.gz

ExclusiveArch: %{ix86} x86_64

BuildRequires:    java
BuildRequires:    maven
BuildRequires:    jpackage-utils

Requires:         java 
BuildRequires:    maven
Requires:         jpackage-utils
%{?scl:Requires: %scl_runtime}

%description
Apache Felix is a community effort to implement the OSGi R4 Service Platform
and other interesting OSGi-related technologies under the Apache license. The
OSGi specifications originally targeted embedded devices and home services
gateways, but they are ideally suited for any project interested in the
principles of modularity, component-orientation, and/or service-orientation.
OSGi technology combines aspects of these aforementioned principles to define a
dynamic service deployment framework that is amenable to remote management.

%prep
%setup -q -n gogo-parent-%{version}

%build
mvn-rpmbuild install

%install
# pom
install -d -m 755 %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{pkg_name}.pom
%add_maven_depmap JPP-%{pkg_name}.pom 


%files
%doc LICENSE NOTICE
%{_mavenpomdir}/JPP-%{pkg_name}.pom
%{_mavendepmapfragdir}/%{name}

%changelog
* Tue Nov 20 2012 Alexander Kurtakov <akurtako@redhat.com> 0.6.0-5
- Make it exclusive arch due to no OpenJDK 1.7 on non x86.

* Tue Nov 13 2012 Krzysztof Daniel <kdaniel@redhat.com> 0.6.0-4
- Removed the hardcoded scl macro enablement.

* Fri Nov 9 2012 Krzysztof Daniel <kdaniel@redhat.com> 0.6.0-3
- Added scl_runtime dependency.

* Thu Nov 8 2012 Krzysztof Daniel <kdaniel@redhat.com> 0.6.0-2
- Correct the name of pom.

* Thu Nov 8 2012 Krzysztof Daniel <kdaniel@redhat.com> 0.6.0-1
- Initial contribution to SCL.
