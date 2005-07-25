Summary:	Tool that cracks 802.11 WEP encryption keys
Summary(pl):	Program do ³amania szyfrowania WEP dla protoko³u 802.11
Name:		aircrack
%define	beta_ver	beta10
Version:	2.2
Release:	0.%{beta_ver}.1
License:	GPL
Group:		Networking
Source0:	http://www.cr0.net:8040/code/network/%{name}-%{version}-%{beta_ver}.tgz
# Source0-md5:	81d510161155e960ca231464d425bc8d
URL:		http://www.cr0.net:8040/code/network/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Aircrack is a 802.11 WEP key cracker. It implements the so-called
Fluhrer - Mantin - Shamir (FMS) attack, When enough encrypted packets
have been gathered, aircrack can almost instantly recover the WEP key.

%description -l pl
Aircrack to program do ³amania szyfrowania WEP dla protoko³u 802.11
u¿ywaj±cy ataku typu FMS (Fluhrer - Mantin - Shamir). Po zgromadzeniu
wystarczaj±cej liczby zaszyfrowanych pakietów aircrack mo¿e prawie
natychmiast odtworzyæ klucz WEP.

%prep
%setup -q -n %{name}-%{version}-%{beta_ver}

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
