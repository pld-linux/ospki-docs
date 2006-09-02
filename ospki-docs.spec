Summary:	Open-source PKI Book
Summary(pl):	Ksi±¿ka traktuj±ca o PKI
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

%description -l pl
Dokument ten opisuje Infrastrukturê Klucza Publicznego, obecne
standardy, wyja¶nia praktycznie funkcjonowanie PKI i daje pogl±d na
implementacje PKI w ¶rodowisku open-source.

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
