#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	OLE
%define		pnam	Storage_Lite
Summary:	OLE::Storage_Lite Perl module - simple class for OLE document interface
Summary(pl.UTF-8):	Moduł Perla OLE::Storage_Lite - prosta klasa obsługująca interfejs dokumentów OLE
Name:		perl-OLE-Storage_Lite
Version:	0.19
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	1a713f5342c7d90e54ab0d9659650296
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-IO-stringy
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module allows you to read and write an OLE-Structured file.
The module will work on the majority of Windows, UNIX and Macintosh
platforms.

%description -l pl.UTF-8
Moduł ten umożliwia odczyt i zapis plików w standardzie OLE.
Jest niezależny od platformy systemowej i powinien działać na systemach
Windows, UNIX i Macintosh.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
install sample/{README,*.pl,*xls} $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/OLE/*.pm
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
