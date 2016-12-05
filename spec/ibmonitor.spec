Name:           ibmonitor
Version:        1.4
Release:        13%{?dist}

Summary:        Interactive bandwidth monitor

Group:          Applications/Internet
License:        GPLv2+
URL:            http://ibmonitor.sourceforge.net/
Source0:        http://dl.sf.net/ibmonitor/ibmonitor-1.4.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch

Requires:       perl(Term::ReadKey)

%description
The program ibmonitor is an interactive linux console application which shows
bandwidth consumed and total data transferred on all interfaces.


%prep
%setup -q -n ibmonitor


%build


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_bindir}
install -p -m 0755 ibmonitor $RPM_BUILD_ROOT%{_bindir}


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING ChangeLog README TODO
%{_bindir}/ibmonitor


%changelog
* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 1.4-9
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed May 21 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.4-2
- fix license tag

* Mon Oct 16 2006 Adrian Reber <adrian@lisas.de> - 1.4-1
- updated to 1.4

* Mon Sep 18 2006 Adrian Reber <adrian@lisas.de> - 1.3-4
- rebuilt

* Mon Feb 13 2006 Adrian Reber <adrian@lisas.de> - 1.3-3
- rebuilt

* Fri Apr  7 2005 Michael Schwendt <mschwendt[AT]users.sf.net>
- rebuilt

* Sat Feb 12 2005 Adrian Reber <adrian@lisas.de> - 0:1.3-1
- updated to 1.3

* Sat Jun 21 2003 Adrian Reber <adrian@lisas.de> - 0:1.2-0.fdr.1
- updated to 1.2

* Sat Jun 21 2003 Adrian Reber <adrian@lisas.de> - 0:1.0-0.fdr.3
- now using install instead of cp

* Sat Jun 21 2003 Adrian Reber <adrian@lisas.de> - 0:1.0-0.fdr.2
- preserve mode, ownership and timestamps during installation

* Sun Jun 08 2003 Adrian Reber <adrian@lisas.de> - 0:1.0-0.fdr.1
- Initial RPM release.
