%define name	mutagen
%define version	1.11
%define release %mkrel 1

Name: 	 	%{name}
Summary: 	Audio tag tools
Version: 	%{version}
Release: 	%{release}

Source:		http://www.sacredchao.net/~piman/software/%{name}-%{version}.tar.bz2
URL:		http://www.sacredchao.net/quodlibet/wiki/Development/Mutagen
License:	GPL
Group:		Sound
BuildRequires:	python-devel
BuildArch:	noarch

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

%install
rm -rf $RPM_BUILD_ROOT
python setup.py install --root=%buildroot

%find_lang %name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(-,root,root)
%doc NEWS README TODO
%python_sitelib/%name
%python_sitelib/%name-%{version}-py2.5.egg-info
%{_bindir}/*
%{_mandir}/man1/*


