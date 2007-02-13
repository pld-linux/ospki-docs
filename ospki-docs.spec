Summary:	Open-source PKI Book
Summary(pl.UTF-8):	Książka traktująca o PKI
Name:		OSPKI
Version:	2.4.7
Release:	1
License:	FDL
Group:		Documentation
Source0:	http://dl.sourceforge.net/ospkibook/%{name}-DOCS-%{version}.tar.gz
# Source0-md5:	92e7b2b29e1ff374a06889519dc36e4f
URL:		http://ospkibook.sourceforge.net/
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Document describes Public-Key Infrastructures, current PKI standards,
explains practical PKI functionality and gives an overview of
available open-source PKI implementations.

%description -l pl.UTF-8
Dokument ten opisuje Infrastrukturę Klucza Publicznego, obecne
standardy, wyjaśnia praktycznie funkcjonowanie PKI i daje pogląd na
implementacje PKI w środowisku open-source.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_docdir}/OSPKI
cp -a * $RPM_BUILD_ROOT%{_docdir}/OSPKI

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_docdir}/OSPKI
