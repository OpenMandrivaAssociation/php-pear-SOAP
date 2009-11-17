%define		_class		SOAP
%define		upstream_name	%{_class}

%define _requires_exceptions pear(SOAP/test/test.utility.php)

Name:		php-pear-%{upstream_name}
Version:	0.12.0
Release:	%mkrel 4
Summary:	Client/Server for PHP
License:	PHP License
Group:		Development/PHP
URL:		http://pear.php.net/package/SOAP/
Source0:	http://download.pear.php.net/package/%{upstream_name}-%{version}.tgz
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
Requires:	php-bcmath
Requires:	php-pear-HTTP_Request
Requires:	php-pear-Net_URL
Requires:	php-pear-Net_DIME
BuildArch:	noarch
BuildRequires:	php-pear
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
Implementation of SOAP protocol and services.

%prep
%setup -q -c
mv package.xml %{upstream_name}-%{version}/%{upstream_name}.xml

%install
rm -rf %{buildroot}

cd %{upstream_name}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%clean
rm -rf %{buildroot}

%post
%if %mdkversion < 201000
pear install --nodeps --soft --force --register-only \
    %{_datadir}/pear/packages/%{upstream_name}.xml >/dev/null || :
%endif

%preun
%if %mdkversion < 201000
if [ "$1" -eq "0" ]; then
    pear uninstall --nodeps --ignore-errors --register-only \
        %{pear_name} >/dev/null || :
fi
%endif

%files
%defattr(-,root,root)
%doc %{upstream_name}-%{version}/example
%{_datadir}/pear/%{_class}
%{_datadir}/pear/packages/%{upstream_name}.xml
