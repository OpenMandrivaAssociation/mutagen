Summary:	Audio tag tools
Name:		mutagen
Version:	1.20
Release:	6
License:	GPLv2+
Group:		Sound
URL:		http://code.google.com/p/mutagen/
Source0:	http://mutagen.googlecode.com/files/%{name}-%{version}.tar.gz
%py_requires -d
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Mutagen is an audio metadata tag reader and writer implemented in pure Python.
It supports reading ID3v1.1, ID3v2.2, ID3v2.3, ID3v2.4, APEv2, and FLAC, and
writing ID3v1.1, ID3v2.4, APEv2, and FLAC.

The goals are (in rough order of importance):
    * Read as many files as possible
    * Compatibility with as many other tag readers and editors as possible
    * Compliance with the relevant specifications
    * Written in Pythonic Python, with a Pythonic API
    * Unit and regression test suite
    * Provide access to all features of the supported formats
    * Easily extensible 

%prep
%setup -q

%build
%{__python} setup.py build

# (tpg) checks fails on x86_64
#%check
#%{__python} setup.py test

%install
%{__python} setup.py install -O2 --skip-build --root %{buildroot}

%files
%defattr(-,root,root)
%doc NEWS README TODO
%{python_sitelib}/%{name}
%{python_sitelib}/%{name}-%{version}-*egg-info
%{_bindir}/*
%{_mandir}/man1/*


%changelog
* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 1.20-3mdv2011.0
+ Revision: 666503
- mass rebuild

* Fri Oct 29 2010 Michael Scherer <misc@mandriva.org> 1.20-2mdv2011.0
+ Revision: 590136
- rebuild for python 2.7

* Sat Aug 07 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 1.20-1mdv2011.0
+ Revision: 567382
- update to new version 1.20

* Sat Feb 20 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 1.19-1mdv2010.1
+ Revision: 508794
- update to new version 1.19

* Wed Nov 11 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 1.18-1mdv2010.1
+ Revision: 464881
- update to new version 1.18

* Sat Jun 20 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 1.16-1mdv2010.0
+ Revision: 387466
- update to new version 1.16
- correct URLs

* Thu Dec 25 2008 Funda Wang <fwang@mandriva.org> 1.15-1mdv2009.1
+ Revision: 319007
- new version 1.15

* Sun Aug 17 2008 Emmanuel Andry <eandry@mandriva.org> 1.14-1mdv2009.0
+ Revision: 273086
- New version

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 1.13-2mdv2009.0
+ Revision: 223331
- rebuild
- fix no-buildroot-tag

* Thu Dec 27 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 1.13-1mdv2008.1
+ Revision: 138231
- disable checks, as it fails on x86_64
- new version
- new license policy
- fix building
- add checks
- spec file clean

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sun May 06 2007 Austin Acton <austin@mandriva.org> 1.11-1mdv2008.0
+ Revision: 23676
- new version


* Sun Feb 18 2007 Jérôme Soyer <saispo@mandriva.org> 1.10.1-1mdv2007.0
+ Revision: 122280
- New release 1.10.1

* Sat Dec 09 2006 Eskild Hustvedt <eskild@mandriva.org> 1.6-2mdv2007.1
+ Revision: 94041
- Package the *.egg-info
- Rebuild for new python
- Import mutagen

* Mon Aug 14 2006 Austin Acton <austin@mandriva.org> 1.6-1mdv2007.0
- 1.6

* Tue Jun 27 2006 Austin Acton <austin@mandriva.org> 1.5-1mdv2007.0
- New release 1.5

* Tue Jun 20 2006 Austin Acton <austin@mandriva.org> 1.4-1mdv2007.0
- fix summary
- source URL
- 1.4

* Sun May 14 2006 Emmanuel Andry <eandry@mandriva.org> 1.2-1mdk
- 1.2

* Tue Apr 04 2006 Austin Acton <austin@mandriva.org> 1.0-1mdk
- initial package

