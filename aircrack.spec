Summary:	Tool that cracks 802.11 WEP encryption keys.
Summary(pl):	Program do ³amania szyfrowania WEP dla protoko³u 802.11.
Name:		aircrack
Version:	2.1
Release:	1
License:	GPL
Group:		Networking
Source0:	http://www.cr0.net:8040/code/network/%{name}-%{version}.tgz
# Source0-md5:	694c6180f620b0534e5925a71b960bd1
URL:		http://www.cr0.net:8040/code/network/
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Aircrack is a 802.11 WEP key cracker. It implements the so-called
Fluhrer - Mantin - Shamir (FMS) attack, When enough encrypted packets
have been gathered, aircrack can almost instantly recover the WEP key.

%description -l pl
Aircrack to program do ³amania szyfrowania WEP dla protoko³u 802.11,
u¿ywaj±cy ataku typu FMS.

%prep
%setup -q


%build
%{__make}


%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
        DESTDIR=$RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog docs/*
