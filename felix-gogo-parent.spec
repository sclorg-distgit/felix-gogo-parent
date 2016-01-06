%global project   felix-gogo
%global pkgname   parent

%{!?scl:%global pkg_name %{name}}
%{?scl:%scl_package %{project}-%{pkgname}}
%{?java_common_find_provides_and_requires}

Name:             %{?scl_prefix}%{project}-%{pkgname}
Version:          0.6.0
Release:          12%{?dist}
Summary:          Parent package for Felix Gogo
License:          ASL 2.0
URL:              http://felix.apache.org/site/apache-felix-gogo.html

Source0:          http://apache.mirror.rbftpnetworks.com//felix/gogo-parent-0.6.0-project.tar.gz

BuildArch:        noarch

BuildRequires:  %{?scl_prefix_java_common}maven-local
BuildRequires:  %{?scl_prefix_maven}felix-parent

Requires:  %{?scl_prefix_maven}felix-parent

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
scl enable %{scl_maven} %{scl} - <<EOF
%mvn_build
EOF

%install
scl enable %{scl_maven} %{scl} - <<EOF
%mvn_install
EOF

%files -f .mfiles
%doc LICENSE NOTICE
%dir %{_mavenpomdir}/felix-gogo-parent

%changelog
* Mon Jan 05 2015 Mat Booth <mat.booth@redhat.com> - 0.6.0-12
- Update for java common SCL usage

* Fri May 16 2014 Roland Grunberg <rgrunber@redhat.com> - 0.6.0-11
- Add manual R: to felix-parent.

* Fri May 16 2014 Mat Booth <mat.booth@redhat.com> - 0.6.0-10
- Use macros from scl-build package

* Tue May 13 2014 Alexander Kurtakov <akurtako@redhat.com> 0.6.0-9
- Initial DTS 3.0 import.

* Tue Aug 06 2013 Michal Srb <msrb@redhat.com> - 0.6.0-8
- Adapt to current guidelines

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Mar 15 2013 Krzysztof Daniel <kdaniel@redhat.com> 0.6.0-6
- Initial SCLization.

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 0.6.0-4
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Nov 07 2011 Tomas Radej <tradej@redhat.com> - 0.6.0-2
- Added install section to verify dependencies
- Added (build)requires to maven

* Wed Nov 02 2011 Tomas Radej <tradej@redhat.com> - 0.6.0-1
- Initial Packaging
