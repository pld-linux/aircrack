Summary:	Tool that cracks 802.11 WEP encryption keys
Summary(pl):	Program do �amania szyfrowania WEP dla protoko�u 802.11
Name:		aircrack
Version:	2.1
Release:	2
License:	GPL
Group:		Networking
Source0:	http://www.cr0.net:8040/code/network/%{name}-%{version}.tgz
# Source0-md5:	694c6180f620b0534e5925a71b960bd1
Patch0:		%{name}-aireplay.patch
URL:		http://www.cr0.net:8040/code/network/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Aircrack is a 802.11 WEP key cracker. It implements the so-called
Fluhrer - Mantin - Shamir (FMS) attack, When enough encrypted packets
have been gathered, aircrack can almost instantly recover the WEP key.

%description -l pl
Aircrack to program do �amania szyfrowania WEP dla protoko�u 802.11
u�ywaj�cy ataku typu FMS (Fluhrer - Mantin - Shamir). Po zgromadzeniu
wystarczaj�cej liczby zaszyfrowanych pakiet�w aircrack mo�e prawie
natychmiast odtworzy� klucz WEP.

%prep
%setup -q
%patch0	-p1

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	prefix=/usr \
        DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README docs/* patch
%attr(755,root,root) %{_bindir}/*
