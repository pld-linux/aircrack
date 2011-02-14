Summary:	Tool that cracks 802.11 WEP encryption keys
Summary(pl.UTF-8):	Program do łamania szyfrowania WEP dla protokołu 802.11
Name:		aircrack
Version:	2.41
Release:	2
License:	GPL
Group:		Networking
Source0:	http://www.cr0.net:8040/code/network/%{name}-%{version}.tgz
# Source0-md5:	05a37c8a165efb11ea226829c809deb3
URL:		http://www.cr0.net:8040/code/network/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Aircrack is a 802.11 WEP key cracker. It implements the so-called
Fluhrer - Mantin - Shamir (FMS) attack, When enough encrypted packets
have been gathered, aircrack can almost instantly recover the WEP key.

%description -l pl.UTF-8
Aircrack to program do łamania szyfrowania WEP dla protokołu 802.11
używający ataku typu FMS (Fluhrer - Mantin - Shamir). Po zgromadzeniu
wystarczającej liczby zaszyfrowanych pakietów aircrack może prawie
natychmiast odtworzyć klucz WEP.

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="-s %{rpmcflags}"


%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	prefix=%{_prefix} \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README.txt linux/patch
%attr(755,root,root) %{_bindir}/*
