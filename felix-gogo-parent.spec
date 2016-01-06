%{?scl:%scl_package felix-gogo-parent}
%{!?scl:%global pkg_name %{name}}
%{?java_common_find_provides_and_requires}

Name:             %{?scl_prefix}felix-gogo-parent
Version:          0.6.0
Release:          13.2%{?dist}
Summary:          Parent package for Felix Gogo
License:          ASL 2.0
URL:              http://felix.apache.org/site/apache-felix-gogo.html

Source0:          http://apache.mirror.rbftpnetworks.com//felix/gogo-parent-0.6.0-project.tar.gz

BuildArch:        noarch

BuildRequires:  %{?scl_prefix_java_common}maven-local
BuildRequires:  %{?scl_prefix_java_common}mvn(junit:junit)
BuildRequires:  %{?scl_prefix_maven}mvn(org.apache.felix:felix-parent:pom:)
BuildRequires:  %{?scl_prefix_maven}mvn(org.apache.maven.plugins:maven-compiler-plugin)
BuildRequires:  %{?scl_prefix_java_common}mvn(org.easymock:easymock:3)
BuildRequires:  %{?scl_prefix}mvn(org.mockito:mockito-all)

%description
Apache Felix is a community effort to implement the OSGi R4 Service Platform
and other interesting OSGi-related technologies under the Apache license. The
OSGi specifications originally targeted embedded devices and home services
gateways, but they are ideally suited for any project interested in the
principles of modularity, component-orientation, and/or service-orientation.
OSGi technology combines aspects of these aforementioned principles to define a
dynamic service deployment framework that is amenable to remote management.

%prep
%{?scl:scl enable %{scl_maven} %{scl} - << "EOF"}
%setup -q -n gogo-parent-%{version}
%{?scl:EOF}


%build
%{?scl:scl enable %{scl_maven} %{scl} - << "EOF"}
%mvn_build
%{?scl:EOF}


%install
%{?scl:scl enable %{scl_maven} %{scl} - << "EOF"}
%mvn_install
%{?scl:EOF}


%files -f .mfiles
%doc LICENSE NOTICE
%dir %{_mavenpomdir}/felix-gogo-parent

%changelog
* Fri Jul 10 2015 Mat Booth <mat.booth@redhat.com> - 0.6.0-13.2
- Fix unowned directories

* Mon Jun 29 2015 Mat Booth <mat.booth@redhat.com> - 0.6.0-13.1
- Import latest from Fedora

* Mon Jun 29 2015 Mat Booth <mat.booth@redhat.com> - 0.6.0-13
- Remove forbidden SCL macros.

* Wed Jun 17 2015 Alexander Kurtakov <akurtako@redhat.com> 0.6.0-12
- Fix FTBFS.

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 28 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 0.6.0-9
- Rebuild to regenerate Maven auto-requires

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
