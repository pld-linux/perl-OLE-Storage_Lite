#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	OLE
%define	pnam	Storage_Lite
Summary:	OLE::Storage_Lite Perl module - simple class for OLE document interface
Summary(pl):	Modu³ Perla OLE::Storage_Lite - prosta klasa obs³uguj±ca interfejs dokumentów OLE
Name:		perl-%{pdir}-%{pnam}
Version:	0.11
Release:	1.1
License:	GPL or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	78edc8f66074787b98af92df9bc5cc79
BuildRequires:	perl-devel >= 5.6.1
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-IO-stringy
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module allows you to read and write an OLE-Structured file.
The module will work on the majority of Windows, UNIX and Macintosh
platforms.

%description -l pl
Modu³ ten umo¿liwia odczyt i zapis plików w standardziee OLE.
Jest niezale¿ny od platformy systemowej i powinien dzia³aæ na systemach
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

%{__make} install DESTDIR=$RPM_BUILD_ROOT
install sample/{README,*.pl,*xls} $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/OLE/*.pm
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
