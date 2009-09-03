%define		_class		SOAP
%define		_pearname	%{_class}
%define		_status		beta

%define _requires_exceptions pear(SOAP/test/test.utility.php)

Summary:	%{_pearname} - Client/Server for PHP
Name:		php-pear-%{_pearname}
Version:	0.12.0
Release:	%mkrel 3
License:	PHP License
Group:		Development/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
URL:		http://pear.php.net/package/SOAP/
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
Requires:	php-bcmath
Requires:	php-pear-HTTP_Request
Requires:	php-pear-Net_URL
Requires:	php-pear-Net_DIME
BuildArch:	noarch
BuildRequires:	dos2unix
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Implementation of SOAP protocol and services.

In PEAR status of this package is; %{_status}.

%prep

%setup -q -c

find . -type d -perm 0700 -exec chmod 755 {} \;
find . -type f -perm 0555 -exec chmod 755 {} \;
find . -type f -perm 0444 -exec chmod 644 {} \;

for i in `find . -type d -name CVS` `find . -type f -name .cvs\*` `find . -type f -name .#\*`; do
    if [ -e "$i" ]; then rm -rf $i; fi >&/dev/null
done

# strip away annoying ^M
find -type f | grep -v ".gif" | grep -v ".png" | grep -v ".jpg" | xargs dos2unix -U

%install
rm -rf %{buildroot}

install -d %{buildroot}%{_datadir}/pear/%{_class}/{tools,Transport,Server,Type}

install %{_pearname}-%{version}/*.php		%{buildroot}%{_datadir}/pear/%{_class}/
install %{_pearname}-%{version}/tools/*.php		%{buildroot}%{_datadir}/pear/%{_class}/tools
install %{_pearname}-%{version}/Transport/*.php	%{buildroot}%{_datadir}/pear/%{_class}/Transport
install %{_pearname}-%{version}/Server/*.php		%{buildroot}%{_datadir}/pear/%{_class}/Server
install %{_pearname}-%{version}/Type/*.php		%{buildroot}%{_datadir}/pear/%{_class}/Type

install -d %{buildroot}%{_datadir}/pear/packages
install -m0644 package.xml %{buildroot}%{_datadir}/pear/packages/%{_pearname}.xml

%post
if [ "$1" = "1" ]; then
	if [ -x %{_bindir}/pear -a -f %{_datadir}/pear/packages/%{_pearname}.xml ]; then
		%{_bindir}/pear install --nodeps -r %{_datadir}/pear/packages/%{_pearname}.xml
	fi
fi
if [ "$1" = "2" ]; then
	if [ -x %{_bindir}/pear -a -f %{_datadir}/pear/packages/%{_pearname}.xml ]; then
		%{_bindir}/pear upgrade -f --nodeps -r %{_datadir}/pear/packages/%{_pearname}.xml
	fi
fi

%preun
if [ "$1" = 0 ]; then
	if [ -x %{_bindir}/pear -a -f %{_datadir}/pear/packages/%{_pearname}.xml ]; then
		%{_bindir}/pear uninstall --nodeps -r %{_pearname}
	fi
fi

%clean
rm -rf %{buildroot}

%files
%defattr(644,root,root,755)
%doc %{_pearname}-%{version}/example
%dir %{_datadir}/pear/%{_class}
%dir %{_datadir}/pear/%{_class}/tools
%dir %{_datadir}/pear/%{_class}/Transport
%dir %{_datadir}/pear/%{_class}/Server
%dir %{_datadir}/pear/%{_class}/Type
%{_datadir}/pear/%{_class}/*.php
%{_datadir}/pear/%{_class}/tools/*.php
%{_datadir}/pear/%{_class}/Transport/*.php
%{_datadir}/pear/%{_class}/Server/*.php
%{_datadir}/pear/%{_class}/Type/*.php
%{_datadir}/pear/packages/%{_pearname}.xml
