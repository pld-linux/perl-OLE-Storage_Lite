#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	OLE
%define		pnam	Storage_Lite
Summary:	OLE::Storage_Lite Perl module - simple class for OLE document interface
Summary(pl):	Modu� Perla OLE::Storage_Lite - prosta klasa obs�uguj�ca interfejs dokument�w OLE
Name:		perl-OLE-Storage_Lite
Version:	0.14
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	376118e3061bf4370b1a286dd7a0bb07
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-IO-stringy
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module allows you to read and write an OLE-Structured file.
The module will work on the majority of Windows, UNIX and Macintosh
platforms.

%description -l pl
Modu� ten umo�liwia odczyt i zapis plik�w w standardzie OLE.
Jest niezale�ny od platformy systemowej i powinien dzia�a� na systemach
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
