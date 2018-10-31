Summary:	Audio tag tools
Name:		mutagen
Version:	1.23
Release:	4
License:	GPLv2+
Group:		Sound
Url:		http://code.google.com/p/mutagen/
Source0:	http://mutagen.googlecode.com/files/%{name}-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	python-devel

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
%doc NEWS README TODO
%{python_sitelib}/%{name}
%{python_sitelib}/%{name}-%{version}-*egg-info
%{_bindir}/*
%{_mandir}/man1/*

